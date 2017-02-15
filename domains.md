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

<div class="imgwrap">
<a href="{{IMAGE_PATH}}/ATLAS-Test-RGW-Dash.png">
	<img src="{{IMAGE_PATH}}/ATLAS-Test-RGW-Dash.png" style="width: 100%">
</a>
Plot of our S3 gateway statistics during a run of ATLAS event test code
</div>


### Oceanic Modeling

The Naval Research Lab is collaborating with researchers at UM to share their high-resolution ocean models with the broader community. This data is not classified but was stored on Navy computers that were not easily accessible to many researchers. 

 We're currently storing this data in OSiRIS in a CephFS pool replicated at all three sites and accessible via our transfer gateways (Globus, FDT, SCP).  Users from Karlsruhe Institute of Technology in Germany and University of Washington in the US are collaborating on the data so far.  

### Timeline for future science domain engagement

* Year 1: High-energy Physics, High-resolution Ocean Modeling (**now ongoing**)
* Year 2: Biosocial Methods and Population Studies,  Aquatic Bio-Geochemistry
* Year 3: Neurodegenerative Disease Studies
* Year 4: Statistical Genetics, Genomics and Bioinformatics
* Year 5: Remaining participants, New Science Domains
