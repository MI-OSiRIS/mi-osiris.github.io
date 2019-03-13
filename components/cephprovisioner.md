---
layout: default
title : Ceph Provisioner
tagline : Ceph Storage and User provisioning
subnavgroup: components
group: components
---
{% include JB/setup %}

The CephProvisioner plugin provisions storage for COmanage COU and identities with the capabilities to use that storage.  It works by directly running 'ceph auth' and 'radosgw-admin' commands.  

The plugin source is on github: <br /> <a href="https://github.com/MI-OSiRIS/comanage-registry/tree/ceph_provisioner/app/AvailablePlugin/CephProvisioner">https://github.com/MI-OSiRIS/comanage-registry/tree/ceph_provisioner/app/AvailablePlugin/CephProvisioner</a>

The plugin handles the following
<ul>
<li>
    <strong>COU</strong> - When new COU are created the plugin creates data pools in Ceph for that COU and associates them with the appropriate application (CephFS, RGW).  It also creates data placement targets and tags for the RGW pool.  The Ceph credentials menu in COmnage allows users to select a default bucket placement target if they belong to multiple COU. 
</li>

<li>
    <strong>RGW</strong> - A RGW user is created matching COperson UID identifier.  The Ceph credentials menu in COmanage allows users to create additional userid and additional access/secret pairs for their userid. 
</li>

<li>
    <strong>CephFS</strong> - COmanage provisions LDAP posixUser information used by systems which mount CephFS, and it provisions default COU groups to Grouper where they they are provisioned to LDAP along with any user-created groups.  This plugin creates a ceph client key with appropriate access capabilities to access the COU directory path and COU data pool dedicated to CephFS.  We use an external script to create a directory for each COU and set the <a href="http://docs.ceph.com/docs/master/cephfs/file-layouts/">file layout</a> for the directory to be the COU CephFS data pool.  The key created by this plugin also includes capabilities to access COU data pools for rados and rbd. 
</li>
</ul>


<h3>Basic requirements</h3>

<p>You have installed COmanage according to their <a href="https://spaces.at.internet2.edu/display/COmanage/Registry+Installation">instructions</a>.  

<p>A Ceph client configuration and key with sufficient capabilities is required on the host running COmanage.
<pre>
ceph auth get-or-create client.comanage mon 'allow *' osd 'allow * pool=.rgw.root, allow *  \ 
pool=default.rgw.users.uid, allow * pool=default.rgw.meta, allow * pool=default.rgw.control, \
allow * pool=default.rgw.data.root, allow * pool=default.rgw.users.keys, \
allow * pool=default.rgw.users.email, allow * pool=default.rgw.log, \
allow * pool=default.rgw.users.swift'
</pre>

The key created above should be installed in /etc/ceph/ceph.client.comanage.keyring
</p>

<h3>Installation</h3>
<ol>
<li>Clone our repository from Github: <a href="https://github.com/MI-OSiRIS/comanage-registry">https://github.com/MI-OSiRIS/comanage-registry</a></li>
<li>Switch to the ceph_provisioner branch</li>
<li>Copy app/AvailablePlugin/CephProvisioner to the same directory in your installation.</li>
<li>Alternately:  Use the osiris_master branch of our repository when installing your COmanage instance - it will include the CephProvisioner plugin in the appropriate directory.  Instead of downloading their source tarball clone our repo (or download as zip) into your installation directory.</li>
<li>Link the plugin into local/Plugin:
<pre>
cd /srv/comanage/registry-current/local/Plugin
ln -s ../../app/AvailablePlugin/CephProvisioner .
</pre>
</li>
<li>
Setup the plugin schema (replace 'apache' with your httpd user if different):
<pre>
cd /srv/comanage/registry-current/app
su -c "./Console/cake database" apache
</pre>
</li>
</ol>

<h3>Setup</h3>
<ol>
    <li>In COmanage registry under the CO you have created (not under the COmanage internal CO) open the Configuration -> Provisioning Targets settings</li>
    <li>Add a new provisioning target.  Choose CephProvisioner as plugin type.  Optionally set it to be Manual if you would like the opportunity to test on a small scale by manually provisioning single COU or User (recommended)</li>
    <li>On the provising targets screen click the "Configure" button to set some required settings (details below)</li>
