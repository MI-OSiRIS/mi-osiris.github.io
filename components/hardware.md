---
layout: default
title : Hardware
header : OSiRIS Hardware Components
group: components
subnavgroup: components
---
{% include JB/setup %}
[![Hardware Overview]({{IMAGE_PATH}}/MI-OSiRIS-CephStorage.png){: style="width: 100%"}]({{IMAGE_PATH}}/MI-OSiRIS-CephStorage.png)
<br />

## Hardware Provisioning

The project leverages Libvirt for VM hosting, Foreman for provisioning, and Puppet for configuration management.  Foreman's smart-proxy architecture simplifies provisioning from a single master to sites on different networks.  Most of our VMs are provisioned by the libvirt foreman plugin except for the initial instance where we installed Foreman/Puppet using the Foreman installer tool.  New libvirt hypervisors are configured by puppet to allow our Foreman host to access them though it is required to manually configure the new compute resources in Foreman to use them.

As seen in the architecture overview below we use Git to coordinate configuration work between all the engineers in the project and the 'r10k' tool to deploy to our puppetmaster.  If necessary we can scale our puppet installation out to have masters at each site.  For the time being a single master is sufficient.  Not shown in the diagram are the Foreman smart-proxy instances at other sites which would handle serving dhcp, tftp, and provisioning templates.  These instances are spawned from VM templates and configured by puppet.  The only requirement to spin a new one up is to set the provisioning networks properly in puppet hiera data for the site.  New site smart-proxy instances auto-register to the Foreman master.  

<img src="{{IMAGE_PATH}}/ProvisionBlock.png" alt="OSiRIS Provisioning Setup">
 
<a href="/components/management.html">More information on provisioning and management </a>
