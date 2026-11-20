---
layout: default
title : Groups
tagline: Managing OSiRIS Groups
header : OSiRIS Groups
group: documentation
subnavgroup: documentation
---
{% include JB/setup %}

In the following page we'll describe how unix groups work in OSiRIS, what the default group memberships are, and how to create new groups.

These instructions apply only to Unix/Posix style access to OSiRIS storage (not S3).  They may be relevant if you are using Globus, ssh/sftp/scp, or NFSv4 mounts.  

If you are using Globus shares to provide access to other collaborators outside OSiRIS then they only apply so far as your own group memberships and file access.  Globus shares act as the user that created them.  You may not need to do anything with these permissions if you are using only Globus shares to manage permissions and access. 

<h2>Default Groups</h2>
In OSiRIS everybody is a member of virtual organizations known as "COU"  (COmanage Organizational Unit).  

When you are initially approved for <a href="enrollment.html">enrollment</a> into an OSiRIS COU you are automatically made a member of a special group:
<pre>CO_COU_YourCouName_members_active</pre>   
By default this group will have Read-only privileges to your OSiRIS storage and any new folders you create under your OSiRIS storage.

Additionally, if you are marked as a 'COU Admin' you will also be a member of another special group:
<pre>CO_COU_YourCouName_admins</pre>
By default this group will have Read-write privileges to your OSiRIS storage and new folders you create.  

Generally during initial discussions about using OSiRIS you would designate one or more people to be admins for your group and we would put them into the appropriate group.  Once you have at least 1 admin that person can mark additional people as admins.  

You are not limited to these two groups.  They are intended as reasonable defaults.  

It may be helpful to see the permissions from a unix command line perspective. 

<pre>
[user@um-xfer01 ~]$ ls -l /osiris
drwxrws--- 1 root     CO_COU_TestCOU_admins               1 Mar 26 15:50 testcou
</pre>

As you can see, the directory setup for 'TestCOU'  has rwx permissions for the CO_COU_TestCOU_admins group.  It is set 'sticky' so new folders retain those permissions and ownership.   

<pre>
[user@um-xfer01 ~]$ mkdir /osiris/testcou/testdir

[user@um-xfer01 ~]$ ls -l /osiris/testcou
drwxrws--- 1 user CO_COU_TestCOU_admins 0 Mar 26 15:50 testdir
</pre>

We use posix ACLs to allow COU members RO permissions, and you can also <a href="https://wiki.archlinux.org/index.php/Access_Control_Lists#Set_ACL" target='_new'>use them yourself</a> to assign more granular permissions to folders/files.  

<pre>
[user@um-xfer01 ~]$ getfacl /osiris/testcou/

... cut ...

default:group:CO_COU_TestCOU_members_active:r-x
    
</pre>

Whether you access your CephFS directory via Globus, scp, or NFS these permissions are in effect.  When you create a Globus share you are responsible for permissions on that share - it has the same effective permissions that you have.

<h2>Managing groups</h2>

Groups are managed in COmanage, at <a href="https://comanage.osris.org">https://comanage.osris.org</a>. (Until November 2026 they were managed in a separate tool, Grouper, which has been retired.)

- Log in to COmanage with your institution's account and choose **Groups** in the menu. You see the groups you belong to, including the default groups described above. In COmanage their names use colons, for example <code>CO:COU:YourCouName:members:active</code>; on OSiRIS systems the colons become underscores (<code>CO_COU_YourCouName_members_active</code>). COmanage keeps the default groups up to date, so don't edit them.
- To create a group, choose **Add Group**, give it a short name and a description, and save. The name becomes the Unix group name, so use only letters, digits, <code>-</code> and <code>_</code>, with no spaces.
- Open the group and add members. These are usually people in your own COU, but anyone enrolled in OSiRIS can be added.
- COmanage passes the change to the OSiRIS directory right away, and OSiRIS systems see it within about a minute. Log in again to see a new group in a shell.

If you can't create a group or add someone, ask your COU admin or write to <a href="mailto:osiris-help@umich.edu">osiris-help@umich.edu</a>.

Once the group exists you can use it in shell commands. For example, you could create a folder and make 'mynewgroup' the owner so that anyone you put in 'mynewgroup' can write in that folder.
<pre>
    cd /osiris/testcou
    mkdir myfolder
    chgrp mynewgroup myfolder
    chmod g+rwx myfolder

    ls -l

    drwxrws--- 1 user mynewgroup 0 Mar 26 15:50 myfolder
</pre>

Inside a shell use the unix 'id' command to see what groups you are in. They match your groups in COmanage, with underscores in place of colons.
<pre>
[user@um-xfer01 testcou]$ id

uid=99999(user) gid=99999(user) groups=99999(user),123456(CO_COU_TestCOU_admins),1234567(CO_COU_TestCOU_members_active),12345678(CO_COU_TestCOU_members_all)
</pre>
