---
layout: default
title : Monitoring
header : OSiRIS Monitoring and Logging
group: components
subnavgroup: components
---
{% include JB/setup %}

We use several tools to gain insight into performance at each level of our infrastructure.

For many system metrics we use <a href="https://collectd.org/">Collectd</a>.  Typical metrics include CPU, disk, network (including OVS stats), and also metrics specific to some of our services such as HAproxy and Ceph processes details.  To configure collectd we use a <a href="https://forge.puppet.com/puppet/collectd">puppet-collectd</a> module.  

Ceph Metrics are gathered by a plugin to ceph-mgr originally written by a U-M student while working for our project.  The plugin was contributed back to Ceph where it has seen significant modification since then.  Some details about the plugin are covered in <a href="{% post_url 2017-12-7-the-influxdb-ceph-mgr-plugin %}">our article</a> and you can also find out more information from the <a href="http://docs.ceph.com/docs/master/mgr/influx/">Ceph documentation.

For new deployments considering the question of Ceph metrics and monitoring you may also want to look into Prometheus.  It also has a ceph-mgr plugin for exporting stats.  

In our case we feed metrics from ceph-mgr and from Collectd to <a href="https://www.influxdata.com/time-series-platform/influxdb/">InfluxBD</a>.  We run our own instance of the open source edition with NVMe storage.  

We take the stats from Influxdb and use <a href="https://grafana.com/">Grafana</a> to construct dashboards for monitoring Ceph status, system status, etc.  


<div class="imgwrap" style="width: 80%">
<a href="{{IMAGE_PATH}}/components/grafana-cluster-dash.png">
    <img style="width: 100%" src="{{IMAGE_PATH}}/components/grafana-cluster-dash.png" alt="Example OSiRIS Cluster Dashboard" />
</a>
OSiRIS Cluster Dashboard combining Ceph metrics from manager plugin and system metrics gathered with Collectd</div>


Metric/stats collection is done with [Collectd](https://collectd.org/) on host systems feeding instances of [Influxdb](https://influxdata.com/time-series-platform/influxdb/).  We then visualize this data with [Grafana](http://grafana.org/). A variety of Collectd plugins gather data about Ceph, system performance, network throughput, switch interfaces (snmp plugin), and more.  

#### ELK Stack

Log collection and aggregation uses the "ELK" stack and [Filebeat](https://www.elastic.co/products/beats/filebeat) for shipping logs to [Elasticsearch Cluster](https://www.elastic.co/products/elasticsearch).  We collect logs from syslog files, from Ceph log files, and also logs from devices such as switches.  These are all fed into [Logstash](https://www.elastic.co/products/logstash).  

For log searching and visualization we use [Kibana](https://www.elastic.co/products/kibana).  [Grafana](http://grafana.org/) can also use Elasticsearch data for generating plots though it is not as convenient as other inputs from time-series databases

[![ELK Stack in OSiRIS]({{IMAGE_PATH}}/components/flek-overview.png){: style="width: 70%"}]({{IMAGE_PATH}}/components/flek-overview.png)
