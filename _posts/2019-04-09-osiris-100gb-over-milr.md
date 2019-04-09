---
layout: post
category : article
title: OSiRIS upgrades to 100Gb over Michigan LambdaRail 
tagline: 
tags : [ network, milr ]
---
{% include JB/setup %}

<img class="lf" style="padding: 5px; background: white;" src="{{IMAGE_PATH}}/logos/milr-logo.jpg" alt="MiLR Logo" />

Working closely with network teams at Wayne State University, Michigan State University, University of Michigan and Merit, OSiRIS has recently linked our sites via 100Gbit across the Michigan LambdaRail (MiLR) fiber loop.  Completion of this work marks a major milestone in the OSiRIS planning roadmap and we look forward to leveraging this new capability for enabling science!

<!--excerpt-->

Our new links land directly on OSiRIS switches so we have more options to implement <a href="/nmal">network management</a> services than we might have when uplinking our switches via campus/DMZ networks.    

Previously OSiRIS had inter-site links ranging from 10-80Gbps.  With consistent 100Gb connectivity we avoid bottlenecks that required <a href="/components/ceph/">tuning Ceph</a> to avoid saturating our smallest link.  Multiple links also give us more options for routing traffic in the most efficient manner.  

The project owes great thanks to our campus networking teams for coordinating together on this update.  We couldn't do it without their support!

<a href="https://tech.msu.edu/network/network-systems/"><img class="lf" style="width: 20%" src="{{IMAGE_PATH}}/logos/msu_logo_square.png" alt="MSU logo"></a>

<a href="https://tech.wayne.edu"><img class="lf" style="width: 37%;" src="{{IMAGE_PATH}}/logos/wsu_cit_stacked.jpg" alt="WSU CIT Logo"></a>

<a href="https://its.umich.edu/infrastructure"><img src="{{IMAGE_PATH}}/logos/its-signature-vertical.png" alt="UM ITS Logo" style="width: 25%"></a>


<br style="clear: both;"/>

<h3>Other Resources</h3>

MiLR is a high-speed, special purpose, data network built jointly by Michigan State University, the University of Michigan, and Wayne State University, and operated by the Merit Network.  

You can find more information about MiLR and other research connections on the <a href="https://its.umich.edu/enterprise/wifi-networks/researchers/milr">U-M ITS website</a>.

The <a href="http://www.milr.org/">MiLR website</a> has not been updated for a while but contains some historical information.  

OSiRIS provides a distributed, multi-institutional storage infrastructure based on Ceph that lets researchers write, manage, and share data from their own computing facility locations. Our goal is transparent, high-performance access to the same storage infrastructure from well-connected locations on any participating campus.  
