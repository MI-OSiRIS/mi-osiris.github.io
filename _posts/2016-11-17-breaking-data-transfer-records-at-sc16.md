---
layout: post
category : article
title: "Breaking Data Transfer Records At SC16"
tagline: "SC16 and SCinet set new 1.2 Terabyte record"
tags : [ sc16, supercomputing, conferences, networking ]
---
{% include JB/setup %}

<div class="imgwrap lf" style="width: 270px">
	<a href="{{IMAGE_PATH}}/sc16/total-showfloor-Thursday.jpg">
		<img src="{{IMAGE_PATH}}/sc16/total-showfloor-Thursday.jpg" alt="Total SCinet traffic monitored by sflow/netflow" style="width: 270px">
	</a>
	SCinet total traffic 
</div>
<a href="http://sc16.supercomputing.org/scinet/">SCinet</a> is a high performance advanced network created every year for the Supercomputing conference.  SCinet comes together thanks to the hard work of volunteers and the support of industry vendors who donate equipment and services.

On the last day of Supercomputing a call went out to 100G booths to push as much traffic as we could across SCinet LAN and WAN links to set a new SC16 bandwidth record.  Of course we had to participate!

To generate traffic we used OSiRIS 100Gb connected hosts at UM, WSU, and MSU as well as 100Gb hosts from ATLAS Great Lakes Tier 2.  

The combined traffic of all participating exhibitors set a new record for pushing over 1.2 Terabybtes of traffic over the show floor and more than 1 Terabit/s across WAN circuits.
<!--excerpt-->
For our part, we saturated the incoming 100Gb link landing on the Dell Z9100 switch in our booth:

<div class="imgwrap" style="width:850px; margin-bottom: 50px">
<a href="{{IMAGE_PATH}}/sc16/SC-WanChallenge-OSiRIS-Switch-Incoming.png"><img src="{{IMAGE_PATH}}/sc16/SC-WanChallenge-OSiRIS-Switch-Incoming.png" style="width:850px" alt="Incoming traffic to OSiRIS switch"></a>
Incoming traffic blackholed on the switch
</div>



While fully utilizing our available outgoing campus bandwidth:

<div class="imgwrap" style="width:850px; margin-bottom: 50px">
<a href="{{IMAGE_PATH}}/sc16/SC-BandwidthChallenge-OSiRIS-Sites-Stacked.png"><img src="{{IMAGE_PATH}}/sc16/SC-BandwidthChallenge-OSiRIS-Sites-Stacked.png" style="width:850px" alt="Traffic Outgoing from OSiRIS sites"></a>
MSU hpcc-atlas bond - 2 x 40 Gb <br />
UM r-MACC* - 40Gb each <br />
WSU MLXe - 10Gb
</div>


<img src="{{IMAGE_PATH}}/sc16/its-signature-vertical.png" alt="UM ITS Logo" class="lf" style="width:150px">
We'd like to thank in particular for this challenge Dan Kirkland and Dan Eklund from the UM ITS team.  Their hard work before and during the conference made sure we had stable, fast network paths to the conference and on the showroom floor.  

<div class="imgwrap" style="width:850px; margin-bottom: 50px; margin-top: 50px">
<a href="{{IMAGE_PATH}}/sc16/SC16 Physical Topology.png"><img src="{{IMAGE_PATH}}/sc16/SC16 Physical Topology.png" style="width: 850px" alt="SC16 Physical Topology"></a>
OSiRIS SC16 Physical Topology 
</div>

Thanks also to Zayo and CenturyLink for providing 100Gb network paths from Michigan to the conference.

<a href="http://www.centurylink.com"><img style="width: 350px; padding-right: 50px" src="{{IMAGE_PATH}}/sc16/CenturyLink_2010_logo.svg.png" alt="CenturyLink Logo"></a>
<a href="http://www.zayo.com"><img style="width:200px" src="{{IMAGE_PATH}}/sc16/large_Zayo.png" alt="Zayo Logo"></a>

Thanks to Juniper and Adva for providing network equipment.

<a href="http://www.juniper.net"><img style="width: 280px; padding-right: 50px" src="{{IMAGE_PATH}}/sc16/juniper-networks-blue-png.png" alt="Juniper Logo"></a>
<a href="http://www.advaoptical.com"><img style="width: 250px" src="{{IMAGE_PATH}}/sc16/ADVA_Optical_Networking.svg.png" alt="ADVA Logo"></a>

We would also like again to acknowledge the hard-working team that built the <a href="http://sc16.supercomputing.org/scinet/">SCinet infrastructure</a> to support local and wide-area networks at the conference.  

Read more about the record in the <a href="http://sc16.supercomputing.org/2016/11/18/sc16-scinet-set-new-1-2-terabyte-record/">article on the SC16 website</a>. 

