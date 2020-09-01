---
layout: post
category : article
title: Ceph Upgrade from Nautilus to Octopus
tags : [ ceph, octopus, nautlius ]
---
{% include JB/setup %}

The OSiRIS team updated the ceph cluster from Nautilus 14.2.9 to Octopus 15.2.4 which is the latest release of Ceph as of August 2020 and it is the fourth release of the Ceph Octopus stable release series.  

<strong> Major Changes from Nautilus </strong>
<ul>
   <li>A new deployment tool called <b>cephadm</b> has been introduced that integrates Ceph daemon deployment and management via containers into the orchestration layer. For more information see <a href="https://docs.ceph.com/docs/master/cephadm/#cephadm">Cephadm</a>
    </li>
    <li> Health alerts can now be muted, either temporarily or permanently.   
    </li>
    <li>Health alerts are now raised for recent Ceph daemons crashes.    
    </li>  
</ul>

<!--excerpt-->

<strong> CentOS 7 Dependencies </strong>

The dashboard, prometheus, and restful manager modules do not work on CentOS 7 build due to Python 3 module dependencies that are missing in CentOS 7. To resolve the dependency issue and make sure the dashboard, prometheus and restful manager modules function as desinged in Octopus we installed three python3 rpm packages in our repo server by adding them to um-repo. The 3 packages are i) python3-cherrypy ii) python3-routes iii) python3-jwt. Please install these python3 packages in CentOS7 before proceeding with upgrade to Ceph Octopus if you use the ceph-mgr-dashboard, prometheus and restful manager modules.

<strong> Upgrade Instructions </strong>

<ol>
<li> Make sure your cluster is stable and healthy (no down or recovering OSDs) </li>
<pre>
ceph health detail
</pre>

<li> Set the noout flag for the duration of the upgrade </li>
<pre>
ceph osd set noout
</pre> 

<li> Upgrade monitors by installing the new packages and restarting the monitor daemons </li>
<pre>
systemctl restart ceph-mon.target
</pre>

Once all monitors are up, verify that the monitor upgrade is complete by looking for the octopus string in the mon map
<pre>
ceph mon dump | grep min_mon_release
</pre>

The output should show :
<pre>
min_mon_release 15 (octopus)
</pre>

<li> Upgrade ceph-mgr daemons by installing the new packages and restarting all manager daemons </li>
<pre>
systemctl restart ceph-mgr.target
</pre>

Verify that ceph-mgr deamons are running by executing <pre>ceph -s </pre>

<li> Upgrade all OSDs by installing the new packages and restarting the ceph-osd daemons on all OSD hosts </li>
<pre>
systemctl restart ceph-osd.target
</pre>

The progress of the OSD upgrades can be monitored using the either of the commands
<pre>
ceph versions 
ceph osd versions
</pre>

<li> Upgrade all CephFS MDS daemons </li>
<br>
<li> Upgrade all radosgw daemons by upgrading packages and restarting daemons on all hosts </li>
<pre>
systemctl restart ceph-radosgw.target
</pre>

<li> Complete the upgrade by disallowing pre-Octopus OSDs and enabling all new Octopus-only functionality </li>
<pre>
ceph osd require-osd-release octopus
</pre>

<li> If noout was set at the beginning be sure to clear it with</li>
<pre>
ceph osd unset noout
</pre>

<li>Verify the cluster is healthy by running</li>
<pre>
ceph health
</pre>

</ol>

For the complete information about upgrading Ceph from Nautilus to Octopus  including new features, prerequisties and compatibility deatils , please refer to the <a href="https://docs.ceph.com/docs/master/releases/octopus/#v15-2-0-octopus">Octopus upgrade documentation</a> on the ceph website


