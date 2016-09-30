---
layout: default
title : OSiRIS Monitoring and Logging
header : OSiRIS Monitoring and Logging
sidebar: components-menu.html
---
{% include JB/setup %}

We use several tools to gain insight into performance at each level of our infrastructure.

Metric/stats collection is done with [Collectd](https://collectd.org/) on host systems feeding instances of [Influxdb](https://influxdata.com/time-series-platform/influxdb/).  We then visualize this data with [Grafana](http://grafana.org/). A variety of Collectd plugins gather data about Ceph, system performance, network throughput, switch interfaces (snmp plugin), and more.  

[![Collectd-Influx-Grafana Stack]({{IMAGE_PATH}}/monitoring/collectd-influxdb-grafana.png){: style="width: 700px"}]({{IMAGE_PATH}}/monitoring/collectd-influxdb-grafana.png)

#### Cluster Dashboard
[![Cluster Dashboard]({{IMAGE_PATH}}/monitoring/Cluster Dash Write.png){: style="width: 800px"}]({{IMAGE_PATH}}/monitoring/Cluster Dash Write.png)

#### Detail of OSD/Journal IO
[![OSD IO Detail]({{IMAGE_PATH}}/monitoring/OSD IO Detail.png){: style="width: 800px"}]({{IMAGE_PATH}}/monitoring/OSD IO Detail.png)

#### ELK Stack
Log collection and aggregation uses the "ELK" stack and [Filebeat](https://www.elastic.co/products/beats/filebeat) for shipping logs to Elasticsearch  

Log collection and processing in [Logstash](https://www.elastic.co/products/logstash)  
Log storage in an [Elasticsearch Cluster](https://www.elastic.co/products/elasticsearch)  
Visualization in [Kibana](https://www.elastic.co/products/kibana) and also in [Grafana](http://grafana.org/) for data processed as time-series.   

[![ELK Stack in OSiRIS]({{IMAGE_PATH}}/monitoring/flek-overview.png){: style="width: 600px"}]({{IMAGE_PATH}}/monitoring/flek-overview.png)