---
layout: post
category : article
title: Cache Tier Demo at SC18
tags : [ sc18, supercomputing, conferences, ceph ]
---
{% include JB/setup %}

<div class="imgwrap rf" style="width: 30%">
<a href="{{IMAGE_PATH}}/sc18/crate-rear-cropped.jpg">
    <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/crate-rear-cropped.jpg" alt="Equipment Crate Rear View" />
</a>
Demo Equipment 
</div>

At Supercomputing 2018 the OSiRIS project configured a Ceph storage node with 60 OSD to host cache tier pools.  This gave us approximately 600TB of raw caching space, or 200TB with 3x replicated pools.  For purposes of testing we replicated pools on just a single host but in a production setup a more resilient set of OSD would be desirable.  
<!--excerpt-->

Below is an overview of the setup:


 <div class="imgwrap" style="width: 70%">
        <a href="{{IMAGE_PATH}}/sc18/OSiRIS-SC18-OverviewDiagram.jpg">
            <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/OSiRIS-SC18-OverviewDiagram.jpg" alt="Conceptual diagram for OSiRIS SC18" />
        </a>
        </div>

We used the SC18 node to host cache overlays for Radosgw, CephFS, and direct Rados.

A 2nd node at SC hosted gateway or client services - Ganesha NFS and Radosgw.  For Ganesha we used version 2.6 from our <a href="https://hub.docker.com/r/miosiris/nfs-ganesha-ceph/">Docker image</a>.  Radosgw was configured to use the new <a href="http://docs.ceph.com/docs/mimic/radosgw/frontends/">Beast</a> frontend in Mimic.  Typically we run HAproxy in front of several instances but for this event we just ran one standalone.  

Normally with a Ceph client geographically far away from the Ceph OSD it is expected that higher latency decreases IOPS and overall throughput.  The latency between Dallas and our sites in Michigan is about 25ms.  The latency between our sites in Michigan is more like 2-3ms and latency between hosts in the same datacenter is less than 1ms.  

The performance hit from latency is extremely obvious when communicating with the cluster directly via RADOS.  Below is a plot showing Latency, IOPS and Throughput averages.  The tests labeled 'Michigan Storage' use a pool on OSD in Michigan (WSU/MSU/UM).  The tests labeled 'SC18 Cache' use a pool also located in Michigan but with a cache tier overlaid which is using OSD at SC18.  During the duration of the test the cache tier does not flush back to Michigan.   

 <div class="imgwrap" style="width: 80%">
        <a href="{{IMAGE_PATH}}/sc18/sc18-rados-bench-comparison.png">
            <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/sc18-rados-bench-comparison.png" alt="Rados benchmarks with and without cache tier" />
        </a>
        Rados bench average with and without cache tier, 120s duration test
        </div>

The differences here are fairly obvious and dramatic.  Reducing the latency for client communications greatly increases the numbers.  With a large enough cache one could reasonably keep enough 'hot' data that latency delays would be rare.  Unfortunately other unrelated issues invalidated the results during a read test from the Michigan storage pool but the result would most likely be slower than similar tests with cache tier as with the write test.  

But we also did some tests with other services.  Below are the results from running tests with swift bench.  We tried 4 scenarios here all using a swift-bench client at SC18:
<ul>
    <li>RGW service at SC18, using cache overlay at SC18</li>
    <li>RGW service in Michigan, using cache overlay at SC18.  The idea here was to see how great a penalty is incurred when clients in Michigan are forced to direct writes through a far-away cache tier.  The Michigan RGW service is backed by 3 RGW instances behind HAproxy. </li>
    <li>RGW service at SC18 using pool in Michigan with no cache overlay</li>
    <li>RGW service in Michigan using pool in Michigan with no cache overlay</li>
</ul>

 <div class="imgwrap" style="width: 80%">
        <a href="{{IMAGE_PATH}}/sc18/sc18-swift-bench-comparison.png">
            <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/sc18-swift-bench-comparison.png" alt="Swift benchmarks with and without cache tier" />
        </a>
        Swift bench average with and without cache tier
        </div>

