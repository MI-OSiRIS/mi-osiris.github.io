---
layout: default
title : OSiRIS Ceph Deployment
header : OSiRIS Ceph Deployment
sidebar: components-menu.html
---
{% include JB/setup %}
[![Ceph Logo]({{IMAGE_PATH}}/logos/ceph.png)](http://www.ceph.com)

[Ceph](http://www.ceph.com) is a distributed object store and file system designed to provide excellent performance, reliability and scalability.  

The OSiRIS Ceph deployment spans WSU, MSU, and UM.  We currently have deployed approximately 900 OSD.  Our OSD are 8TB or 10TB disks for a total of about 8PB raw storage.

[![Puppet]({{IMAGE_PATH}}/logos/puppet_logo.png){: style="float: left; margin-right: 10px"}]({{IMAGE_PATH}}/grafana/Collect-Grafana-Ceph-osd-op.png)
All of our components are deployed and managed with a puppet module forked from a module started by the Openstack group.  The module code is available on Github: [https://github.com/MI-OSiRIS/puppet-ceph](https://github.com/MI-OSiRIS/puppet-ceph)

<br />

#### Ceph Metrics 

To gather Ceph metrics we use Collectd with a plugin that reads from the daemon admin sockets.  Collectd feeds into Influxdb which supports intaking Collectd UDP data directly.  We also gather system stats such as CPU, Iotime, memory, threads, etc.  For an overview of this toolchain please have a look at our [monitoring and logging overview](/components/monitoring.html)

We can then visualize this data with Grafana.  For example, here are two simple dashboards showing OSD operation latency and operations per second.

##### OSD Operation latency
[![OSD Operations per second]({{IMAGE_PATH}}/grafana/Collectd-Grafana-Ceph-osd-op-latency.png){: style="width: 100%"}]({{IMAGE_PATH}}/grafana/Collectd-Grafana-Ceph-osd-op-latency.png)

##### OSD Operations per second
[![OSD Operations Latency]({{IMAGE_PATH}}/grafana/Collectd-Grafana-Ceph-osd-op.png){: style="width: 100%"}]({{IMAGE_PATH}}/grafana/Collectd-Grafana-Ceph-osd-op.png)



##### Cluster Dashboard

We also can combine plots to make dashboards giving us an overview of our cluster.


[![Ceph Dashboard]({{IMAGE_PATH}}/grafana/Collectd-Grafana-Ceph-Overview.png){: style="width: 100%"}]({{IMAGE_PATH}}/grafana/Collectd-Grafana-Ceph-Overview.png)


