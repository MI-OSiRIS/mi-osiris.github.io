---
layout: default
title : Components
tagline : Technology Components in OSiRIS
group: navigation
subnavgroup: components
order: 4
---
{% include JB/setup %}

OSiRIS is built on open source technology.  The components we used or built are detailed below.

<h3>Ceph</h3>

[![Ceph Logo]({{IMAGE_PATH}}/logos/ceph.png)](http://www.ceph.com)

[Ceph](http://www.ceph.com) is a distributed object store and file system designed to provide excellent performance, reliability and scalability.  

The OSiRIS Ceph deployment spans WSU, MSU, and UM.  We currently have deployed approximately 970 OSD.  Our OSD are 8TB or 10TB disks for a total of about 8PB raw storage.

For information on how we tune and configure Ceph:  <a href="/components/ceph">Ceph configuration</a>

One of our project goals is to explore the limits of Ceph and our distributed architecture.  As such we did extensive <a href="/components/ceph/latency.html">simulated latency testing</a>.

We also did <a href="{% post_url 2016-11-15-provisioning-osiris-at-sc16 %}">real-world latency testing</a> at Supercomputing 2016.  As a method to work around network latency we have also explored and are actively using Ceph cache tiering functionality.  Experiments with this were done at <a href="{% post_url 2016-11-16-ceph-cache-tiering-with-liqid-nvme-at-sc16 %}">Supercomputing 2016</a>, <a href="{% post_url 2018-11-19-osiris-at-supercomputing-2018 %}">Supercomputing 2018</a>, and we have deployed a production cache tier at the <a href="/domains/vai.html">Van Andel Institute</a> in Grand Rapids, MI.  

The Ceph CRUSH map also allows for choosing which OSD will be used as the primary in any given set of replicas, and the primary is where reads/writes are directed.  Setting the primary to be proximate to where most client reads will occur can boost performance (for those clients) in a high-latency deployment.  Our <a href="{% post_url 2019-03-01-ceph-osd-site-affinity %}">article</a> details the configuration and performance benchmarks. 

<h4>COmanage</h4>

OSiRIS identity management and provisioning is handled by <a href="https://www.internet2.edu/products-services/trust-identity/comanage/">Internet2 COmanage</a>.  Plugins to provision user information from COmanage to LDAP and to Grouper are part of the COmanage release.  For Ceph we created a new plugin.  Each plugin is developed on a git branch and merged into a master branch that reflects our current in-use version of COmanage.  We tend to track the <a href="https://github.com/Internet2/comanage-registry/tree/develop">master</a> branch of COmanage.  

More information and usage instructions for the COManage Ceph Provisioner plugin are available in <a href="cephprovisioner.html">our documentation</a>.  

<a class="ptitle" href="https://github.com/MI-OSiRIS/comanage-registry/tree/ldap_user_group/app/AvailablePlugin/LdapUserPosixGroupProvisioner">LdapUserPosixGroupProvisioner:</a> A simple plugin that provisions a posixGroup with gid matching every posixUser uid.  Possibly will be obsoleted by including this feature in the core LdapProvisioner plugin but nonetheless we needed something to do this.  

Stable code from of all of these plugins is combined on the <a href="https://github.com/MI-OSiRIS/comanage-registry/tree/osiris_master">osiris_master</a> Git branch within our fork of the <a href="https://github.com/Internet2/comanage-registry">Internet2 COmanage repository</a>.  Other miscellanous changes to COmanage are also included on this branch but they are non-essential for recreating our functionality.   From time to time we have made PR to the upstream repo with small changes that are applicable to general use, and may at some point make an effort to include our other plugins in the upstream release if there is interest.  

<h3>Monitoring</h3>

For many system metrics we use <a href="https://collectd.org/">Collectd</a>.  Typical metrics include CPU, disk, network (including OVS stats), and also metrics specific to some of our services such as HAproxy and Ceph processes details.  To configure collectd we use a <a href="https://forge.puppet.com/puppet/collectd">puppet-collectd</a> module.  

Ceph Metrics are gathered by a plugin to ceph-mgr originally written by a U-M student while working for our project.  The plugin was contributed back to Ceph where it has seen significant modification since then.  Some details about the plugin are covered in <a href="{% post_url 2017-12-7-the-influxdb-ceph-mgr-plugin %}">our article</a> and you can also find out more information from the <a href="http://docs.ceph.com/docs/master/mgr/influx/">Ceph documentation.

For new deployments considering the question of Ceph metrics and monitoring you may also want to look into Prometheus.  It also has a ceph-mgr plugin for exporting stats.  

In our case we feed metrics from ceph-mgr and from Collectd to <a href="https://www.influxdata.com/time-series-platform/influxdb/">InfluxBD</a>.  We run our own instance of the open source edition with NVMe storage.  

We take the stats from Influxdb and use <a href="https://grafana.com/">Grafana</a> to construct dashboards for monitoring Ceph status, system status, etc.  

Log collection and aggregation uses the "ELK" stack and [Filebeat](https://www.elastic.co/products/beats/filebeat) for shipping logs to [Elasticsearch Cluster](https://www.elastic.co/products/elasticsearch).  We collect logs from syslog files, from Ceph log files, and also logs from devices such as switches.  These are all fed into [Logstash](https://www.elastic.co/products/logstash).  

For log searching and visualization we use [Kibana](https://www.elastic.co/products/kibana).  [Grafana](http://grafana.org/) can also use Elasticsearch data for generating plots though it is not as convenient as other inputs from time-series databases.

<a href="/components/monitoring.html">More details about monitoring tools</a>

<h3>Puppet Modules</h3>
We use Puppet to manage setup and configuration.  The following puppet modules were created or forked from other modules and modified for OSiRIS usage.  Documentation on using them is included in the repository README file.

<a href="/components/management.html">More information on Puppet and other management tools we use</a>

<a class="ptitle" href="https://github.com/MI-OSiRIS/puppet-ceph">puppet-ceph:</a> OSiRIS storage is provided by Ceph.  This puppet module is used to deploy and manage all ceph components.  It was recently updated to deploy Bluestore OSD.  Our version is forked from <a href="https://github.com/openstack/puppet-ceph">openstack/puppet-ceph</a>

<a class="ptitle" href="https://github.com/MI-OSiRIS/puppet-ds389">puppet-ds389:</a>  OSiRIS backend directory services are provided by 389 Directory server in a multi-master replicated configuration.  This module is used to deploy/manage that configuration and additional schema required for OSiRIS.  

<a class="ptitle" href="https://github.com/MI-OSiRIS/puppet-grouper">puppet-grouper:</a> OSiRIS Posix groups are managed and provisioned to LDAP by <a href="https://www.internet2.edu/products-services/trust-identity/grouper/">Internet2 Grouper</a>.  Grouper could also be extended with additional provisioning targets to manage non-LDAP groups or to translate group memberships to other models such as S3 bucket ACL users but we haven't explored this.  This puppet module manages Grouper config as used by OSiRIS but requires some pre-setup of Grouper.  

<a class="ptitle" href="https://github.com/MI-OSiRIS/puppet-shibboleth">puppet-shibboleth:</a>  Our web services are authenticated by Shibboleth using InCommon meta-data.  We use this puppet module to manage the configuration.  It is forked from <a href="https://github.com/Aethylred/puppet-shibboleth">Aethylred/puppet-shibboleth</a>.

<a class="ptitle" href="https://github.com/MI-OSiRIS/puppet-pdsh">puppet-pdsh:</a>  Pdsh is a utility for running shell commands via ssh on multiple nodes in parallel.  Our module can be used as a puppet exported resource to define and gather node definitions and groupings for pdsh.  

Many other internal components are managed by puppet modules also available from our <a href="https://github.com/MI-OSiRIS">Github repository</a>.  These include LLDP for network link information, Rancid network config version control, and a Shibboleth auth module for our <a href="https://www.dokuwiki.org/dokuwiki#">Dokuwiki</a> internal wiki.  Further information on any module should be in the repository README.  We also leverage a large number of modules from <a href="http://forge.puppet.com">Puppet Forge</a> for basic system configuration.  






