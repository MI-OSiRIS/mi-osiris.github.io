---
layout: post
category: article
title: OSiRIS at the Van Andel Institute in Grand Rapids
tagline: Leveraging Ceph Caching
tags : [ceph, caching, van andel, articles]
---
{% include JB/setup %}

 For more information please see our <a href="/domains/vai.html">full article</a> covering the configuration and performance of the Van Andel site.

 Building on existing collaboration between MSU and the Grand Rapids based Van Andel Institute, OSiRIS has deployed NVMe-based Ceph OSD nodes and an NFS gateway at the institute to enable direct access to bioinformatics research data.  OSIRIS at VAI will enable VAI bioinformaticians to work with MSU researchers to better understand Parkinson's disease and cance.  OSiRIS facilitates data access for VAI researchers to leverage the computational resources at MSU Institute for Cyber Enabled Research.

 The OSiRIS site at Van Andel is deployed and managed similar to other OSiRIS sites.  The 3 nodes there are part of the multi-institutional OSiRIS cluster and OSD are partitioned into a separate Ceph Crush tree to be used in rules defining cache tier pools.  

<div class="imgwrap" style="width: 90%">
<a href="/domains/vai.html">
    <img style="width: 100%" class="rf" src="{{IMAGE_PATH}}/domains/VAI-Cache-Diagram.jpg
" alt="Van Andel Institute site overview diagram" />
</a>
</div>




<!--excerpt-->
