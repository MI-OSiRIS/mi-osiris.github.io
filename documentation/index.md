---
layout: default
title : Documentation
group: navigation
order: 7
---
{% include JB/setup %}

We've included here instructions for OSiRIS users as well as for other sites that are interested in setting up an installation similar to OSiRIS.

Questions:  <a href="mailto:osiris-help@umich.edu">osiris-help@umich.edu</a>

<h3>User Documentation</h3>

<p>
<a href="enrollment.html">Enrolling in OSiRIS:</a> 

How to enroll in your OSiRIS COU and obtain access tokens for use with OSiRIS Storage
</p>

<p>
<a href="sshkey.html">Uploading an SSH key:</a>

How to upload your ssh key so you can use OSiRIS ssh/scp/sftp gateways
</p>

<p>
    <a href="s3.html">Using OSiRIS S3:</a>
    How to obtain credentials and use OSiRIS S3 gateways
</p>

<p>
    <a href="globus.html">Using Globus with OSiRIS:</a>
    How to get setup to use Globus with OSiRIS CephFS or S3 storage.
</p>

<p>
    <a href="nfs.html">Using NFS with OSiRIS:</a>
    How to access NFS exports of OSiRIS CephFS on U-M or MSU campuses
</p>

<p>
    <a href="rados.html">Using RADOS:</a>
    How to use OSiRIS Ceph object store directly with rados libs and utils (requires configuration, please contact us)
</p>


<p>
    <a href="groups.html">Managing OSiRIS Groups:</a>

    How to create new posix groups and manage memberships
</p>

<p>
<a href="s3fuse.html">Configuring an S3 fuse mount:</a>

 The S3 fuse program will present S3 buckets as mounted filesystems though the standard http-based S3 protocol.
</p>

<h3>OSiRIS Setup Documentation</h3>

At this time we do not have detailed setup documentation for OSiRIS.  However, all of the components used are publicly available.  Here is a quick overview.

<h4>Puppet Modules</h4>
Generally we use Puppet to manage setup and configuration.  The following puppet modules were created or forked from other modules and modified for OSiRIS usage.  Documentation on using them is included in the repository README file.

<a class="ptitle" href="https://github.com/MI-OSiRIS/puppet-ceph">puppet-ceph:</a> OSiRIS storage is provided by Ceph.  This puppet module is used to deploy and manage all ceph components.  It was recently updated to deploy Bluestore OSD.  Our version is forked from <a href="https://github.com/openstack/puppet-ceph">openstack/puppet-ceph</a>

<a class="ptitle" href="https://github.com/MI-OSiRIS/puppet-ds389">puppet-ds389:</a>  OSiRIS backend directory services are provided by 389 Directory server in a multi-master replicated configuration.  This module is used to deploy/manage that configuration and additional schema required for OSiRIS.  

<a class="ptitle" href="https://github.com/MI-OSiRIS/puppet-grouper">puppet-grouper:</a> OSiRIS Posix groups are managed and provisioned to LDAP by <a href="https://www.internet2.edu/products-services/trust-identity/grouper/">Internet2 Grouper</a>.  Grouper could also be extended with additional provisioning targets to manage non-LDAP groups or to translate group memberships to other models such as S3 bucket ACL users but we haven't explored this.  This puppet module manages Grouper config as used by OSiRIS but requires some pre-setup of Grouper.  

<a class="ptitle" href="https://github.com/MI-OSiRIS/puppet-shibboleth">puppet-shibboleth:</a>  Our web services are authenticated by Shibboleth using InCommon meta-data.  We use this puppet module to manage the configuration.  It is forked from <a href="https://github.com/Aethylred/puppet-shibboleth">Aethylred/puppet-shibboleth</a>.

Many other internal components are managed by puppet modules also available from our <a href="https://github.com/MI-OSiRIS">Github repository</a>.  These include pdsh for distributed command execution, LLDP for network link information, Rancid network config version control, and a Shibboleth auth module for our <a href="https://www.dokuwiki.org/dokuwiki#">Dokuwiki</a> internal wiki.  Further information on any module should be in the repository README.  We also leverage a large number of modules from <a href="http://forge.puppet.com">Puppet Forge</a> for basic system configuration.  

<h4>COmanage</h4>

