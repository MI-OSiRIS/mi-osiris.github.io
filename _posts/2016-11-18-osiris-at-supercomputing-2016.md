---
layout: post
category : article
title: "OSiRIS At Supercomputing 2016"
redirect_from: 
 - /article/2016/11/18/OSiRIS-At-Supercomputing-2016
tags : [ sc16, supercomputing, conferences ]
---
{% include JB/setup %}
<div class="rf imgwrap" style="width:240px">
<a href="{{IMAGE_PATH}}/sc16/BoothCrates-UM.jpg"><img style="width: 240px"  src="{{IMAGE_PATH}}/sc16/BoothCrates-UM.jpg" alt="OSiRIS Equipment at SC"></a>
<a href="{{IMAGE_PATH}}/sc16/Osiris-sign-1.pdf">sign text</a>
</div>

<a href="http://sc16.supercomputing.org"><img src="{{IMAGE_PATH}}/sc16/SC16.4CBlackRedTextOutline.png" alt="SC16 Logo" class="lf" style="width: 340px"></a>

<a href="http://arc.umich.edu/"><img style="width: 200px; padding-top: 20px" src="{{IMAGE_PATH}}/logos/arc-logo.png" alt="UM ARC Logo"></a>

<br clear='left'>

The OSiRIS project was featured in the University of Michigan Advanced Research Computing booth at Supercomputing in Salt Lake City this year.  

For the week of the conference, November 14 - 18, OSiRIS deployed a 4th storage site in Salt Lake City at the Salt Palace convention center.

<br clear='all' />

<!--excerpt-->


<div class="imgwrap" style="width:850px; margin-bottom: 20px; margin-top: 20px;" >
<a href="{{IMAGE_PATH}}/sc16/SC16SiteMap.png"><img src="{{IMAGE_PATH}}/sc16/SC16SiteMap.png" alt="OSiRIS Sites during SC16" style="width: 850px"></a>
</div>


<div class="lf imgwrap" style="width:240px">
<a href="{{IMAGE_PATH}}/sc16/BoothCrates-MSU.jpg"><img style="width: 240px" src="{{IMAGE_PATH}}/sc16/BoothCrates-MSU.jpg"></a>
<a href="{{IMAGE_PATH}}/sc16/Osiris-sign-2.pdf">sign text</a>
</div>

We went to Supercomputing with these goals in mind:

* Demonstrate our ability to quickly deploy additional OSiRIS sites.  At our booth we presented a talk including a live demonstration of spinning up a new storage block (<a href="{% post_url 2016-11-15-provisioning-osiris-at-sc16 %}">article</a> and <a href="{{ASSET_PATH}}/slides/SC16-Booth-Talk.pdf">slides</a>).

* Demonstrate and test the usability of OSiRIS with a higher latency site involved (confirming our <a href="/performance/latency">formal test results</a>).

* Test and gather data on using Ceph cache tiers to help overcome latency issues.  This test features LIQID NVMe drives installed in a pair of 100Gb capable hosts in our rack at SC. 
{% comment %} (<a href="{% post_url 2016-11-16-ceph-cache-tiering-with-liqid-nvme-at-sc16 %}">article</a>). {% endcomment %}

* Demonstrate live data movement with the Data Logistics Toolkit created at Indiana University.  This demo showcased the movement of USGS earthsat data from capture to storage not only in the main OSiRIS Ceph cluster but also a dynamic OSiRIS Ceph cluster deployment built at Cloudlab (<a href="{% post_url 2016-11-16-moving-usgs-data-with-dlt-and-osiris-at-sc16 %}">article</a>). 

At the 'CEPH in HPC Environments' BOF we were invited to give a brief overview of the project.  Slides from that talk are available here on <a href="{{ASSET_PATH}}/slides/SC16-Ceph-BOF.pdf">our website</a> as well as posted here on the <a href="https://www.msi.umn.edu/sc16Ceph">BOF overview</a>.  You may also be interested in talks from <a href="https://www.msi.umn.edu/sc15Ceph">last year's BOF</a> though OSiRIS did not yet exist to attend.  

To cap off the conference we participated in breaking the SCinet record for most data transferred via the SC16 network links (<a href="{% post_url 2016-11-17-breaking-data-transfer-records-at-sc16 %}">article</a>) 

<hr> 

<img src="{{IMAGE_PATH}}/sc16/its-signature-vertical.png" alt="UM ITS Logo" class="lf" style="width:150px">
We appreciate the support of Dan Kirkland and Dan Eklund from the UM ITS team.  Their hard work before and during the conference made sure we had stable, fast network paths to the conference and on the showroom floor.    

<br clear='left' />

Special thanks to Bob Ball, Victor Yang, and Anthony Orians from UM Physics/AGLT2 for assistance with equipment preparation before and after the conference. 

Thanks to Zayo and CenturyLink for providing 100Gb network paths from Michigan to the conference.

<a href="http://www.centurylink.com"><img style="width: 350px; padding-right: 50px" src="{{IMAGE_PATH}}/sc16/CenturyLink_2010_logo.svg.png" alt="CenturyLink Logo"></a>
<a href="http://www.zayo.com"><img style="width:200px" src="{{IMAGE_PATH}}/sc16/large_Zayo.png" alt="Zayo Logo"></a>

Thanks to Juniper and Adva for providing network equipment.

<a href="http://www.juniper.net"><img style="width: 280px; padding-right: 50px" src="{{IMAGE_PATH}}/sc16/juniper-networks-blue-png.png" alt="Juniper Logo"></a>
<a href="http://www.advaoptical.com"><img style="width: 250px" src="{{IMAGE_PATH}}/sc16/ADVA_Optical_Networking.svg.png" alt="ADVA Logo"></a>

We would also like to acknowledge the hard-working team that built the <a href="http://sc16.supercomputing.org/scinet/">SCinet infrastructure</a> to support local and wide-area networks at the conference.  

 




