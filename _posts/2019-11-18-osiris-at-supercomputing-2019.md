---
layout: post
category : article
title: OSiRIS At Supercomputing 2019
tags : [ sc19, supercomputing, conferences ]
---
{% include JB/setup %}


<div class="imgwrap lf" style="width: 15%">
<a href="https://sc19.supercomputing.org/">
    <img style="width: 100%" class="lf" src="{{IMAGE_PATH}}/sc19/SC19-color-vert.png" alt="SC19 Logo" />
</a>
</div>


<p>The International Conference for High Performance Computing, Networking, Storage, and Analysis: November 17–22, Colorado Convention Center, Denver, CO </p>

Members of the OSiRIS team traveled to SC19 to deploy a pod of equipment in the booth for OSiRIS and <a href="http://slateci.io/">SLATE</a> demos.  We gained valuable experience and data on Ceph cache tiering as well as a new ONIE-based switch running SONiC OS.  

<!--excerpt-->

<br style="clear:both" />

<div class="imgwrap lf" style="width: 32%">
<a href="{{IMAGE_PATH}}/sc19/osiris-booth-posters.jpg">
    <img style="width: 100%" src="{{IMAGE_PATH}}/sc19/osiris-booth-posters.jpg" alt="OSiRIS in Booth" />
</a>
OSiRIS in the UM ARC / MSU iCER booth.
</div>

<div class="imgwrap lf" style="width: 32%">
<a href="{{IMAGE_PATH}}/sc19/osiris-crate-setup.jpg">
    <img style="width: 100%" src="{{IMAGE_PATH}}/sc19/osiris-crate-setup.jpg" alt="Setup" />
</a>
Getting everything connected and ready to go!
</div>

<div class="imgwrap lf"  style="width: 32%">
<a href="{{IMAGE_PATH}}/sc19/scinet-cables.jpg">
    <img style="width: 100%" src="{{IMAGE_PATH}}/sc19/scinet-cables.jpg" alt="SCINet NOC" />
</a>
SCInet provides all conference networking.  Somewhere in here is our OSiRIS 100Gb fiber path back to Michigan.
</div>
<br style="clear:both" />

<h2>OSiRIS SC19 Storage and Network Demos</h2>

<div class="imgwrap rf"  style="width: 32%; padding-bottom: 50px;">
<a href="{{IMAGE_PATH}}/sc19/osiris-nre-booth-sign.jpg">
    <img style="width: 100%;" src="{{IMAGE_PATH}}/sc19/osiris-nre-booth-sign.jpg" alt="OSiRIS NRE Poster on SCINet NOC booth" />
</a>
OSiRIS NRE demo poster on SCINet NOC booth
</div>

Our demonstration this year was focused on stress-testing Ceph cache tiering for use in responsive, dynamic deployments.  We know from <a href="{% post_url 2016-11-18-osiris-at-supercomputing-2016 %}">previous</a> <a href="{% post_url 2018-11-19-osiris-at-supercomputing-2018 %}">years</a> that a cache tier can be use to provide IO boosts to geographically local clients.  We also know that it becomes a disadvantage for any clients with high latency to the cache.  What if we could create a more responsive system for managing caches which spins them up on demand and then removes them once the demand has moved to a different location?  That was our goal this year:   To find out how our Ceph cluster will respond to rapidly deploying, filling, draining, and removing cache tiers at SC19.  

Also in the works was a plan to showcase SDN-based quality-of-service (QoS) techniques using OpenVSwitch, network monitoring, and declarative, programmatic control of the networking using a domain-specific language called Flange incorporated by our NMAL team at IU.  The combined tools were to be used to manage the Ceph traffic between our local SC OSiRIS deployment and the WAN links to our core deployment in Michigan.  Unfortunately the late arrival of our equipment and difficulties with our switch platform prevented us from collecting significant data in this area.  

<h2>Ceph Cache Tier Rapid Deployment Tests</h2>

OSiRIS already uses Ceph cache tiering for users at the <a href="/domains/vai.html">Van Andel Institute</a> in Grand Rapids.  It works well for them but for users at other sites who might want to access the same data the tier location is a disadvantage.  Either the data needs to be moved to another pool without a cache or the cache drained and removed so other users can access the data more rapidly from storage at our 3 core sites.  What we envision is a service that responds to client demands and manages cache pools as needed.  Lots of usage at a site with available storage for deploying a cache tier?  Spin up a cache.  Demand changes, more usage elsewhere?  Drain the cache, spin one up where the demand is highest.  

So how will Ceph respond to using this feature as we envision?  Typical cache deployment is static and unchanged once configured.  This is how we have used it so far in production and testing.  Our testing at SC19 confirmed that a more dynamic scenario is possible.

We used a <a href="https://github.com/MI-OSiRIS/ceph-mgr-cachetier/blob/master/cache-test.sh">simple script</a> to create a cache tier on NVMe storage at SC19 while simultaneously doing rados read/write benchmarks on several clients. The results were promising!  Ceph chugged along happily while creating, filling, draining, and repeating for at least 10 runs.  We didn't see any signs of errors or problems.  The only notable thing is that sometimes the 'cache-flush-evict-all' command did not completely flush the cache.  The overlay remove commands would then fail because the cache was not empty.  Repeating the evict command until the cache is truly empty resolves the issue .  

