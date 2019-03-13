---
layout: default
title : Tuning
header : System Tunings for Network and Ceph
subnavgroup: components
group: components
---
{% include JB/setup %}

We started with the RHEL7 tuned 'latency-performance' profile on hardware doing duty as storage blocks.  This profile adjusts default C-states to reduce latency from switching out of deep C-states.  Hardware acting as transfer nodes is set to the 'throughput-performance' profile, and our hypervisors use 'virtual-host'.  Our service VMs use the 'virtual-guest' profile.  For more information check out the <a href="https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Performance_Tuning_Guide/chap-Red_Hat_Enterprise_Linux-Performance_Tuning_Guide-Tuned.html#ch-Tuned-overview">Redhat docs</a>.
Building on the baseline profiles we then apply the following sysctl tunings to some hosts.

## Ceph Storage Block (OSD) Tuning

These apply only to Ceph storage blocks.  Mainly we are aiming to reduce VM swapping to ensure OSD never have to wait for it.  
File max is because Ceph tends to open many file descriptors.  This is perhaps less the case in recent versions of Ceph which use an asynchronous messaging thread pool instead of keeping many messaging threads open statically.  

<pre>
fs.file-max = 78718144
vm.swappiness = 20
vm.vfs_cache_pressure = 20
</pre>

## Network Tuning

These are applied to every machine in OSiRIS.  They are collected from a variety of sources including https://fasterdata.es.net/host-tuning/linux/ and others.  


<pre>
net.core.optmem_max = 40960
net.ipv4.tcp_max_syn_backlog = 4096
net.core.default_qdisc = fq_codel
net.ipv4.tcp_fin_timeout = 15
net.ipv4.tcp_wmem = 4096 87380 16777216
net.ipv4.tcp_congestion_control = htcp
net.ipv4.tcp_window_scaling = 1
net.ipv4.tcp_slow_start_after_idle = 0
net.ipv4.tcp_rmem = 4096 87380 16777216
net.ipv4.tcp_timestamps = 1
net.ipv4.tcp_low_latency = 1
net.ipv4.tcp_keepalive_intvl = 15
net.core.wmem_max = 67108864
net.ipv4.tcp_rfc1337 = 1
net.ipv4.neigh.default.unres_qlen = 6
net.core.netdev_max_backlog = 250000
net.ipv4.tcp_keepalive_time = 300
net.ipv4.tcp_keepalive_probes = 5
net.core.dev_weight = 128
net.core.somaxconn = 1024
net.ipv4.neigh.default.proxy_qlen = 96
net.ipv4.ipfrag_low_thresh = 446464
net.ipv4.ipfrag_high_thresh = 512000
net.ipv4.tcp_sack = 1
net.core.rmem_max = 67108864
</pre>

