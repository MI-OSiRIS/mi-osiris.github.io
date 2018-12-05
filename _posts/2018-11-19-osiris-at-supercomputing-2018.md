---
layout: post
category : article
redirect_from: 
 - /article/2018/11/10/osiris-at-supercomputing-2018
title: OSiRIS At Supercomputing 2018
tags : [ sc18, supercomputing, conferences ]
---
{% include JB/setup %}



<div class="imgwrap lf" style="width: 20%">
<a href="https://sc18.supercomputing.org/">
    <img style="width: 100%" class="lf" src="{{IMAGE_PATH}}/sc18/SC18-color-ver-highlights.png" alt="SC18 Logo" />
</a>
</div>

The International Conference for High Performance Computing, Networking, Storage, and Analysis <br />
November 11–16, 2018 <br />
Kay Bailey Hutchison Convention Center, Dallas, Texas

<div class="imgwrap rf" style="width: 30%">
<a href="https://arc.umich.edu/">
    <img style="width: 100%" src="{{IMAGE_PATH}}/logos/arc_logo_square.png" alt="SC18 Logo" />
</a>
</div>

Members of the OSiRIS team traveled to SC18 to setup in the University of Michigan and Michigan State University combined booth!  

We setup up a rack of equipment designated for use by OSiRIS, <a href="http://slateci.io/">SLATE</a>, and <a href="https://www.aglt2.org/">AGLT2</a> demos at SC.  The rack was shipped as a unit from Michigan and was waiting for us to plug it in and set up when we got to the conference.  


<br style="clear:both" />

<div class="imgwrap lf" style="width: 30%">
<a href="{{IMAGE_PATH}}/sc18/showfloor-booth-both-1.jpg">
    <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/showfloor-booth-both-1.jpg" alt="Combined Booth" />
</a>
Combined MSU / UM Booth
</div>

<div class="imgwrap lf" style="width: 30%">
<a href="{{IMAGE_PATH}}/sc18/osiris-booth-activity.jpg">
    <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/osiris-booth-activity.jpg" alt="Demo Equipment and Posters" />
</a>
Demo Equipment and Posters
</div>

<div class="imgwrap lf"  style="width: 30%">
<a href="{{IMAGE_PATH}}/sc18/crate-posters-closeup.jpg">
    <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/crate-posters-closeup.jpg" alt="Science domain posters" />
</a>
Science domain highlight posters
</div>

<br style="clear:both" />

<!--excerpt-->

Our demonstration encompassed our storage features, advanced networking, identity management/onboarding, and included a collaboration with <a href="http://slateci.io/">SLATE infrastructure</a> utilizing OSiRIS storage.

 <div class="imgwrap" style="width: 70%">
        <a href="{{IMAGE_PATH}}/sc18/OSiRIS-SC18-OverviewDiagram.jpg">
            <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/OSiRIS-SC18-OverviewDiagram.jpg" alt="Conceptual diagram for OSiRIS SC18" />
        </a>
        </div>
<ul class="bolditem">
    <li> 
        <p>
        <span><a href="{% post_url 2018-11-15-ceph-cache-tiering-demo-at-sc18 %}">Storage Features - caching</a>:</span> Typical Ceph storage clusters are heavily affected by network latency between components and clients.  As such a client accessing OSiRIS storage in Michigan from the SC showroom would not see similar performance to our more proximate users.  OSiRIS will deploy dedicated storage hardware for a Ceph cache-tier at SC18 to show that it is possible to achieve reasonable performance even though the backing data pool components are geographically quite far away.   The SC18 collaboration with SLATE also leveraged this configuration as a 50TB RBD for their XCache container. 
        </p>
    </li>
    <li>
    <p>
     <span>Storage Features - primary OSD:</span> Taking another angle on optimizing around network latency, we also experimented with setting primary OSD at SC18 for certain storage pools.  Our tests compare the benefits and drawbacks of this approach for clients with low latency to the primary OSD vs those farther away and also compare to the 'default' Ceph setting of randomly allocated primary OSD.  
    </p> 
    </li>
    <li>
        <p>
        <span>Advanced Networking:</span>  The OSiRIS Network Management Abstraction Layer (NMAL) seeks to orchestrate network pathing and quality of service based on real-time feedback.  At SC18 we demonstrated the impact of these intelligent network capabilities on the client experience.
    </p>
    </li>
    <li>    
        <p>
        <span>Identity Management and SC18 Test Sandbox:</span>  OSiRIS virtual organizations and the people within those organizations are managed by Internet2 COmanage and a collection of plugins we’ve written to tie together with Ceph storage.  For SC18 we spawned a virtual organization for the show to demonstrate self-service onboarding and credential management.  We then made this <a href="/sc18">storage sandbox</a> available to SCInet clients on the show floor via NFS mount or RGW services.  Our provisioning infrastructure was also involved in the collaboration with SLATE as far as being used to provision storage resources for their virtual organization as we would for any dedicated VO.  
    </p>
    </li>
    <li>
        <p>
            <span>SLATE Collaboration:</span> <a href="http://slateci.io/">SLATE</a> (Services Layer At The Edge) aims to provide a platform for deploying scientific services across national and international infrastructures.  At SC18 they demonstrated their containerized Xcache service using storage (RBD) hosted by OSiRIS using our Ceph cache tier at SC18.  
        </p>
    </li>
</ul>   

<hr> 

Thanks to everyone on the OSiRIS team at University of Michigan, Wayne State University, Indiana University, and Michigan State University for helping to make the conference a great success!

<a href="https://its.umich.edu/infrastructure"><img src="{{IMAGE_PATH}}/sc18/its-signature-vertical.png" alt="UM ITS Logo" class="lf" style="width:20%"></a>
We appreciate the support of Nick Grundler and Dan Eklund from the UM ITS team.  Their hard work before and during the conference made sure we had stable, fast network paths to the conference and on the showroom floor.    

<br style="clear: both;" />

<a href="http://www.aglt2.org"><img src="{{IMAGE_PATH}}/logos/aglt2_logo.png" alt="AGLT2 Logo" class="lf" style="margin-top: 10px; width:11%"></a>
Special thanks to Wenjing Wu and Troy Morgan from UM Physics/AGLT2 for assistance with equipment preparation before and after the conference. 

<br style="clear: both;" />

Thanks to Merit Networks and Internet2 for assistance providing 100Gb network paths from Michigan to the conference.

<a href="https://www.merit.edu/"><img style="width: 23%" src="{{IMAGE_PATH}}/sc18/merit_logo.png" alt="Merit Logo"></a>
<a href="https://www.internet2.edu"><img style="width: 23%" src="{{IMAGE_PATH}}/sc18/internet2_logo.gif" alt="Internet2 Logo"></a>
<br style="clear: both;" />
Thanks to Juniper and Adva for providing network equipment.

<a href="http://www.juniper.net"><img style="width: 30%; padding-right: 50px" src="{{IMAGE_PATH}}/sc18/juniper-networks-blue-png.png" alt="Juniper Logo"></a>
<a href="http://www.advaoptical.com"><img style="width: 25%" src="{{IMAGE_PATH}}/sc18/ADVA_Optical_Networking.svg.png" alt="ADVA Logo"></a>

<br style="clear: both;" />
We would also like to acknowledge the hard-working team that built the <a href="https://sc18.supercomputing.org/experience/scinet/">SCinet infrastructure</a> to support local and wide-area networks at the conference.  

