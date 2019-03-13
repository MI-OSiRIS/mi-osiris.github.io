---
layout: default
title : Ceph Rados Gateway Tuning
---
{% include JB/setup %}

<h2>RGW threads, handles, and connection rates</h2>

Ceph RGW has three params available to tune performance.  They are listed below with the defaults that you get if not configured at all.  The num_threads param is one of several that might be specified to civetweb.  For example, a typical rgw_frontends param might also include 'port = xxx' and such.  
<pre>
# Default values shown 
rgw_num_rados_handles = 1
rgw_frontends = civetweb num_threads = 50
rgw_thread_pool_size = 100
</pre>

We used 5 hosts running swift-bench to establish some benchmark numbers and tune.  The following command was used, run in parallel on five hosts via <a href="https://github.com/grondo/pdsh">pdsh</a>.  The swift bench config was sourced from a network location all 5 hosts can read.  

<pre>
5 clients parallel:  swift-bench -c 64 -s 4096 -n 100000 -g 100000 swift.conf 

-c number of concurrent connections
-s size of objects (bytes)
-n number of puts
-g number of gets
</pre>

The swift.conf file is simple:
<pre>
[bench]
auth = http://host:1234/auth/v1.0
user = testuser:swift
key = XXXYYY
auth_version = 1.0
</pre>

For these tests we also disabled the rgw cache.  Its another variable that can effect repeatability, it skews results higher and requires much longer tests to smooth out the initial performance peaks.  

We know already from usage experience that the default settings are not ideal.  However, let's do a run and see where we stand using swift-bench.  Note that the test duration (number of ops) is shorter here to avoid waiting for what we know will be a fairly slow rate:
<div class="imgwrap">
<a href="{{IMAGE_PATH}}/performance/rgw/RgwDash-default.png">
	<img src="{{IMAGE_PATH}}/performance/rgw/RgwDash-default.png" style="width: 100%">
</a>
	Swift-bench test with default configuration
</div>

In later tests we'll see that the parallel requests are all serviced in parallel.  In this test the requests end up being serviced over a long time window taking about 7 minutes to get through the whole test.  On the client side, we started to see connection timeouts after a few minutes.  Mostly what we learned here is that the default config can't keep up with the load imposed by our benchmark.  

Next we adjusted both thread settings to 512 and tried various higher settings for the handles.  

<pre>
rgw_num_rados_handles = range from 8 - 32
rgw_frontends = civetweb num_threads = 512
rgw_thread_pool_size = 512
rgw_cache_enabled = false
</pre>

<div class="imgwrap">
<a href="{{IMAGE_PATH}}/performance/rgw/RgwDash-512t-vhandles.png">
	<img src="{{IMAGE_PATH}}/performance/rgw/RgwDash-512t-vhandles.png" style="width: 100%">
</a>
	Swift-bench test with variable num_rados_handles setting and 512 threads
</div>

Here we see that things move along a lot quicker and all the requests can be serviced in parallel.  Tests always have an initially high peak but settle to a sustained number.  So far it appears that increasing the rados handles in this context slightly decreases performance.

So lets move on to increasing the civetweb num_threads and rgw_thread_pool_size to see if performance can be increased correspondingly.

<pre>
rgw_num_rados_handles = range from 8 - 32
rgw_frontends = civetweb num_threads = 1024
rgw_thread_pool_size = 1024
rgw_cache_enabled = false
</pre>


<div class="imgwrap">
<a href="{{IMAGE_PATH}}/performance/rgw/RgwDash-1024t-vhandles.png">
	<img src="{{IMAGE_PATH}}/performance/rgw/RgwDash-1024t-vhandles.png" style="width: 100%">
</a>
	Swift-bench test with variable num_rados_handles setting and 1024 threads
</div>

Overall our performance is lower for the same rados_handles settings as in the previous test.  The trend is somewhat similar with slightly decreasing performance for more handles.  

So far it looks like there isn't any reason to increas threads beyond 512 and rados handles beyond 8 - in fact it is detrimental.  Let's also hit some data points with higher settings to further verify.

<pre>
rgw_num_rados_handles = range from 32 - 64
rgw_frontends = civetweb num_threads = 2048
rgw_thread_pool_size = 2048
rgw_cache_enabled = false
</pre>

<div class="imgwrap">
<a href="{{IMAGE_PATH}}/performance/rgw/RgwDash-2048t-32h-64h.png">
	<img src="{{IMAGE_PATH}}/performance/rgw/RgwDash-2048t-32h-64h.png" style="width: 100%">
</a>
	Swift-bench test with variable num_rados_handles setting and 2048 threads
</div>

The numbers just get worse!

Earlier it was noted that the rgw cache was disabled for these tests.  We repeated the tests with the best and worst configurations with cache enabled as well.

<pre>
rgw_num_rados_handles = range from 8, 64, 128
rgw_frontends = civetweb num_threads = 512, 2048
rgw_thread_pool_size = 512, 2048
rgw_cache_enabled = true
</pre>

<div class="imgwrap">
<a href="{{IMAGE_PATH}}/performance/rgw/RgwDash-withcache.png">
	<img src="{{IMAGE_PATH}}/performance/rgw/RgwDash-withcache.png" style="width: 100%">
</a>
	Swift-bench test with variable num_rados_handles setting and 1024 threads, rgw cache enabled
</div>

Overall numbers are higher, in fact much higher for the best configuration.  But the relative trend is the same.  

The rate of puts/second was so high for the first configuration in this test that it finished 100000 operations very quickly.  Possibly this is just a brief peak and not the true sustained rate.  One more test was done with the same config and 400000 operations to get a longer test.  Spread out over a longer time period we see the same peak followed by sustained rate as we saw in the previous tests.

<pre>
rgw_num_rados_handles = 8
rgw_frontends = civetweb num_threads = 512
rgw_thread_pool_size = 512
rgw_cache_enabled = true
</pre>

<div class="imgwrap">
<a href="{{IMAGE_PATH}}/performance/rgw/RgwDash-withcache-512t-8h-long.png">
	<img src="{{IMAGE_PATH}}/performance/rgw/RgwDash-withcache-512t-8h-long.png" style="width: 100%">
</a>
	Longer swift-bench test with 8 rados handles and 512 threads, rgw cache enabled
</div>

That was a lot of testing to reach two simple conclusions, but hopefully these data points are useful nonetheless.   

<ul>
	<li>In the context of our tests with multiple concurrent clients and small objects 512 threads and 8 rados handles outperforms any higher settings in terms of operations / second.  Boosting those parameters higher just results in using more memory and less performance.</li>
	<li>Rados gateway cache significantly boosts performance, as expected.  The default setting is enabled and there's no reason to disable it in normal usage.  We did it here to reduce variables for the tests.</li>
</ul>

Further documentation of Ceph RGW and the civetweb embedded component is available from their respective websites:

<a href="http://docs.ceph.com/docs/kraken/radosgw/config-ref/">Ceph RGW config reference</a>

<a href="https://github.com/civetweb/civetweb/blob/master/docs/UserManual.md">Civetweb user manual</a>

More information about tuning the Ceph RGW is currently part of our ongoing work with ATLAS.  Please have a look at the <a href="/domains.html">ATLAS science domain</a> to see what we have learned so far from ATLAS Event Service test jobs.
