---
layout: default
title : Science Domains
header : Science Domains
group: navigation
order: 3
---
{% include JB/setup %}


### ATLAS

Our project has started engaging with the ATLAS experiment to serve as a store of ATLAS physics events for compute jobs.  

ATLAS compute jobs will use the OSiRIS Ceph S3 gateway to read/write single events.  By reading only a single event at a time ATLAS can leverage transient computing resources to run short jobs as available.

<div class="imgwrap">
<a href="{{IMAGE_PATH}}/ATLAS-Object-Gateway.png">
	<img src="{{IMAGE_PATH}}/ATLAS-Object-Gateway.png" style="width: 100%">
</a>
	ATLAS and OSiRIS S3 Gateways
</div>


OSiRIS and ATLAS have been engaged in load-testing our S3 gateways with large numbers of connections from nodes at ANL and BNL.  Initially, with no tuning of any Ceph configuration, our limit was 16,000 client connections and 40 requests/second across our 3 gateway nodes (1 at each of UM, WSU, MSU).  At higher rates the S3 service started to issue 403 denied errors with the following log:

<pre>
2017-02-09 08:53:16.915536 7f8c667bc700 0 NOTICE: request time skew too big now=2017-02-09 08:53:16.000000 req_time=2017-02-09
08:37:18.000000
</pre>


In addition we would see TCP connection refused errors.  We reached out to the ceph-users list for some guidance and received a few tuning suggestions.  By adjusting the following Ceph parameters we were able to reach much higher rates with 58,000 client connections and 150 requests/second.  This is just the start though - we still are not reaching any limitations of the hardware.  

<pre>
 [client.radosgw]
  # default num_threads is 50
  rgw_frontends = civetweb port=xxx num_threads=400 ssl_certificate=/path/to/cert
  rgw_thread_pool_size = 800  # default is 100
  rgw_num_rados_handles = 8   # default is 1
</pre>

Though we increased the civetweb num_threads setting it does not appear that this made any significant difference in capability.  As we tested and changed settings we monitored requests / second.  The data below is gathered from the collectd-ceph plugin which reads it from the Ceph daemon admin socket (/var/run/ceph/ceph-client.id.asok).  The plugin then forwards it to Influxdb and we can plot with <a href="components/monitoring.html">Grafana</a>.    

<div class="imgwrap">
<a href="{{IMAGE_PATH}}/RGW-ATLAS-Tuning-2-9-to-2-10.png">
	<img src="{{IMAGE_PATH}}/RGW-ATLAS-Tuning-2-9-to-2-10.png" style="width: 100%">
</a>
Plot of our S3 gateway requests / second during load testing and tuning (<a href="{{IMAGE_PATH}}/RGW-ATLAS-Tuning-2-9-to-2-10.png ">larger view</a>)
</div>

There is still more tuning to reach the maximum potential of the hardware hosting the S3 gateway.  Using the same test setup that was used to generate representative traffic from ANL and BNL we plan to leverage the <a href="http://arc-ts.umich.edu/systems-and-services/flux/">UM Flux cluster at ARC-TS</a> to generate high connection loads to a single OSiRIS S3 gateway and tune with a shorter test/feedback loop to maximize our throughput for ATLAS loads.  


### Oceanic Modeling

The Naval Research Lab is collaborating with researchers at UM to share their high-resolution ocean models with the broader community. This data is not classified but was stored on Navy computers that were not easily accessible to many researchers. 

 We're currently storing this data in OSiRIS in a CephFS pool replicated at all three sites and accessible via our transfer gateways (Globus, FDT, SCP).  Users from Karlsruhe Institute of Technology in Germany and University of Washington in the US are collaborating on the data so far.  

### Timeline for future science domain engagement

* Year 1: High-energy Physics, High-resolution Ocean Modeling (**now ongoing**)
* Year 2: Biosocial Methods and Population Studies,  Aquatic Bio-Geochemistry
* Year 3: Neurodegenerative Disease Studies
* Year 4: Statistical Genetics, Genomics and Bioinformatics
* Year 5: Remaining participants, New Science Domains
