---
layout: post
category : article
title: Cache Tier Demo at SC18
tags : [ sc18, supercomputing, conferences, ceph ]
---
{% include JB/setup %}

<div class="imgwrap rf" style="width: 30%">
<a href="{{IMAGE_PATH}}/sc18/crate-posters.jpg">
    <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/crate-posters.jpg" alt="Equipment Crate" />
</a>
Demo Equipment 
</div>

At Supercomputing 2018 the OSiRIS project configured a Ceph storage node with 60 OSD to host cache tier pools.  This gave us approximately 600TB of raw caching space, or 200TB with 3x replicated pools.  For purposes of testing we replicated pools on just a single host but in a production setup a more resilient set of OSD would be desirable.  Below is a rough overview of the setup:

 <div class="imgwrap" style="width: 70%">
        <a href="{{IMAGE_PATH}}/sc18/OSiRIS-SC18-OverviewDiagram.jpg">
            <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/OSiRIS-SC18-OverviewDiagram.jpg" alt="Conceptual diagram for OSiRIS SC18" />
        </a>
        </div>



We used the SC18 node to host cache overlays for Radosgw, CephFS, and direct Rados.

A 2nd node at SC hosted gateway or client services - Ganesha NFS and Radosgw.  For Ganesha we used version 2.6 from our <a href="https://hub.docker.com/r/miosiris/nfs-ganesha-ceph/">Docker image</a>.  Radosgw was configured to use the new <a href="http://docs.ceph.com/docs/mimic/radosgw/frontends/">Beast</a> frontend in Mimic.  Typically we run HAproxy in front of several instances but for this event we just ran one standalone.  

Normally with a Ceph client geographically far away from the Ceph OSD it is expected that higher latency decreases speed and overall throughput.  We can see that below in these benchmarks with Rados, CephFS, and NFS from clients here at the show.  In these tests the data pool is located on our usual sites in Michigan with network latency of approximately 25ms.  



