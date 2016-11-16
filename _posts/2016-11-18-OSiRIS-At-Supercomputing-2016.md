---
layout: post
category : article
tags : [ sc16, supercomputing, conferences ]
---
{% include JB/setup %}

[![OSiRIS Equipment at SC]({{IMAGE_PATH}}/sc16/BoothCrates-UM.jpg){: style="width: 240px" class="rf"}]({{IMAGE_PATH}}/sc16/BoothCrates-UM.jpg)

<a href="http://sc16.supercomputing.org"><img src="{{IMAGE_PATH}}/sc16/SC16.4CBlackRedTextOutline.png" alt="SC16 Logo" class="lf" style="width: 340px"></a>

<a href="http://arc.umich.edu/"><img style="width: 200px; padding-top: 20px" src="{{IMAGE_PATH}}/logos/arc-logo.png" alt="UM ARC Logo"></a>

<br clear='left'>

The OSiRIS project was featured in the University of Michigan Advanced Research Computing booth at Supercomputing in Salt Lake City this year.  

For the week of the conference, November 14 - 18, OSiRIS deployed our '4th site' in Salt Lake City at the Salt Palace convention center.

<br clear='all' />
<!--excerpt-->

[![OSiRIS Equipment at SC]({{IMAGE_PATH}}/sc16/BoothCrates-MSU.jpg){: style="width: 240px" class="rf"}]({{IMAGE_PATH}}/sc16/BoothCrates-MSU.jpg)

We went to Supercomputing with these goals in mind:

* Demonstrate our ability to quickly deploy additional OSiRIS sites.  At our booth we presented a talk including a live demonstration of spinning up a new storage block (<a href="{{ASSET_PATH}}/slides/SC16-Booth-Talk.pdf">download slides</a>).

{% comment %} article in progress (<a href="{% ds_post_url 2016-11-15-Provisioning-OSiRIS-At-SC16 %}">article</a>).  {% endcomment %}

* Demonstrate and test the usability of OSiRIS with a higher latency site involved.

* Test and gather data on using Ceph cache tiers to help overcome latency issues.  This test features LIQID NVMe drives installed in a pair of 100Gb capable hosts in our rack at SC. 
{% comment %} (<a href="{% post_url 2016-11-16-Ceph-Cache-Tiering-With-LIQID-NVMe-At-SC16 %}">article</a>). {% endcomment %}
* Demonstrate live data movement with the Data Logistics Toolkit created at Indiana University.  This demo showcased the movement of USGS earthsat data from capture to storage not only in the main OSiRIS Ceph cluster but also a dynamic OSiRIS Ceph cluster deployment built at Cloudlab.
{% comment %}  (<a href="{% post_url 2016-11-16-Moving-USGS-Data-With-DLT-And-OSiRIS-At-SC16 %}">article</a>). {% endcomment %}

At the 'CEPH in HPC Environments' BOF we were invited to give a brief overview of the project.  Slides from that talk are available here on <a href="{{ASSET_PATH}}/slides/SC16-Ceph-BOF.pdf">our website</a> as well as posted here on the <a href="https://www.msi.umn.edu/sc16Ceph">BOF overview</a>.  You may also be interested in talks from <a href="https://www.msi.umn.edu/sc15Ceph">last year's BOF</a> though OSiRIS did not yet exist to attend.  

To cap off the conference we participated in breaking the SCinet record for most data transferred via the SC16 network links (<a href="http://sc16.supercomputing.org/2016/11/18/sc16-scinet-set-new-1-2-terabyte-record">article on SC16 site</a>)
{% comment %} article in progress  (<a href="{% post_url 2016-11-17-Breaking-Data-Transfer-Records-At-SC16 %}">article</a>) {% endcomment %}

<hr> 

<img src="{{IMAGE_PATH}}/sc16/its-signature-vertical.png" alt="UM ITS Logo" class="lf" style="width:150px">
None of this would have been possible without the support of Dan Kirkland and Dan Eklund from the UM ITS team.  Their hard work before and during the conference made sure we had stable, fast network paths to the conference and on the showroom floor.    

<br clear='left' />

Special thanks to Bob Ball, Victor Yang, and Anthony Orians from UM Physics/AGLT2 for assistance with equipment preparation before and after the conference. 

Thanks to Zayo and CenturyLink for providing 100Gb network paths from Michigan to the conference.

<a href="http://www.centurylink.com"><img style="width: 350px; padding-right: 50px" src="{{IMAGE_PATH}}/sc16/CenturyLink_2010_logo.svg.png" alt="CenturyLink Logo"></a>
<a href="http://www.zayo.com"><img style="width:200px" src="{{IMAGE_PATH}}/sc16/large_Zayo.png" alt="Zayo Logo"></a>

Thanks to Juniper and Adva for providing network equipment.

<a href="http://www.juniper.net"><img style="width: 280px; padding-right: 50px" src="{{IMAGE_PATH}}/sc16/juniper-networks-blue-png.png" alt="Juniper Logo"></a>
<a href="http://www.advaoptical.com"><img style="width: 250px" src="{{IMAGE_PATH}}/sc16/ADVA_Optical_Networking.svg.png" alt="ADVA Logo"></a>

We would also like to acknowledge the hard-working team that built the <a href="http://sc16.supercomputing.org/scinet/">SCinet infrastructure</a> to support local and wide-area networks at the conference.  

 




