---
layout: default
title: Performance
header : Ceph Network Latency 
group: navigation
sidebar: performance-menu.html
---
{% include JB/setup %}

One of our responsibilies under the NSF CC*DNI DIBBs grant is exploration of the limits of Ceph and our architecture.  Resilience to network latency is a key determinant in how far we can scale geographically.  

Latency was simulated using tc and netem.   More information on netem is here:  [https://wiki.linuxfoundation.org/networking/netem](https://wiki.linuxfoundation.org/networking/netem).
We wrote a small script to quickly change latency on all host interfaces:  [delay-script.sh]({{ASSET_PATH}}/misc/delay-script.sh)

## OSD Network Latency and RW speeds

We experimented with increasing the latency to a single storage block hosting 71 OSD while running rados bench write and rand read.  
In steps the induced latency on um-stor01 was increased to a max of 160ms ingress/egress, 320ms round trip (in addition to normal latency of a few ms). 

### Rados Bench Write
[![OSD Increasing Latency During Recovery]({{IMAGE_PATH}}/latency/OSD Latency - 320ms RTT - rados bench write.png){: style="width: 800px"}]({{IMAGE_PATH}}/latency/OSD Latency - 320ms RTT - rados bench write.png)

<br />


### Rados Bench Read Random
[![OSD Increasing Latency During Recovery]({{IMAGE_PATH}}/latency/OSD Latency - 320ms RTT - rados bench read random.png){: style="width: 800px"}]({{IMAGE_PATH}}/latency/OSD Latency - 320ms RTT - rados bench read random.png)

## OSD Network Latency during recovery

We experimented with ncreasing the latency to a single storage block while recovery operations were ongoing to another storage block.  The following annotated dashboards cover a time range shortly after wsu-stor01 was brought back online after the OSD on the host had been down approximately 3 days. During this time the cluster was steadily recovering placement groups.  

In steps the induced latency on um-stor01 was increased to a max of 160ms ingress/egress, 320ms round trip (in addition to normal latency of a few ms). From there it was backed down. The trip up and the trip down are focused on separately in the following 2 images.

wsu-stor01 and um-stor01 both have 60 OSD.  

### Latency increasing

[![OSD Increasing Latency During Recovery]({{IMAGE_PATH}}/latency/OSD Latency During Recovery - detail up to 320ms RT ascending.png){: style="width: 800px"}]({{IMAGE_PATH}}/latency/OSD Latency During Recovery - detail up to 320ms RT ascending.png)

### Latency decreasing

[![OSD Increasing Latency During Recovery]({{IMAGE_PATH}}/latency/OSD Latency During Recovery - detail up to 320ms RT ascending.png){: style="width: 800px"}]({{IMAGE_PATH}}/latency/OSD Latency During Recovery - detail up to 320ms RT ascending.png)

## Latency to client

There was nothing surprising here.  Read and write speeds steadily decrease with increasing latency to client.  Using rados bench utility.  

### Rados Bench Write Test

#### Cluster Dashboard

[![OSD Increasing Latency During Recovery]({{IMAGE_PATH}}/latency/Cluster Dash - Rados Bench Write Increasing Latency.jpg){: style="width: 800px"}]({{IMAGE_PATH}}/latency/Cluster Dash - Rados Bench Write Increasing Latency.jpg)

#### Client Network IO

[![OSD Increasing Latency During Recovery]({{IMAGE_PATH}}/latency/Client NetIO - Rados Bench Write Increasing Latency.jpg){: style="width: 800px"}]({{IMAGE_PATH}}/latency/Client NetIO - Rados Bench Write Increasing Latency.jpg)

### Rados bench random read test

#### Cluster Dashboard

[![OSD Increasing Latency During Recovery]({{IMAGE_PATH}}/latency/Cluster Dash - Rados Bench Rand Read Increasing Client Latency.jpg){: style="width: 800px"}]({{IMAGE_PATH}}/latency/Cluster Dash - Rados Bench Rand Read Increasing Client Latency.png)

#### Client Network IO

[![OSD Increasing Latency During Recovery]({{IMAGE_PATH}}/latency/Client NetIO - Rados Bench Rand Read Increasing Latency.jpg){: style="width: 800px"}]({{IMAGE_PATH}}/latency/Client NetIO - Rados Bench Rand Read Increasing Latency.png)


## Latency to monitors

A simple test of increasing latency to a monitor until things stopped working.  We found that cluster operations break down at 6400ms RTT.  It was no longer possible to show health, create auth keys, or map rbd.  At around 3200ms there was questionable stability with frequent monitor elections being forced.  There were no apparent issues at 1600ms besides slowness to complete operations requiring a monitor session.   