---
layout: default
title : SC18 OSiRIS Sandbox
---
{% include JB/setup %}

Welcome Supercomputing 2018 users!  This sandbox is no longer active but the page is left for reference.  If you have questions about OSiRIS please email <a href="mailto: osiris-help@umich.edu">osiris-help@umich.edu</a>.

OSiRIS has configured a virtual organization 'sandbox' available to anyone at SC18 on SCInet.  The storage used by this VO has a Ceph cache tier overlaid.  This cache is hosted on the hardware in the UM and MSU combined booth:

   <div class="imgwrap" style="width: 70%">
        <a href="{{IMAGE_PATH}}/sc18/OSiRIS-SC18-OverviewDiagram.jpg">
            <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/OSiRIS-SC18-OverviewDiagram.jpg" alt="Conceptual diagram for OSiRIS SC18" />
        </a>
        Conceptual overview of OSiRIS demo at SC18
        </div>

<br style="clear:both" />

There are two available options for accessing OSiRIS storage at SC18.  The maximum available quota for each is 400TB (separate quotas).  Of that, 50TB will fit into local caching pools.  No data will be kept after the conference.  


<h2>NFS Gateway</h2>

NFS gateway using Ganesha-NFS (using a <a href="https://hub.docker.com/r/miosiris/nfs-ganesha-ceph/">Docker container</a>).

The server is configured to squash all users to a single test user for purposes of this demo.  It is only accessible from SCInet VLANS.  To mount create directory of your choice and:
<pre>mount -t nfs sc-stor-nvm01.osris.org:/sc18 /sc18osiris</pre>


<h2>S3 Gateway</h2>

S3 Ceph Radosgw:   
<pre>
https://sc-stor-nvm01.osris.org:8443
</pre>
OR
<pre>
http://sc-stor-nvm01.osris.org:880
</pre>

This works slightly differently and requires enrollment in OSiRIS.  

<ol>
    <li>Visit <a href="https://comanage.osris.org/enroll">comanage.osris.org/enroll</a> and login with your institutional credentials</li>
    <li>Fill in the brief form, and be sure to choose <span style="font-weight: bold;">SC18</span> for the "COU" field on the form (first field).</li>
    <li>Respond to confirmation email</li>
    <li>Wait for 2nd email indicating approval</li>
    <li>Visit again https://comanage.osris.org or refresh the page.</li>
    <li>Obtain S3 credentials by clicking on "Person Menu" at upper-right of page and choosing "My OSiRIS Tokens"</li>
    <li>More details including screenshots in our <a href="http://www.osris.org/documentation/s3.html">documentation</a> (you can use the endpoints documented there to see the penalties imposed by using the SC18 cache tier from distant locations)</li>
</ol> 

If you are unable to complete the enrollment process because of a problem or if you do not belong to any of the available institutions please <a href="mailto:bmeekhof@umich.edu?subject=SC18 Sandbox">email us</a> with subject "SC18 Sandbox" and credentials can be manually created for you.

For more details on our SC18 demo and configuration please have a look at the <a href="{% post_url 2018-11-19-osiris-at-supercomputing-2018 %}">full article</a>.
