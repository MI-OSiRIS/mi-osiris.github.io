---
layout: default
title : Documentation
group: navigation
order: 7
subnavgroup: documentation
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

<p>
<a href="encryption.html">Using S3 SSE-C:</a>
How to use S3 Server Side Encryption with client provided keys.  
</p>

<h3>Architectural Documentation</h3>

If you are interested in how OSiRIS is structured or in creating a deployment similar to OSiRIS please have a look at the <a href="/components">OSiRIS technology components documentation</a> and OSiRIS white paper.

<h3>OSiRIS Whitepaper</h3>

A reference paper is available for OSiRIS.  The paper provides a general overview of the process and components involved in deploying OSiRIS.  This version of the paper is a public draft eventually planned for submission to relevant publications.   

<a href="/documentation/OSiRIS-Whitepaper.pdf">OSiRIS-Whitepaper.pdf</a>



