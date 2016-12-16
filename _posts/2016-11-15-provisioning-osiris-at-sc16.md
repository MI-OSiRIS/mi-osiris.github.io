---
layout: post
category : article
title: Provisioning an OSiRIS Site at SC16
tags : [ sc16, supercomputing, conferences ]
---
{% include JB/setup %}

<div id="sitemap_excerpt" class="lf imgwrap" style="width:45%">
<a href="{{IMAGE_PATH}}/sc16/SC16SiteMap.png"><img src="{{IMAGE_PATH}}/sc16/SC16SiteMap.png" alt="OSiRIS Sites during SC16" class="lf" style="width: 100%"></a>
</div>

One of our major goals at the SC16 conference was demonstrating our ability to quickly deploy additional OSiRIS sites and operate successfully across higher latency wide area networks.  

For the week of the conference, November 14 - 18, OSiRIS deployed a 4th storage site in Salt Lake City at the Salt Palace convention center.  In doing so we showcased the processes we use to build and manage new sites.  

<!--excerpt-->

<div class="imgwrap" style="width:100%">
<a href="{{IMAGE_PATH}}/sc16/SC16SiteMap.png"><img src="{{IMAGE_PATH}}/sc16/SC16SiteMap.png" alt="OSiRIS Sites during SC16" class="" style="width: 100%"></a>
</div>


<script type='text/javascript'>
var element = document.getElementById("sitemap_excerpt");
element.parentNode.removeChild(element);
</script>

At our booth we presented a talk detailing the process of deploying a new site and including a live demonstration of spinning up a new storage block (<a href="{{ASSET_PATH}}/slides/SC16-Booth-Talk.pdf">download slides</a>).

A typical OSiRIS site, including the SC16 site, includes Ceph storage components (OSD) and service components for Ceph and site monitoring.  For SC we deployed 3 storage nodes for a total of 76 OSD.  Of those, 16 were fast LIQID NVMe devices on a pair of hosts purchased from 2CRSI {% comment %} (<a href="{% post_url 2016-11-16-ceph-cache-tiering-with-liqid-nvme-at-sc16 %}">read our article on Ceph cache tiering</a>){% endcomment %}.

<div class="imgwrap" style="width:100%">
<a href="{{IMAGE_PATH}}/sc16/SC16-OSiRIS-TypicalSite.png"><img src="{{IMAGE_PATH}}/sc16/SC16-OSiRIS-TypicalSite.png" alt="Typical OSiRIS site" class="" style="width: 100%"></a>
</div>

To provision a new site all we need to start is a simple Foreman 'smart-proxy' host.  We provide this host as a small VM template to be deployed on the virtualization host that OSiRIS sites start with.  We have documented manual procedures to deploy the VM host or we can provide an install image for new sites to easily get started.  

<div class="imgwrap" style="width:100%">
<a href="{{IMAGE_PATH}}/sc16/DeploymentOverview.png"><img src="{{IMAGE_PATH}}/sc16/DeploymentOverview.png" alt="OSiRIS Provisioning Overview" class="" style="width: 100%"></a>
</div>

To coordinate and quickly configure new hosts we use Puppet configuration management in combination with r10k and a central git repository (currently a private Github repository).
R10k maps git branches to puppet environments and automatically manages syncing up external puppet modules in deployed environments.  Our admins can test and develop in independent environments and filter pull requests through coordinating admins for review.  

<div class="imgwrap" style="width:100%">
<a href="{{IMAGE_PATH}}/sc16/ManagementOverview.png"><img src="{{IMAGE_PATH}}/sc16/ManagementOverview.png" alt="OSiRIS Puppet Management Overview" class="" style="width: 100%"></a>
</div>

Our project is multi-institutional with sites and hosts that may have any number of inconsistencies.  Puppet's hiera integration is a good map to our situation.  To deploy the SC16 site we simply created a new hiera node with site-specific information, and as needed also over-rode definitions at the node level.  We name all of our hosts with a specific pattern that puppet can parse and convert into hiera lookups by site and node type.  

<div class="imgwrap" style="width:100%">
<a href="{{IMAGE_PATH}}/sc16/PuppetOrganizationOverview.png"><img src="{{IMAGE_PATH}}/sc16/PuppetOrganizationOverview.png" alt="OSiRIS Puppet and Hiera Organization example" class="" style="width: 100%"></a>
</div>

Overall we consider the deployment at SC16 to be a success.  As expected the overall data transfer speeds are slowed by the latency between ceph OSD nodes but everything functioned well.  During SC16 we demonstrated initializing a new storage block with 60 OSD several times during our booth talks.  Recovery and data-peeering operations to the node carried on without a hitch even as our <a href="{% post_url 2016-11-16-moving-usgs-data-with-dlt-and-osiris-at-sc16 %}">DLT demo</a> from IU was ongoing.

<div class="imgwrap" style="width:100%">
<a href="{{IMAGE_PATH}}/sc16/Grafana-SCTalk-11-15-AddOsd.png"><img src="{{IMAGE_PATH}}/sc16/Grafana-SCTalk-11-15-AddOsd.png" alt="Adding OSD during SC booth talk" class="" style="width: 100%"></a>
</div>