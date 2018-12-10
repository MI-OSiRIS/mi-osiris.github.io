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

We deploy perfSONAR components both within OSiRIS and at our “client”
locations to allow monitoring and measuring the networks interconnecting science
domain users and OSiRIS components.  Ryu topology discovery and Flange rules are used to dynamically manage network pathing.  At this point we are still in the experimental stages of network dynamic network management but have working proof of concept services and have also collaborated with the <a href="http://slateci.io/">SLATE project</a> to deploy and test our components in their infrastructure.  

Dockerized deployments of UNIS, Flange, Ryu topology discovery are available on <a href="https://hub.docker.com/u/miosiris/">Docker Hub</a>.  

### Example application

<div class="lf imgwrap" style="width: 50%">
Ryu Network topology information 
<a href="{{IMAGE_PATH}}/nmal/TopologyViewDetail.png">
    <img style="width: 100%" src="{{IMAGE_PATH}}/nmal/TopologyViewDetail.png" alt="Topology information collected by OSiRIS " />
</a>

</div>
Here is a sample of the topology map put together by querying SDN instances on OSiRIS switches and hosts.  This map can be combined with the metrics collected from Periscope and BLiPP to understand network characteristics and make best-path determinations.  
<br style="clear: left"/>


<div class="lf imgwrap" style="width: 50%">
<a href="{{IMAGE_PATH}}/nmal/NetworkPathingRules.png">
    <img style="width: 100%" src="{{IMAGE_PATH}}/nmal/NetworkPathingRules.png" alt="Flange Network pathing visualization" />
</a>
Flange network pathing rules visualized
</div>
We can leverage this topology information in conjunction with performance metrics gathered by Perfsonar-Periscope to generate network pathing rules propogated to our network by Flange.  

<br style="clear:both" />

### Periscope 

Periscope comprises a set of extensions to the standard perfSonar distribution as well as a client monitoring component and data store.  The information collected by periscope components is fed back to the data store component UNIS. 

#### UNIS

The Periscope UNIS data store exposes a RESTful interface for information necessary to perform data logistics.  The data store can hold measurements from BLiPP or network topology inferred through various agents.

<a href="{{IMAGE_PATH}}/nmal/NMAL-Unis.png"><img src="{{IMAGE_PATH}}/nmal/NMAL-Unis.png" alt="UNIS Topology and Measurement Store" style="width: 50%"></a>

#### BLiPP - Basic Lightweight Perfsonar Probe

BLiPP is a flexible framework for collecting host metrics for reporting back to the network information store.  Every OSiRIS node runs a BLiPP agent.  These agents may reside in both the end hosts (monitoring end-to-end network status) and dedicated diagnostic hosts inside networks.  The latter deployment can help isolate section failures of networks.  In our context the perfSonar nodes deployed at each member site and many client/user sites function as diagnostic hosts but the BLiPP agent is also running on our end hosts.  

<a href="{{IMAGE_PATH}}/nmal/NMAL-Blipp-Deployment.png"><img src="{{IMAGE_PATH}}/nmal/NMAL-Blipp-Deployment.png" alt="BLiPP Deployment" style="width: 50%"></a>

### AAA 

Authentication to NMAL components is done using normal signup and shibboleth single sign on.  The 'dlt-web' application generates a pair of keys per users which are signed by its certificate and are made available for download.  

These signed keys can be used by other applications like blipp, ibp-server and ceph for AA with UNIS.

* ABAC (Attibute based access control) is used for authorization in UNIS. 
* UNIS assigns attributes to each principal which in our case is dlt-web and any other trusted principals which are then used to delegate attributes to other users. 
* ABAC is then used in UNIS to decipher appropriate attributes from certificates and provide appropriate authorization to the application.

<a href="{{IMAGE_PATH}}/nmal/NMAL-AAA.png"><img src="{{IMAGE_PATH}}/nmal/NMAL-AAA.png" alt="NMAL AAA Components" style="width: 70%"></a>

### SDN Configuration

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

<a href="{{IMAGE_PATH}}/nmal/OVS_config.jpg"><img src="{{IMAGE_PATH}}/nmal/OVS_config.jpg" alt="Openvswitch Host configuration" style="width:90%"></a>


