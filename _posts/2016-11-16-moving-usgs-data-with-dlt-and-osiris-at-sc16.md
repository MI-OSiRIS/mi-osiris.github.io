---
layout: post
category : article
title: Moving USGS Data With DLT And OSiRIS At SC16
tagline: Rapid Distribution of Earth Science Data with the Earth Observation Depot Network and the Data Logistics Toolkit
tags : [ sc16, supercomputing, conferences, dlt ]
---
{% include JB/setup %}

<div id="dltviz_excerpt" class="rf imgwrap" style="width:300px">
<a href="{{IMAGE_PATH}}/sc16/dlt_dlviz.gif"><img src="{{IMAGE_PATH}}/sc16/dlt_dlviz.gif" alt="DLT Data Movement Visualization" class="lf" style="width: 300px"></a>
</div>

The NSF-funded Data Logistics Toolkit (DLT) project was featured in the Indiana University and the University of Michigan Advanced Research Computing booths at Supercomputing in Salt Lake City this year.  

As an instantiation of the DLT, the Earth Observation Depot Network (EODN) aims to enable open access, reduced latency, and fast downloads for valuable and compelling Earth Science data from satellites for meteorological and atmospheric researchers.  Data sources include remote sensing data from NASA’s Earth Science Program (EOS-DIS) and the United States Geological Survey (USGS) Landsat ground network and are made available within EODN via a “harvester” workflow maintained at IU.

<!--excerpt-->

<script type='text/javascript'>
var element = document.getElementById("dltviz_excerpt");
element.parentNode.removeChild(element);
</script>

<div class="imgwrap" style="width:800px; margin-bottom: 20px">
<a href="{{IMAGE_PATH}}/sc16/dlt_dlviz.gif"><img src="{{IMAGE_PATH}}/sc16/dlt_dlviz.gif" alt="DLT Data Movement Visualization" style="width: 800px"></a>
<font>Data from NASA’s Earth Science Program (EOS-DIS) and the United States Geological Survey (USGS) Landsat ground network transferring from OSiRIS and Cloudlab using DLT</font>
</div>

Initially deployed on GENI infrastructure, EODN has been extended to operate on the OSiRIS open storage infrastructure using Ceph technology.  In addition, we made use of resources at Utah’s CloudLab to show the viability of a cloud-based storage cluster that may be instantiated during periods of high demand.  Our demonstration at Supercomputing highlighted this interoperability and evaluated the performance of large-scale Landsat data transfers between Michigan, Indiana, and Salt Lake City storage sites.

<div class="imgwrap" style="width:800px; margin-bottom: 20px">
<a href="{{IMAGE_PATH}}/sc16/sc16_osiris_wm.png"><img src="{{IMAGE_PATH}}/sc16/sc16_osiris_wm.png" alt="SC16 network weather map" style="width: 800px"></a>
Weathermap of DLT network data transfers between OSiRIS sites at Michigan, SC16, and separate cluster at Cloudlab.
</div>

The Supercomputing network infrastructure provided a valuable testbed to further research and development on a number of DLT and OSiRIS components:

* libdlt – DLT filesystem middleware.   Includes an object store abstraction for the interchangeable use of underlying data movement routines.

* IDMS – The Intelligent Data Movement Service enforces global and user-specific data distribution policies and governs the storage nodes between which data is transferred.

* UNIS-RT and Flange – The runtime for the Unified Network Information Service (UNIS).  Flange directly uses the runtime to operate programmatically on a UNIS topology representation (network graph) for dynamic updates and control.

* Periscope – Measurement collection/analysis framework.

More information on DLT and EODN may be found at <a href="http://data-logistics.org">data-logistics.org</a>
