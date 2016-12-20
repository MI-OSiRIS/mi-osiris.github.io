---
layout: post
category : article
title: Ceph Cache Tiering with LIQID NVMe Drives at SC16
tags : [ sc16, supercomputing, conferences, ceph ]
---
{% include JB/setup %}

Ceph has the capability to 'overlay' pools with a cache pool.  Typically a cache pool would reside on faster storage to speed up client RW operations for frequently used data.

<div class="rf imgwrap" style="width:50%; margin-bottom: 20px;">
<a href="{{IMAGE_PATH}}/sc16/CephCacheTierDiagram.png"><img src="{{IMAGE_PATH}}/sc16/CephCacheTierDiagram.png" alt="Ceph cache overlay illustration" style="width: 100%"></a>
This image taken from the <a href="http://docs.ceph.com/docs/master/rados/operations/cache-tiering/">Ceph website</a> illustrates a cache overlay
</div>

At SC16 we experimented with using a cache pool to overcome some of the speed handicaps inherent in having OSD separated by high latencies.  The theory was that a cache pool local to clients at SC16 would speed up writing in cases where the data could be written without needing to flush the cache.  

Our cache pool devices were LIQID NVMe drives in hardware purchased from <a href="http://2crsi.com">2CRSI</a>.  One LIQID drive card is 4 x 800GB devices, and each box contained two cards for a total of 16 Ceph OSD available for use as a cache pool. 

<br style="clear:right" />
<!--excerpt-->  

We used the 'rados bench' util from a client at SC to take several benchmarks.  Three pool configurations were tested:

* 3 replicas, mapped to UM, WSU, MSU, and SC16 sites.    
* 3 replicas, mapped as previous, with a cache pool overlaid.  The cache is mapped to the 2 NVMe hosts at SC16 with 2 replicas (16 total NVMe OSD)
* 2 replicas, mapped to NVMe hosts at SC16 to get an idea of max performance of our all-NVMe pool

The results were very interesting and seemed to clearly indicate the advantages of this cache configuration in overcoming the high latency between SC and our Michigan sites.  We can probably assume that at some point the cache pool would have to start flushing back to the underlying HDD pool and we would then see client throughput drop long term.  Our test was not long enough in duration to see this happen.

We plotted the rados bench output for comparison:

<h4>Write Throughput and Latency</h4>
<div class="imgwrap" style="width:80%">
<a href="{{IMAGE_PATH}}/sc16/CacheOverlay-WriteThroughput.png"><img src="{{IMAGE_PATH}}/sc16/CacheOverlay-WriteThroughput.png" alt="Rados Bench Write Throughput" style="width: 100%"></a>
</div>

<div class="imgwrap" style="width:80%">
<a href="{{IMAGE_PATH}}/sc16/CacheOverlay-WriteLatency.png"><img src="{{IMAGE_PATH}}/sc16/CacheOverlay-WriteLatency.png" alt="Rados Bench Write Latency" style="width: 100%"></a>
</div>
<br style="clear: both;"/>
<h4>Read Throughput and Latency</h4>
<div class="lf imgwrap" style="width:80%">
<a href="{{IMAGE_PATH}}/sc16/CacheOverlay-ReadThroughput.png"><img src="{{IMAGE_PATH}}/sc16/CacheOverlay-ReadThroughput.png" alt="Rados Bench Read Throughput" style="width: 100%"></a>
</div>

<div class="imgwrap" style="width:80%">
<a href="{{IMAGE_PATH}}/sc16/CacheOverlay-ReadLatency.png"><img src="{{IMAGE_PATH}}/sc16/CacheOverlay-ReadLatency.png" alt="Rados Bench Read Latency" style="width: 100%"></a>
</div>

Based on this experience we plan to do more tests with cache pools to optimize access to our project for science groups concentrated at individual institutions.  The tradeoff here is that clients which might be closer to other OSD still have to push all writes through the cache pool OSD and perhaps suffer increased latency in that respect.

<h2>Configuring a cache tier</h2>

So how do we configure a pool that is isolated to these devices, and then set that pool as cache?  

We modify the Ceph crush map first.  We'll need a new 'root' to isolate the NVMe OSD from the root used by the default crush ruleset.  

<pre>ceph osd crush add nvmecache root</pre>

To begin our new root is empty:

<pre>
ceph osd tree
...
ID      WEIGHT  TYPE NAME   
-24         0   root nvmecache                                                     
-1 2488.07227   root default                                                       
-7 1658.72217     member um 
</pre>

Now we'll move our NVMe hosts into the new root.  Alternately, we could set the osd_crush_location in /etc/ceph.conf before bringing up the OSD for the first time.  

<pre>
ceph osd crush move sc-stor02 nvmecache
</pre>

Example of ceph.conf to have the OSD on node come up in the desired location:

<pre>
[osd]
	osd_crush_location = root=nvmecache host=sc-stor02 rack=crate-1 building=salt-palace member=sc
</pre>

Once that is done then we'll need a crush rule to use the new root.  For a simple rule we can create on command line:

<pre>
osd crush rule create-simple cachetier nvmecache host firstn
</pre>

Which generates a rule that looks like this.  You could also dump the whole map, decompile, add this rule, and then set the updated map (detailed in <a href="http://docs.ceph.com/docs/master/rados/operations/crush-map/">Ceph documentation</a>)

<pre>
rule cachetier {
    ruleset 3
    type replicated
    min_size 1
    max_size 10
    step take nvmecache
    step chooseleaf firstn 0 type host
    step emit
}
</pre>
With the prerequisites in place we created a pool using the cachetier rule, and two pools in the standard root replicated across UM, WSU, MSU, and SC16.  One of the pools is then overlaid with the cache tier, the other left for comparison.

Create pool of NVMe devices:
<pre>
ceph osd pool create foo-hot 4096 4096 cachetier
ceph osd pool set foo-hot size 2
</pre>

Create regular pool with default size 3 replication:
<pre>
ceph osd pool create foo 4096 4096 
ceph osd pool set foo size 3
</pre>

Finally we set the NVMe pool as an overlay:
<pre>
ceph osd tier add foo foo-hot
ceph osd tier cache-mode foo-hot writeback
ceph osd tier set-overlay foo foo-hot
</pre>

<hr>
Thanks to Michael Thompson (WSU) and Charlie Miller (MSU) for their work on configuration and benchmarking.

More information on Ceph cache configuration: <a href="http://docs.ceph.com/docs/master/dev/cache-pool/">http://docs.ceph.com/docs/master/dev/cache-pool/</a>

