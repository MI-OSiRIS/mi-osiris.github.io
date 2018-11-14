---
layout: post
category : article
title: OSiRIS At Supercomputing 2018
tags : [ sc18, supercomputing, conferences ]
---
{% include JB/setup %}



<div class="imgwrap lf" style="width: 20%">
<a href="https://sc18.supercomputing.org/">
    <img style="width: 100%" class="lf" src="{{IMAGE_PATH}}/sc18/SC18-color-ver-highlights.png" alt="SC18 Logo" />
</a>
</div>

The International Conference for High Performance Computing, Networking, Storage, and Analysis
November 11–16, 2018
Kay Bailey Hutchison Convention Center, Dallas, Texas

<div class="imgwrap rf" style="width: 30%">
<a href="https://arc.umich.edu/">
    <img style="width: 100%" src="{{IMAGE_PATH}}/logos/arc_logo_square.png" alt="SC18 Logo" />
</a>
</div>

OSiRIS has finished set up at SC18 in the University of Michigan and Michigan State University combined booth!  

We've setup up a rack of equipment designated for use by OSiRIS, <a href="http://slateci.io/">SLATE</a>, and <a href="https://www.aglt2.org/">AGLT2</a> demos at SC.  The rack was shipped as a unit from Michigan last week.  


<br style="clear:both" />

<div class="imgwrap lf" style="width: 30%">
<a href="{{IMAGE_PATH}}/sc18/crate-posters.jpg">
    <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/crate-posters.jpg" alt="Equipment Crate" />
</a>
Demo Equipment 
</div>

<div class="imgwrap lf" style="width: 30%">
<a href="{{IMAGE_PATH}}/sc18/crate-posters-rear.jpg">
    <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/crate-posters-rear.jpg" alt="UM and MSU Booth" />
</a>
Combined MSU / UM Booth
</div>

<div class="imgwrap lf"  style="width: 30%">
<a href="{{IMAGE_PATH}}/sc18/showfloor-general-1.jpg">
    <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/showfloor-general-1.jpg" alt="Convention Showroom" />
</a>
Showroom Floor during early setup
</div>

<div class="imgwrap lf" style="width: 30%">
<a href="{{IMAGE_PATH}}/sc18/crate-front-1.jpg">
    <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/crate-front-closeup.jpg" alt="Equipment Crate" />
</a>
Demo Equipment Crate
</div>

<div class="imgwrap lf" style="width: 30%">
<a href="{{IMAGE_PATH}}/sc18/crate-rear.jpg">
    <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/crate-rear-closeup.jpg" alt="Equipment Crate (rear)" />
</a>
Demo Equipment Crate (rear)
</div>

<br style="clear:both" />

<!--excerpt-->

Our demonstration will encompass our use of storage features, advanced networking, identity management/onboarding, and include a collaboration with <a href="http://slateci.io/">SLATE infrastructure</a> utilizing OSiRIS storage.

<ul>
    <li> 
        <p>
        Storage Features:  Typical Ceph storage clusters are heavily affected by network latency between components and clients.  As such a client accessing OSiRIS storage in Michigan from the SC showroom would not see similar performance to our more proximate users.  OSiRIS will deploy dedicated storage hardware for a Ceph cache-tier at SC18 to show that it is possible to achieve reasonable performance even though the backing data pool components are geographically quite far away.  A similar demonstration optimized for read-only will be done using a technique to configure pools such that they direct all reads to the storage component of our choice.  We will compare/contrast the two as they might apply to various scenarios.  The collaboration with SLATE will also leverage these configurations and give us experience with a new use case.
        <div class="imgwrap" style="width: 70%">
        <a href="{{IMAGE_PATH}}/sc18/OSiRIS-SC18-OverviewDiagram.jpg">
            <img style="width: 100%" src="{{IMAGE_PATH}}/sc18/OSiRIS-SC18-OverviewDiagram.jpg" alt="Conceptual diagram for OSiRIS SC18" />
        </a>
        </div>
        </p> 
    </li>
    <li>
        <p>
        Advanced Networking:  The OSiRIS Network Management Abstraction Layer (NMAL) seeks to orchestrate network pathing and quality of service based on real-time feedback.  At SC18 we plan to demonstrate the impact of these intelligent network capabilities on the client experience.
    </p>
    </li>
    <li>    
        <p>
        Identity Management / onboarding:  OSiRIS virtual organizations and the people within those organizations are managed by Internet2 COmanage and a collection of plugins we’ve written to tie together with Ceph storage.  For SC18 we’ll spawn one or more virtual organizations for the show and demonstrate self-service onboarding and credential management linked to existing institutional federated identities.  Our ideal scenario would be if other demonstrators at SC18 made some active use of OSiRIS storage in scenarios similar to real-world usage.   Here again we can somewhat refer to the collaboration with SLATE as they will obtain storage allocation and credentials via this infrastructure.  
    </p>
    </li>
</ul>   

<span style="text-align: center; font-weight: bold; font-size: 120%"><a href="/sc18">Information for using the OSiRIS Supercomputing 2018 Sandbox</a></span>

<hr> 

Thanks to everyone on the OSiRIS team at University of Michigan, Wayne State University, Indiana University, and Michigan State University for helping to make the conference a great success!

<img src="{{IMAGE_PATH}}/sc18/its-signature-vertical.png" alt="UM ITS Logo" class="lf" style="width:25%">
We appreciate the support of Nick Grundler and Dan Eklund from the UM ITS team.  Their hard work before and during the conference made sure we had stable, fast network paths to the conference and on the showroom floor.    

<br clear='left' />

Special thanks to Wenjing Wu and Troy Morgan from UM Physics/AGLT2 for assistance with equipment preparation before and after the conference. 

Thanks to Merit Networks and Internet2 for assistance providing 100Gb network paths from Michigan to the conference.

<a href="https://www.merit.edu/"><img style="width: 30%" src="{{IMAGE_PATH}}/sc18/merit_logo.png" alt="Merit Logo"></a>
<a href="https://www.internet2.edu"><img style="width: 30%" src="{{IMAGE_PATH}}/sc18/internet2_logo.gif" alt="Internet2 Logo"></a>

Thanks to Juniper and Adva for providing network equipment.

<a href="http://www.juniper.net"><img style="width: 40%; padding-right: 50px" src="{{IMAGE_PATH}}/sc18/juniper-networks-blue-png.png" alt="Juniper Logo"></a>
<a href="http://www.advaoptical.com"><img style="width: 30%" src="{{IMAGE_PATH}}/sc18/ADVA_Optical_Networking.svg.png" alt="ADVA Logo"></a>

We would also like to acknowledge the hard-working team that built the <a href="https://sc18.supercomputing.org/experience/scinet/">SCinet infrastructure</a> to support local and wide-area networks at the conference.  