Our flags to swift bench were:
<pre>
 -c 32 (number of concurrent connections
 -s 8192 (object size max bytes)
 -l 512 (object size lower limit) 
 -n 50000 (number of objects to put)
 -g 50000 (number of gets)
</pre>

The differences here are visible as well.  The RGW instance at SC18 predictably does higher ops/s when utilizing the cache tier.  One anomaly is the slightly higher PUT ops for the SC18 RGW utilizing storage placed back in Michigan.  This figure is an average and both tests hit similar peaks during the run so I think we can attribute this to some other factor and call them approximately equal with the upper limit determined by the capabilities of a single radosgw instance.

Another thing we notice is that the SC18 swift client bench achieves a higher rate of PUTS/s when using the Michigan RGW installation with Michigan storage.  This is most likely because there are more RGW instances processing requests behind this endpoint URL.  Noting as well the fairly small difference in GETS and DELS between SC18 RGW with cache (top test) and Michigan RGW (bottom test) it seems that the latency between client and RGW endpoint is not much of a factor as it is with RADOS itself.  This may be unsurprising given that Rados clients communicate more directly with storage elements involved but useful to document nonetheless. 

We also deployed a Ganesha NFS instance using the Ceph FSAL and ran iozone tests against directories placed on pools with and without cache tier.  In this case there is almost no difference between the results - it looks like the NFS stack is caching these ops since the files are relatively small.  There seems only to be a slight boost to writes at higher record sizes.  


 <div class="imgwrap" style="width: 80%">
    <a href="{{IMAGE_PATH}}/sc18/sc18-iozone-throughput-comparison.png">
        <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/sc18-iozone-throughput-comparison.png" alt="IOZone throughput results with and without cache tier" />
    </a>
    IOZone throughput results with and without cache tier
</div>

<br />

<div class="imgwrap" style="width: 80%">
    <a href="{{IMAGE_PATH}}/sc18/sc18-iozone-iops-comparison.png">
        <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/sc18-iozone-iops-comparison.png" alt="IOZone IOPS results with and without cache tier" />
    </a>
    IOZone IOPS results with and without cache tier
</div>

Given the similarity of results it's worth verifying that the test pools were configured and utilized as expected.  We can see this on the plots collected from ceph-mgr via the <a href="{ post_url 2017-12-7-the-influxdb-ceph-mgr-plugin %}">influxdb module</a>.

These plots align with the tests as follows:  

22:23 iops/cache, 1:44 througput/cache, 3:42 iops/nocache, 6:01 throughput/nocache

<div class="imgwrap lf" style="width: 45%">
    <a href="{{IMAGE_PATH}}/sc18/sc18-iozone-pool-throughput.png">
        <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/sc18-iozone-pool-throughput.png" alt="Pool data throughput during 4 tests" />
    </a>
    Pool data throughput
</div>

<div class="imgwrap" style="width: 45%">
    <a href="{{IMAGE_PATH}}/sc18/sc18-iozone-pool-objs.png">
        <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/sc18-iozone-pool-objs.png" alt="Pool objects written" />
    </a>
    Pool objects written (negative is objects removed)
</div>

As you can see the pool utilization is different depending which directory the tests were utilizing and is consistent with our expectations for using or not using cache pools.  

<h2>Conclusions</h2>

These tests show that in general there is a quite significant boost for rados clients when a high-latency pool is overlaid with a cacher tier having much lower latency to the client.  Likewise there is a benefit if the radosgw service has lower latency to a cache tier.  Less significant is the latency between S3/Swift client and RGW instance - in fact we saw that having more RGW instances working on requests produced higher PUTS / Second than a single instance even with more latency between the client and RGW instances.

Where we saw much less benefit or difference was with NFS exports.  However our benchmarks do show that as files are written with larger block sizes the cache tier does begin to play a role in increasing IOPS and Throughput.  Most likely if we had done tests with larger file sizes we'd see a greater effect here.   

A cache tier arrangement like this is not relevant to every use case.  In fact it has significant disadvantages for users who might see higher latency to the cache components but lower latency to the main storage pool.  For the right use case it can make a lot of sense and allow for small storage installations backed by the resources of the entire OSiRIS project.   


  