OSiRIS identity management and provisioning is handled by <a href="https://www.internet2.edu/products-services/trust-identity/comanage/">Internet2 COmanage</a>.  Plugins to provision user information from COmanage to LDAP and to Grouper are part of the COmanage release.  Plugins related to Ceph we had to write.  Each plugin is developed on a git branch and merged into a master branch that reflects our current in-use version of COmanage.  We tend to track the <a href="https://github.com/Internet2/comanage-registry/tree/develop">develop</a> branch of COmanage.  

<a class="ptitle" href="https://github.com/MI-OSiRIS/comanage-registry/tree/ceph_provisioner/app/AvailablePlugin/CephProvisioner">CephProvisioner:</a> This plugin provisions COmanage identities to Ceph.  It covers several provisioning operations:

<ul>
<li>
    <strong>COU</strong> - When new COU are created the plugin creates data pools in Ceph for that COU and associates them with the appropriate application (CephFS, RGW).  It also creates data placement targets and tags for the RGW pool. 
</li>

<li>
    <strong>RGW</strong> - A RGW user is created for each unique combination of uid identifier and COU name (ie, username_somecou).  This decision was made so we could support setting default data placement targets for each user associated to per-COU data pools.  When the user is provisioned they are configured with default placement and placement tags corresponding to their COU data placement targets.   Users can retrieve their LDAP RGW tokens from the COmanage service token page (modifications were made to the CoServiceToken plugin)
</li>

<li>
    <strong>CephFS</strong> - COmanage provisions LDAP posixUser information used by systems which mount CephFS, and it provisions default COU groups to Grouper where they they are provisioned to LDAP along with any user-created groups.  This plugin creates a ceph client key with appropriate access capabilities to access the COU directory path and COU data pool dedicated to CephFS.  We use an external script to create a directory for each COU and set the <a href="http://docs.ceph.com/docs/master/cephfs/file-layouts/">file layout</a> for the directory to be the COU CephFS data pool.  The key created by this plugin also includes capabilities to access COU data pools for rados and rbd.  Users can retrieve this key from the COmanage service tokens page (more modifications in CoServiceToken plugin)
</li>
</ul>

<a class="ptitle" href="https://github.com/MI-OSiRIS/comanage-registry/tree/co_ldap_token_ceph/app/AvailablePlugin/CephRgwLdapTokenProvisioner">CephRgwLdapTokenProvisioner:</a>
 For the RGW case we use <a href="http://docs.ceph.com/docs/master/radosgw/ldap-auth/">LDAP</a> authentication.  This plugin provisions a simpleSecurityObject into an LDAP OU.  The object uid is a unique combination of uid identifier and COU name, and one object is provisioned for each COU a user might belong to.  The password is set from a COmanage service token type which we added to the CoServiceToken plugin.  The LDAP users match up with userid provisioned by the CephProvisioner plugin in radosgw.  

<a class="ptitle" href="https://github.com/MI-OSiRIS/comanage-registry/tree/co_osiris_tokens/app/AvailablePlugin/CoServiceToken">CoServiceToken:</a> This plugin is already part of COmanage but we made some modifications to save and display Ceph RGW ldap tokens and Ceph cluster auth keys.  Like other COmanage token types the user can regenerate the token on demand and retrieve it from the service token view.  RGW tokens generated by this plugin are saved and propogated to the LDAP directory by the CephRgwLdapTokenProvisioner.  Ceph cluster keys are generated with Ceph cluster commands from this plugin and saved for retrieval by the user.  It relies on the keys already being provisioned by the CephProvisioner plugin to generate a new key with identical caps.  

<a class="ptitle" href="https://github.com/MI-OSiRIS/comanage-registry/tree/ldap_user_group/app/AvailablePlugin/LdapUserPosixGroupProvisioner">LdapUserPosixGroupProvisioner:</a> A simple plugin that provisions a posixGroup with gid matching every posixUser uid.  Possibly will be obsoleted by including this feature in the core LdapProvisioner plugin but nonetheless we needed something to do this.  

Stable code from of all of these plugins is combined on the <a href="https://github.com/MI-OSiRIS/comanage-registry/tree/osiris_master">osiris_master</a> Git branch within our fork of the <a href="https://github.com/Internet2/comanage-registry">Internet2 COmanage repository</a>.  Other miscellanous changes to COmanage are also included on this branch but they are non-essential for recreating our functionality.   From time to time we have made PR to the upstream repo with small changes that are applicable to general use, and may at some point make an effort to include our other plugins in the upstream release if there is interest.  




