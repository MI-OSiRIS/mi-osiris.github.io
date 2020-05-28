---
layout: default 
title: FACL
tagline : Managing file permissions using File Access Control Lists (FACLs)
group: documentation
subnavgroup: documentation
---
{% include JB/setup %}

The OSiRIS filesystem manages file permissions using access control lists or acl's to further protect files and directories. Thus, standard unix file permissions might not be enough to manage file access for users/groups.

<strong> Why do we need FACL(s)? </strong>

Every file in a UNIX system has a owner/group and a set of permissions attached to it. ACLs are used in OSiRIS to provide access to files for multiple users who are from different groups. The file system access control lists(FACLs) are the list of additional users/groups and their respective permissions to the file.

<strong> Viewing FACL(s) </strong>

To display ACL details, filename, owner, group for each file we use the getfacl command. If a directory has a default ACL, getfacl also displays the default ACL. Non-directories cannot have default ACLs. If getfacl is used on a file system that does not support ACLs, getfacl displays the access permissions defined by the traditional file mode permission bits.
<pre>
getfacl /osiris/test

output:
#file : test
#owner: root
#group : CO_COU_NavalOceanics_members_active
user::rw-
user:abc:r--
user:xyz:rwx
group::r--
group:CO_COU_Test_members_active:r-x
mask::r--
other::---
</pre>

Notice 3 different user lines in the output above. Thefirst line lists the standard file permissions of the owner of the file. The two other user permissions are the individual permissions for the users abc and xyz. The mask field defines the maximum effective file permissions for other groups and users. The default group permissions are read only as seen above. Group CO_COU_Test_members_active has been granted read(r) and execute(x) [r-x] permissions exclusively . Other users/groups do not have any permissions.

<strong> Creating and Managing FACL(s) </strong>

The setfacl command is used to set ACL for a given file. Even if a group is provided write permissions using standard unix chmod command, the members of the group would not be able to write to the /osris/test/ directory because the mask has been set to r-- as seen in the section above.

To override the mask the best way is to give exclusive permissions to that particular user/group to the file/directory. In our case we will provide exclusive read write[rw] access for CO_COU_NavalOceanics_members_active group to the /osris/test directory by running the command below:
<pre>
setfacl -m g:CO_COU_NavalOceanics_members_active:rw /osris/test
</pre>

The -m option tells setfacl to modify ACLs on the file(s) mention in command line.

<strong> Masking </strong>

To access control list (ACL) mask defines the maximum effective permissions for any entry in the ACL. This mask is applied automatically everytime you execute the setfacl or chmod commands.
You can prevent masking by using the --no-mask flag in your command as shown below:
<pre>
setfacl --no-mask -m u:xyz:7 /osiris/test.txt
</pre> 

<strong> Backing up the FACL(s) </strong>

Many a times, the backup software may not copy the metadata related to the FACL on the files. In that case you may want to backup the FACL information on the files or directory. To copy the FACL on all the files in a directory , including all sub directories to a single file run :
<pre>
cd /osiris
getfacl -R * > osiris_facl
</pre>

The above commands will get the access control lists for all subdirectories and files under the osiris directory and write it to the osiris_facl file

<strong> Restoring the FACL(s) </strong>

When you restore the files in /osiris directory, you would have to restore the FACLs associated with the files in that direcotry. To do that use the FACL backup file osiris_facl along with the –restore option :
<pre>
setfacl --restore=osiris_facl
</pre>

To learn more about file system access control lists please refer to <a href="http://linux-training.be/storage/ch03.html">this website</a>
