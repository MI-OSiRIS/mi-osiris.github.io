---
layout: default
title : Science Domains
header : Science Domains
group: navigation
---
{% include JB/setup %}


### ATLAS

Our project has started engaging with the ATLAS experiment to serve as a store of ATLAS physics events for compute jobs.  

ATLAS compute jobs will use the OSiRIS Ceph S3 gateway to read/write single events.  By reading only a single event at a time ATLAS can leverage transient computing resources to run short jobs as available.

Below is a plot of our S3 gateway statistics during a run of ATLAS event test code.

[![Cluster Dashboard]({{IMAGE_PATH}}/ATLAS-Test-RGW-Dash.png){: style="width: 100%"}]({{IMAGE_PATH}}/ATLAS-Test-RGW-Dash.png)

### Oceanic Modeling

The Naval Research Lab is collaborating with researchers at UM to share their high-resolution ocean models with the broader community.

This data is not classified but is stored on Navy computers that are not easily accessible to many researchers.

Discussions are underway to determine a suitable interface and transfer method to put this data into OSiRIS for wider use.

We are also exploring S3/RGW with objects mapped to a URL to provide high-level organization of the objects (e.g., the URL defines the type/location of the object data)


### Timeline for future science domain engagement

* Year 1: High-energy Physics, High-resolution Ocean Modeling (**now ongoing**)
* Year 2: Biosocial Methods and Population Studies,  Aquatic Bio-Geochemistry
* Year 3: Neurodegenerative Disease Studies
* Year 4: Statistical Genetics, Genomics and Bioinformatics
* Year 5: Remaining participants, New Science Domains