Below you can see the interaction between the cache pool sc19-test2-michigan.cache and the backing pool sc19-test2-michigan as we repeatedly fill and flush the cache.  Between benchmarks the data was cleaned up.  
<div class="imgwrap">
<a href="{{IMAGE_PATH}}/sc19/Bytes-used-cache-test.png">
    <img style="width: 100%" src="{{IMAGE_PATH}}/sc19/Bytes-used-cache-test.png" alt="Pool space usage during cache deployment" />
</a>
Data used in cache and backing pools as we repeat cycle of cache fill, drain, and removal.  
</div>

<p>Another view during the test shows data throughput to each pool.</p>

<div class="imgwrap">
<a href="{{IMAGE_PATH}}/sc19/Pool-throughput-cache-test.png">
    <img style="width: 100%" src="{{IMAGE_PATH}}/sc19/Pool-throughput-cache-test.png" alt="Pool space usage during cache deployment" />
</a>
Throughput to cache and backing pools showing cache pool fill, drain, removal, and repeat of cycle.    
</div>

The testing we're doing here will inform work on a proof-of-concept cache tier module for the Ceph mgr daemon.  An early version of the module code is available <a href="https://github.com/MI-OSiRIS/ceph-mgr-cachetier">in this repository</a>.  This module should never be used on any production cluster.  In fact it does not at this point do much of anything but make a first pass at implementing the basic architecture for creating and tearing down cache tier pools based on geographic location.  More information is in the README file.  

<h2>Open Source Networking:  A Learning Experience</h2>

<div class="imgwrap lf"  style="width: 32%; padding-bottom: 10px">
<a href="{{IMAGE_PATH}}/sc19/wedge-switch-closeup.jpg">
    <img style="width: 100%; margin: 10px" src="{{IMAGE_PATH}}/sc19/wedge-switch-closeup.jpg" alt="Wedge 100 switch" />
</a>
Wedge 100BF ONIE switch installed in our SC19 booth rack
</div>

Open platform switches running open source software are an exciting development in networking architecture.  For Supercomputing and for our continued experimentation an Edge-Core <a href="https://www.edge-core.com/productsInfo.php?cls=1&cls2=5&cls3=181&id=335">Wedge 100BF-32X</a> switch was acquired.  This switch can run a variety of open network operating systems compatible with the Open Network Install Environment (ONIE).  There are many available switch hardware platforms with this capability.  For the switch OS we chose <a href="https://azure.github.io/SONiC">SONiC</a>.  



What we learned about open networking will help us use this type of equipment more effectively in our networking management and automation goals for the project.  Open networking OS are a rapidly evolving area.  Even in the weeks leading up to Supercomputing a new <a href="https://github.com/Azure/SONiC/wiki/Sonic-Roadmap-Planning">SONiC release</a> came out which added new CLI capabilities relevant to our configuration.  Like many cutting-edge developments there is sometimes a need to spend some time digging into options and configuration that might not be obvious at first glance.  

After some initial troubles we were able to use the switch for 100G connectivity to our nodes at the show.  A few things we discovered:
<ul>
    <li>
        A Null packet sent during initial negotiation would disable the 100G fiber link to SCInet.  Our solution?  Plug in the TX half of the fiber pair, but leave RX unplugged for a few seconds so the switch never sees the problematic packet.  Then plug in RX and everything is good to go!  An <a href="https://github.com/Azure/SONiC/issues/521">issue has been opened</a> for further diagnosis. 
    </li>
    <li>
        Putting switch ports into a VLAN with 'untagged' setting caused all ports to go down.  We never did figure out what we were doing wrong here and ended up using a tagged config on the switch and host ports.  
    </li>
    <li>
        Buffer sizes need to be configured manually based on connected cable length.  SONiC has some design and planning documentation on their wiki <a href="https://github.com/Azure/SONiC/wiki/Buffers-Configuration-Update-design">here</a> and  <a href="https://github.com/Azure/SONiC/wiki/Run-Time-Buffers-Configuration-Update-design">here</a> as well as instructions on <a href="https://github.com/Azure/SONiC/wiki/Converting-old-or-creating-new-buffers-config">manually setting the configuration</a>.  
    </li>
</ul>

All of this experience was valuable!  Supercomputing gives us a chance to try things out in real-world environments.  Sometimes the pace can be frantic trying to get everything working but by the end of the week everything was online and our demo running.  

<h2>Campus Support</h2>

We couldn't have done this without the support from our University campuses!  Our campus networking teams at MSU, WSU, and U-M were responsible for coordination, configuration, and testing a 100Gbit path from Michigan to the SC19 floor.  Thanks is also due to Merit Networks, Internet 2, Juniper, and Adva for network paths or equipment enabling our 100Gbit link.  

<div class="imgwrap rf" style="width:19%; padding-top: 1em;">
<a href="https://arc.umich.edu/">
    <img style="width: 100%" src="{{IMAGE_PATH}}/logos/arc_logo_square.png" alt="U-M Advanced Research Computing Logo" />
</a>
</div>

<div class="imgwrap rf" style="width: 15%">
<a href="https://icer.msu.edu/">
    <img style="width: 100%" src="{{IMAGE_PATH}}/logos/msu_logo_square.png" alt="MSU Logo" />
</a>
</div>

The SC19 show booth is a collaboration between U-M <a href="https://arc.umich.edu">Advanced Research Computing</a> and the MSU <a href="https://icer.msu.edu">Institute for Cyber-Enabled Research</a> to promote research computing at our institutions.  
