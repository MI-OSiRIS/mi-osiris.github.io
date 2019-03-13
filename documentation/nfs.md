---
layout: default
title : NFS
header : Using OSiRIS NFS
group: documentation
subnavgroup: documentation
---
{% include JB/setup %}

OSiRIS can provide access to your CephFS space via our NFS servers if you are on the MSU or UM campus.  Please email <a href="mailto:osiris-help@umich.edu">osiris-help@umich.edu</a> if interested in using OSiRIS via NFS so we can setup the necessary 'user mapping' from your UMICH or other local user to your OSiRIS identity.  Once configured, files owned by your OSiRIS identity will show as owned by your local (non-osiris) identity when listed in the NFS mount.  Groups will still show as 'nobody' but actual group permissions will be respected as determined by your OSiRIS group memberships.  We can also map selected OSiRIS groups to local groups if there is an appropriate correlation.  

<h2>UMICH</h2>

OSiRIS storage is mounted on flux-login nodes at /nfs/osiris (flux-login.arc-ts.umich.edu).  You will automatically have the requisite Kerberos credentials when you login.  Your virtual organization space will be directly under this path.  For example:  /nfs/osiris/mycouname <br /> 

You can copy from here to other paths mounted on flux-login, or work with the data directly for testing or proof of concept (please do not run compute intensive jobs on the login nodes).  

<h2>MSU</h2>

HPCC users at MSU can access OSiRIS storage on globus-01.hpcc.msu.edu at /mnt/cephfs.  After login you will need to run 'kinit' and enter your password to manually obtain Kerberos credentials.

<h2>Mounting on your own client</h2>

Mounting NFS requires Kerberos credentials.  Your client will require a keytab and users of the space require credentials to verify their identity.

If interested in mounting NFS on your client please send an email to <a href="mailto:osiris-help@umich.edu">osiris-help@umich.edu</a> and OSiRIS admins can obtain a keytab for your client as well as assist with configuration.  We also have to configure a 'user mapping' to map your local system user to your OSiRIS identity.  It is not strictly required but if not setup then your files will all show as owned by the NFS 'nobody' user.  

For reference, the NFS servers are: <br />
um-nfs01.osris.org <br />
msu-nfs01.osris.org <br />

Your client must have rpc.gssd and gssproxyd running.  These should startup automatically if /etc/krb5.keytab exists.  If you have just installed a keytab and need to start them on RHEL7 (or CentOS 7):
<pre>
systemctl start rpc-gssd.service 
systemctl start gssproxy.service  
</pre>

You should also set a default_realm in /etc/krb5.conf under libdefaults.  For example:
<pre>
/etc/krb5.conf:

[libdefaults]
    default_realm = UMICH.EDU
</pre>

On your client system the /etc/idmapd.conf file should have a domain that matches your institution.  At UM that domain is 'umich.edu'.  At MSU that domain is 'hpcc.msu.edu'.  For example:
<pre>
/etc/idmapd.conf:

[General]

  # The default is the host's DNS domain name.
  Domain = umich.edu

</pre>

A typical mount command might look like this:
<pre>
mount -t nfs4 -o sec=krb5,nfsvers=4.1,noacl um-nfs01.osris.org:/cephfs /mnt/cephfs/
</pre>

Or in fstab:
<pre>
um-nfs01.osris.org:/cephfs /mnt/cephfs nfs sec=krb5,nfsvers=4.1,noacl,_netdev,rw 0 0
</pre>

