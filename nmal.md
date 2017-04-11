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
Unified Network Information Service (UNIS), and incorporate Software Defined Networking (SDN) into overall operations of the OSiRIS infrastructure.

We plan to deploy and maintain perfSONAR components (both within OSiRIS and at our “client”
locations) to allow monitoring and measuring the networks interconnecting science
domain users and OSiRIS components, and providing input to the Network Fault
Localization Service (NFLS) and the Network Orchestration Service (NOS).


### SDN

Deployed at each site is an SDN controller which is linked to the OSiRIS switch at that site (Dell Z9100).  They are centrally managed by a core SDN controller fed information from the UNIS data store.  

The configuration to enable this is fairly simple.  An openflow instance is required, and vlans on the switch must be configured to be part of that instance.  In the absence of any openflow configuration from the controller the VLANs continue to behave as normal.  

<pre>
openflow of-instance 1
 controller 1 10.10.1.1 port 1234 tcp
 interface-type vlan
 multiple-fwd-table enable
 of-version 1.3
 no shutdown
</pre>

Vlans are configured as normal but must be defined as part of the openflow instance.  They have to be re-defined if already configured, they cannot be switched after.

<pre>
interface vlan 1234 of-instance 1
</pre>

All of our hardware hosts with some multiple of 25Gb NICs are configured with Openvswitch for the core networking so they also can be controlled by openflow.  Generally the 25Gb interfaces are combined into an OVS bond and ports are configured on the OVS for host networking.  Virtualization hosts have libvirt networks configured to utilize the vswitch for VM networking.  

<a href="{{IMAGE_PATH}}/HostOvsBlock.png"><img src="{{IMAGE_PATH}}/HostOvsBlock.png" alt="Openvswitch Host configuration" style="width:90%"></a>


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