</ol>

<h3>Configuration reference</h3>

Many settings are available but may be obsolete or not yet implemented.  Here is a list of settings that are available and how you might use them.

<ul>
    <li>RGW URL:  Marked as required but not used.  Insert any URL here, preferably your actual RGW url for future use</li>
    <li>Ceph Client ID:  Required, should be the client id of the key you created to allow comanage access to the cluster.  Do not include the client. prefix.  For example, if they key was created following the example in this document then the client id is simply 'comanage'. </li>
    <li>RGW Access Key:  Marked as required but not used.  Any string will do.</li>
    <li>Create COU Data Pools: If set then COmanage will use the 'ceph' command to create data pools for new COU.  They will follow a pattern like 'cou.CouName.fs' and 4 pools will be created:  .fs, .rgw, .rados, .rbd.  </li>
    <li>COU Data Pool PG count:  Number of placement groups to specify for new COU data pools.  Set this low enough that your expected number of COU will not end up putting too many PG on your cluster.  You can always increase PG count later outside of COmanage</li>
    <li>LDAP Lookup Target / Grouper Lookup Target:  Obsolete feature, ignored.  It used to be possible to create client keys with uid/gid restrictions but we no longer support creating user keys with direct CephFS mount access in the plugin.  Grouper or LDAP would be used to discover the posix uid/gid. </li>
    <li>Use RGW LDAP Auth:  Obsolete feature, ignored:  At one time we provisioned RGW users into LDAP.  This is no longer true.  The feature was of little benefit since it is still necessary to create a RGW user to hold metadata, and the LDAP token format used for client credentials was confusing since it is unique to Ceph RGW</li>
    <li>Ceph User Prefix:  When creating ceph client keys they will be prefixed with this string.  The default is 'comanage' so new Ceph client keys are created as 'client.comanage.uid'</li>
    <li>Create COU data directory:  If enabled then COmanage will attempt to run an external script that creates a directory for new COU and sets attributes to place it on the 'cou.Name.fs' pool. </li>
    <li>COU dir create command:  The command to run if the above setting is checked.  The default is to use 'sudo' to run /usr/local/bin/mkCouDir.sh.   This script is included in the CephProvisioner/Lib directory and should be copied or symlinked into /usr/local/bin.  You will also need to set sudo permissions for the Apache user.  </li>
    <li>CephFS mountpoint:  If COU data directory creation is enabled, specify the path to create COU data directories</li>
    <li>CephFS Name:  Name of CephFS.  Will be needed to add new data pools for FS usage</li>
    <li>Set key uid/gid limitations:  Obsolete, ignored</li>

</ul>

Note:  The relevant code for enabling user keys to have CephFS access with uid and path restrictions is still in place but commented out - it most likely would work if enabled.  Key caps would be set to limit the path to their COU data directory and UID to those belonging to the COU.  In the context of our project the feature was not needed as we do not provide direct CephFS mounts but instead used NFSv4 to provide this service and the requisite UID mapping.   In general it is not safe to hand out client keys allowing external users to access the CephFS data pools directly but this is required if they use the keys to mount.  

<h3>Plugin Architecture</h3>

These diagrams give a rough overview of plugin provisioning flow for storage and users.  The user flow is mainly focused on initial provisioning and does not cover every scenario in detail for group updates, identifier changes, reprovision, etc.  

<div class="imgwrap" style="width: 70%">
<a href="{{IMAGE_PATH}}/components/COmanageCephStorageProvisioning.png">
    <img style="width: 100%" src="{{IMAGE_PATH}}/components/COmanageCephStorageProvisioning.png" alt="COmanage Ceph Storage Provisioning" />
</a>
OSiRIS COmanage Ceph storage provisioning flow
</div>
<hr>
<div class="imgwrap" style="width: 70%">
<a href="{{IMAGE_PATH}}/components/COmanageCephUserProvisioning.png">
    <img style="width: 100%" src="{{IMAGE_PATH}}/components/COmanageCephUserProvisioning.png" alt="COmanage Ceph User Provisioning" />
</a>
OSiRIS COmanage Ceph user provisioning and credential management flow
</div>

