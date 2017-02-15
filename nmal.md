---
layout: default
title : NMAL
header : OSiRIS NMAL
group: navigation
order: 5
---
{% include JB/setup %}

### Summary

The Network Management Abstraction Layer (NMAL) will extend [perfSONAR](http://www.perfsonar.net)
capabilities to include automated network topology discovery and tracking in the
Unified Network Information Service (UNIS), and incorporate that into overall operations of the OSiRIS infrastructure.

We plan to deploy and maintain perfSONAR components (both within OSiRIS and at our “client”
locations) to allow monitoring and measuring the networks interconnecting science
domain users and OSiRIS components, and providing input to the Network Fault
Localization Service (NFLS) and the Network Orchestration Service (NOS).

### Periscope 

Periscope comprises a set of extensions to the standard perfSonar distribution as well as a client monitoring component and data store.

#### BLiPP

BLiPP agents may reside in both the end hosts (monitoring end-to-end network status) and dedicated diagnose hosts inside networks. 
The latter deployment can help isolate section failures of networks.

<a href="{{IMAGE_PATH}}/nmal/NMAL-Blipp-Deployment.png"><img src="{{IMAGE_PATH}}/nmal/NMAL-Blipp-Deployment.png" alt="BLiPP Deployment" style="width: 70%"></a>

#### UNIS

The Periscope UNIS data store exposes a RESTful interface for information necessary to perform data logistics.  The data store can hold measurements from BLiPP or network topology inferred through various agents.

<a href="{{IMAGE_PATH}}/nmal/NMAL-Unis.png"><img src="{{IMAGE_PATH}}/nmal/NMAL-Unis.png" alt="UNIS Topology and Measurement Store" style="width: 70%"></a>

### AAA 

Authentication to NMAL components is done using normal signup and shibboleth single sign on.  The 'dlt-web' application generates a pair of keys per users which are signed by its certificate and are made available for download.  

These signed keys can be used by other applications like blipp, ibp-server and ceph for AA with UNIS.

* ABAC (Attibute based access control) is used for authorization in UNIS. 
* UNIS assigns attributes to each principal which in our case is dlt-web and any other trusted principals which are then used to delegate attributes to other users. 
* ABAC is then used in UNIS to decipher appropriate attributes from certificates and provide appropriate authorization to the application.

<a href="{{IMAGE_PATH}}/nmal/NMAL-AAA.png"><img src="{{IMAGE_PATH}}/nmal/NMAL-AAA.png" alt="NMAL AAA Components" style="width: 70%"></a>

### SDN

The larger picture of our SDN infrastructure is still in the planning stages.  Regardless we have started our deployment efforts with an eye towards enabling advanced control of network flows by configuring host networking with Openvswitch.  Below is a diagram of our typical configuration.  This is very likely to evolve over time.  

<a href="{{IMAGE_PATH}}/HostOvsBlock.png"><img src="{{IMAGE_PATH}}/HostOvsBlock.png" alt="Openvswitch Host configuration" style="width:90%"></a>

Under discussion is the use of OpenDaylight or RYU as our SDN controller integrating with NMAL.