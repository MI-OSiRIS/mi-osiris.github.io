---
layout: default
title : Management
header : Provisioning and configuration management
group: components
subnavgroup: components
---
{% include JB/setup %}

<h1>Foreman</h1>
OSiRIS uses Foreman for VM and hardware provisioning.  Foreman is structured to use small 'smart proxies' to provide DHCP, TFTP, and kickstart services to hosts in any given location controlled by a central management host.  This structure allows us to deploy hosts at any OSiRIS site from one interface.  It also allows us to bootstrap a new site simply by providing a small VM image pre-configured with appropriate smart-proxies and registering it to our Foreman instance.  We can also generate bootable media to start sites from scratch - for example to deploy a new virtualization host that can then host the Foreman proxy VM.  It is also used for for small sites not requiring the entire infrastructure, such as a site wishing only to deploy a local storage block.  

Foreman also has a variety of plugins to create different types of Virtual Machines which are then PXE booted and have an OS installed.  In our case we use the libvirt plugin to deploy kvm/libvirt VMs.  For non-virtual machines we define them in Foreman using the MAC address of an onboard network interface to PXE and build through.  More complex Openvswitch configurations are then put in place with a script we run post-install.  

<div class="imgwrap">
<a href="{{IMAGE_PATH}}/DeploymentOverview.png">
	<img src="{{IMAGE_PATH}}/DeploymentOverview.png" style="width: 100%">
</a>
	Provisioning hosts with Foreman and smart proxies
</div>

<h1>Puppet and Hiera</h1>

Every OSiRIS host is named following a pattern of site-role-nodetype.osris.org. The -nodetype suffix is optional and at this point only used for different storage block types so we can group common disk configurations.  By defining the common storage devices available on different hardware typese we can easily give these to puppet so it can be used to initialize Ceph OSD on our storage blocks.  

From the hostname we derive variables of the same name and use them to determine the host configuration in puppet. Variables site, role, and nodetype map to yaml files in hiera where we can store information specific to that class of system. They can also be used in puppet manifest logic.  Variables are derived with a simple regex in our site.pp file.

<pre>
if $trusted['certname'] =~ /^([A-z]+)-([A-z]+)-{0,1}([A-z]*)/  {
 $site = $1
 $role = $2
 $tnodetype = $3

  # set default types as needed 
 if ($role == 'stor') and ($tnodetype == '') {
  $nodetype = 'dmd'
 } else {
  $nodetype = $tnodetype
 }

 notice("Set site '$::site', nodetype '$::nodetype', and role '$::role' from hostname")
}

hiera_include('classes')
</pre>

<div class="imgwrap">
<a href="{{IMAGE_PATH}}/PuppetHieraOrganizationOverview.png">
	<img src="{{IMAGE_PATH}}/PuppetHieraOrganizationOverview.png" style="width: 100%">
</a>
	Organizing puppet data with Hiera
</div>

Our puppet code is structured around host 'roles' and service 'profiles'.  A given role may run several profiles depending on what is required.  For example, a host serving as a Ceph monitor includes profiles defining the Ceph configuration, a profile for Collectd configuration, and a base profile that all hosts get.  A google search on the topic will reveal many articles detailing the best practices for organizing puppet code in this manner.  

<h1>Puppet Environments</h1>

Puppet also integrates well with git version control.  A common tool used to manage git and puppet is <a href="https://github.com/puppetlabs/r10k">r10k</a>.  R10k deploys git branches into Puppet environments.  A puppet environment contains all the necessary modules, manifest code, and hiera config to apply puppet configurations to a client.  R10k simplifies multiple environments because it also manages external modules outside of your main puppet config tree - for example from the <a href="http://forge.puppet.com">Puppet forge</a> or from a tree on a public git repository.  All you have to do is specify them in a file called "Puppetfile" in the base of the puppet git repository and r10k will fetch and deploy them into your environment.  

The result is that any OSiRIS admin can create a new independent environment incorporating any modules they choose simply by creating a git branch and pushing it to the the master repository.  R10k can then be used to deploy the environment on our Puppet master(s).  Select hosts can be tested in the environment and after development and testing is complete a pull request can be made against our production git environment.  As we move to a more production-stable mode of operation there will likely be an intermediate testing and/or development environment with periodic releases to production but at the moment we just require verification that branches have been rebased to current production and tested on several hosts. 


<div class="imgwrap">
<a href="{{IMAGE_PATH}}/ManagementOverview.png">
	<img src="{{IMAGE_PATH}}/ManagementOverview.png" style="width: 100%">
</a>
	R10k and Git puppet environments
</div>

<h1>The Whole Picture</h1>
Putting it all together, the pieces detailed above fit together to enable us to deploy and manage OSiRIS across multiple sites with multiple admins.   

<img src="{{IMAGE_PATH}}/ProvisionBlock.png" alt="OSiRIS Provisioning Setup" style="width: 100%">

<h1>OSiRIS on the Puppet blog</h1>
<a href="https://puppet.com/blog/nsf-puppet-help-osiris-provide-software-defined-storage-research-universities"><img src="{{IMAGE_PATH}}/logos/puppet_logo.png" class="lf" alt="Puppet logo" style="padding-top: 10px;"></a>OSiRIS was featured on the <a href="https://puppet.com/blog/nsf-puppet-help-osiris-provide-software-defined-storage-research-universities">Puppet blog</a> in 2016.  Our project lead engineer discusses how we use Puppet and why we chose it. 
