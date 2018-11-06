---
layout: default
title : OSiRIS and ATLAS Event Service
header: OSiRIS and ATLAS
---
{% include JB/setup %}

The ATLAS experiment uses OSiRIS to serve as a store of ATLAS physics events for compute jobs.  We're one of several sites providing "Event Service" capabilities to ATLAS jobs

ATLAS Event Service compute jobs use OSiRIS Ceph S3 gateway to read/write single events.  By reading only a single event at a time ATLAS can leverage transient computing resources to run short jobs as available.

<div class="imgwrap">
<a href="{{IMAGE_PATH}}/ATLAS-Object-Gateway.png">
    <img src="{{IMAGE_PATH}}/ATLAS-Object-Gateway.png" style="width: 100%">
</a>
    ATLAS and OSiRIS S3 Gateways
</div>

OSiRIS has been operating as a regular ATLAS event service site since October 2017.  Pictured below is an excerpt from October 2018 showing events processed by the AGLT2 site which uses the OSiRIS ES as storage endpoint.  

<div class="imgwrap" style="width: 80%">
<a href="{{IMAGE_PATH}}/domains/ATLAS-ES-OSiRIS-Events.png">
    <img src="{{IMAGE_PATH}}/domains/ATLAS-ES-OSiRIS-Events.png" style="width: 100%">
</a>
    ATLAS ES Plot for AGLT2 / OSiRIS
</div>



