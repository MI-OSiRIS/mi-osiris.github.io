---
layout: post
category : article
title: New Storage Deployed
tags : [ hardware, storage ]
---
{% include JB/setup %}

<div class="imgwrap lf" style="width: 28%">
<a href="{{IMAGE_PATH}}/hardware2019/umich-rack-new-front-cropped.jpg">
    <img style="width: 100%" src="{{IMAGE_PATH}}/hardware2019/umich-rack-new-front-cropped.jpg" alt="New OSiRIS hardware nodes" />
</a>
New OSiRIS storage nodes:  Dell R7425 (AMD Epyc) with 16 x 12 TB of storage
</div>

OSiRIS expanded our storage this year with the installation of 33 new nodes across the three core storage sites at U-M, WSU, and MSU.  Each site is deploying 11 new nodes for a total of about 6PB of new capacity.  

In prior years we have focused more on storage density per-node as our most cost effective path to maximizing available space.  Though we have had success with these high density nodes (~600 TB per system) the low node count also has implications for performance, replication times, and potential pool configurations when using erasure coding.  For this year we took a different approach and bought a higher count of nodes with less storage per node.

<!--excerpt-->

A higher node count means more failure domains (hosts) enabling more storage-efficient Ceph <a href="https://docs.ceph.com/docs/master/rados/operations/erasure-code/">Erasure Coded</a> pools.  With only 5-6 very large nodes the ratio of data chunks to EC chunks, and thus the overall space efficiency, cannot be very large.  A higher node count for given amount of storage also tends to increase performance.  Ceph is software defined storage so it responds well to more computational resources.  The new storage nodes give us a good mix to work with for different potential use cases.  

<br clear="left" />

<div class="imgwrap rf" style="width: 40%">
<a href="{{IMAGE_PATH}}/hardware2019/umich-rack-both-front.jpg">
    <img style="width: 100%" src="{{IMAGE_PATH}}/hardware2019/umich-rack-both-front.jpg" alt="New OSiRIS hardware nodes" />
</a>
Existing OSiRIS 600 TB storage nodes on left, new 190 TB OSiRIS storage nodes on the right.
</div>

The new hardware has the following specifications:
<ul>
<li>Dell PowerEdge R7425 / AMD EPYC 7301 2.2GHz/2.7GHz, 16 core</li>
<li>128GB Memory</li>
<li>16 x 12TB 7.2K RPM NLSAS 12Gbps 512e 3.5in hard drive</li>
<li>4 x 512GB Samsung 970 Pro NVMe in ASUS Hyper M.2 X4 Expansion Card (DB/WAL device, 4 per NVMe)</li>
<li>Mellanox ConnectX-4 LX Dual Port 10/25GbE SFP28</li>
<li><b>Net Result:</b> 1 core per OSD / disk, 128GB DB volume per OSD, 8GB RAM per OSD (minus OS needs), 50 Gbps connectivity (OVS bond)</li>
</ul>

You can see the difference between the two nodes types in this side-by-side picture.  The nodes on the left have 60 disk JBOD (Dell MD3060e) attached.  

<h2>More on our NVMe and DB sizing</h2>

As configured by default, the RocksDB that Ceph uses to hold OSD metadata will only put database 'levels' on fast disk if the disk can hold the entire level.  The size of the levels is determined by a base size and a multiplier for each level.  What this ultimately means is that DB volume sizes must take the whole size of each level into account and if not large enough to fit an entire level the extra space is not used.  Effective sizes, including some space for the OSD WAL, are 4, 30, 286 GB.  

Ideally space is also left for the DB levels to compact while staying contained on fast storage.  During a compaction the entire new compacted level must fit alongside the existing uncompacted level so this in effect means doubling the size.

Whether doubling size or not, 286 / 572 GiB is too large to be cost effective when considering high-endurance drives suitable for Ceph.  We ended up assuming 60GiB which maps onto the 512GB drive size commonly available when putting 4 OSD on a single NVMe device.  

A much more detailed discussion of the topic is available <a href="https://yourcmc.ru/wiki/Ceph_performance#About_block.db_sizing">in this article</a>

This <a href="https://tracker.ceph.com/issues/38745">Ceph tracker issue</a> also discusses the topic and the 2x compaction requirement.  

