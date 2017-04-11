---
layout: default
title : System Tunings
header : System Tunings for Network and Ceph
sidebar: performance-menu.html
---
{% include JB/setup %}

We started with the RHEL7 tuned 'performance-throughput' profile on hardware doing duty as storage blocks, transfer nodes, or hypervisors.  Our service VMs use as a baseline the 'virtual-guest' profile.   Building on that baseline profile we then apply the following sysctl tunings.

## Ceph Storage Block (OSD) Tuning

These apply only to Ceph storage blocks:

<pre>
fs.file-max = 78718144
vm.swappiness = 20
vm.vfs_cache_pressure = 20

</pre>

## Network Tuning

These are applied to every machine in OSiRIS:

<pre>
net.ipv4.tcp_timestamps=1
net.ipv4.tcp_sack=1
net.core.netdev_max_backlog=250000
net.core.dev_weight=128
net.core.rmem_max=16777216
net.core.wmem_max=16777216
net.core.rmem_default=16777216
net.core.wmem_default=16777216
net.core.optmem_max=40960
net.core.somaxconn=1024
net.core.default_qdisc=fq_codel
net.ipv4.tcp_window_scaling=1
net.ipv4.tcp_rmem=4096 87380 16777216
net.ipv4.udp_rmem_min=16384
net.ipv4.tcp_wmem=4096 65536 16777216
net.ipv4.udp_wmem_min=16384
net.ipv4.tcp_max_syn_backlog=4096
net.ipv4.tcp_low_latency=1
net.ipv4.tcp_slow_start_after_idle=0
net.ipv4.tcp_congestion_control=htcp
net.ipv4.tcp_fin_timeout=15
net.ipv4.tcp_rfc1337=1
net.ipv4.tcp_keepalive_time=300
net.ipv4.tcp_keepalive_probes=5
net.ipv4.tcp_keepalive_intvl=15
net.ipv4.ipfrag_high_thresh=512000
net.ipv4.ipfrag_low_thresh=446464
net.ipv4.neigh.default.proxy_qlen=96
net.ipv4.neigh.default.unres_qlen=6
kernel.pid_max=4194303
fs.file-max=78718144
</pre>

