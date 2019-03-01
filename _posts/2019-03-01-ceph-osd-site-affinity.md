---
layout: post
category : article
title: Setting Primary OSD For Read Optimization
tagline: 
tags : [ ceph ]
---
{% include JB/setup %}
<span style="font-style: italic;">Michael Thompson, Wayne State University</span>

<div class="imgwrap rf" style="width: 30%">
<a href="{{IMAGE_PATH}}/affinity/ceph-primary-osd-arch.png.png">
    <img style="width: 100%" src="{{IMAGE_PATH}}/affinity/ceph-primary-osd-arch.png" alt="Ceph Primary and Secondary OSD architecture" />
</a>
Image from Ceph architecture documentation
</div>

OSiRIS introduces a new variable to Ceph with the respect to placement of data containers (placement groups or PG) on data storage devices (OSD).  Ceph by default stores redundant copies on randomly selected OSDs within failure domains defined by the CRUSH map.  Typically a failure domain is a host, rack, etc and PG replica have fairly low latency between each other.

The OSiRIS project is structured such that PG might be in different cities or even states with much higher network latency between them.  This certainly effects overall performance but we do have some options to optimize for certain use cases.  One of these options is setting our CRUSH rules to prefer one site or another for the Primary OSD when allocating PG copies.  Based on our testing this is a great way to boost read I/O for certain use cases.    

<br style="clear:both;"/>

<!--excerpt-->

When a Ceph client reads or writes data it uses the CRUSH map to determine the primary OSD from among the available replication locations.  This is then used directly to read or write data.  The primary, unless strategically specified through the crush tree, is randomly selected by the CRUSH map from all available replication buckets.   In a configuration like ours with copies spread across N locations the result is (N-1)/N of the all reads come from OSDs in non-proximate locations.

What if we have a case where most data usage occurs at a particular location?  Obviously one solution is to allocate all the PG copies at that location - but then we can only leverage the storage at that location, and if there is an issue at the site the data is unavailable.  Another solution is to modify the CRUSH map to prefer that site for the primary (first) OSD.  All client direct I/O will come from the OSD at the site specified.  Read operations will never hit the network latency of having to traverse to other sites as long as the primary is up.  For write operations the client won't have to communicate with offsite replicas but the OSD will need to replicate the write so there is much less effect on write I/O for this configuration.  

<h2>Setting Primary OSD with CRUSH rules</h2>

<p style="margin-top: 30px;">

<div class="imgwrap lf" style="width: 50%">
<a href="{{IMAGE_PATH}}/affinity/ceph_crush_default.jpg">
    <img style="width: 100%" src="{{IMAGE_PATH}}/affinity/ceph_crush_default.jpg" alt="Typical CRUSH Rule" />
</a>
Typical CRUSH Rule allocating copies to OSiRIS 'member' sites (WSU,MSU,UM)
</div>
This rule identifies the rule as #0, replicated as opposed to erasure encoded, has a minimum of 1 and a maximum of 10 replicas required for I/O, chooses a random OSD from the root (default) of the tree from any one member and repeats the process from unique members until the PG has reached the required number of OSDs.
</p>

<br style="clear:both;"/>

<p style="margin-top: 30px;">
<div class="imgwrap lf" style="width: 50%;">
<a href="{{IMAGE_PATH}}/affinity/ceph_crush_affinity.jpg">
    <img style="width: 100%" src="{{IMAGE_PATH}}/affinity/ceph_crush_affinity.jpg" alt="CRUSH Rule with affinity for WSU site" />
</a>
Example of a crush rule configured to optimize reads for WSU OSiRIS site
</div>

This crush rule is intended to optimize reads for systems physically located at the WSU site and targets the WSU branch of the crush tree when selecting the first OSD.  The first OSD chosen for a given PG becomes the primary OSD for the respective PG.  Only the active primary OSD is read when reads are requested from any given PG.  The remainder of the above crush rule places up to 2 replicas at the other 2 OSiRIS sites with any additional replicas being placed at any of the 3 sites ('members'). 
</p>

<br style="clear:both;"/>

<h2>Results</h2>

At <a href="{% post_url 2018-11-19-osiris-at-supercomputing-2018 %}">Supercomputing 2018</a> we applied this configuration using storage on the conference floor to host the primary OSD and compared it to reading from storage allocated with primary OSD at sites in Michigan.  

<div class="imgwrap" style="/*width: 30%*/">
<a href="{{IMAGE_PATH}}/affinity/sc18_affinity_summary.jpg">
    <img style="width: 100%" src="{{IMAGE_PATH}}/affinity/sc18_affinity_summary.jpg" alt="SC18 Benchmark Summary" />
</a>
Benchmark results compared to using the default PG during Super Computing 2018</div>

We experienced reads between 400 MBytes/sec and 900 MBytes/sec when the operations included remote sites with higher latency (Dallas,TX to Michigan).  When the primary OSD was mapped to the same location as the client we saw approximately 1,200 MBytes/sec.  We continued this testing after SC and depending on the conditions at the time of test we would often see 100% improvement by setting the primary OSD closer to the client vs a random allocation at all three sites.  The image above details all of these results.

<h2>Conclusion</h2>
Typically the architecture of Ceph is highly sensitive to latency between storage components.  However, the flexibility of CRUSH maps does leave some room for optimization to avoid this issue.  Adjusting the location of the primary OSD is one option that avoids having all copies of the data at one location while still giving that location a boost to read operations.  It may also boost write operations to some extent but those are generally going to be still limited by the latency of replicating to offsite OSD.  The obvious downside is that it also increases latency to clients not in proximity to the primary OSD.  For some applications this particular set of tradeoffs may be a good fit.  

OSiRIS also uses Ceph cache tiering to help work around latency issues.  More information is linked below.  

<h2>More Information</h2>

<a href="http://docs.ceph.com/docs/mimic/rados/operations/crush-map
">Working with the Ceph CRUSH Map
</a>

<a href="http://docs.ceph.com/docs/master/architecture/">Ceph Architecture Overview</a>

<a href="{% post_url 2018-11-15-ceph-cache-tiering-demo-at-sc18 %}">OSiRIS Ceph cache tiering benchmarks at SC18</a>

<a href="/domains/vai.html">OSiRIS cache tier deployment at Van Andel Institute</a>








