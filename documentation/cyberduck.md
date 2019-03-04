---
layout: default
title : Using CyberDuck
tagline: Open Storage Research Infrastructure
header : s3cmd
---

{% include JB/setup %}

<h3>Getting Cyberduck</h3>
Cyberduck can be downloaded from their [website](https://cyberduck.io/). You do not have to donate to use Cyberduck. Follow the Installer to get Cyberduck installed correctly on your machine.

<h3>Connect to the OSIRIS server</h3>
The following information should be used for connecting to OSiRIS.

* The server is `rgw.osris.org`.
* The Access Key ID is the 'access_key' from your <a href="https://comanage.osris.org">Comanage Ceph Credentials</a>
* When you open the connection you'll be asked for the 'secret_key' also found in Comanage Ceph credentials.

<img style="width:50%;" src="{{IMAGE_PATH}}/documentation/s3/cyberduck/create_connection_login_info.png" />

<h3>Using Cyberduck</h3>
Cyberduck uses the word 'folder' instead of 'bucket'.  Most operations can be done with a right click on a bucket or file.

<img style="width:50%;" src="{{IMAGE_PATH}}/documentation/s3/cyberduck/bucket_info.png" />

While not required to change the default upload permissions, it is possible in the Preferences.

<img src="{{IMAGE_PATH}}/documentation/s3/cyberduck/set_permissions.jpg" />

<h3>Setting ACLs</h3>
To set an ACL on a file, right click on the file and select 'info' or use the keyboard combo of 'alt + enter'. ACLs can then be set under the permissions tab.  You want to use 'Canonical User ID' to identity other OSiRIS users, or Everyone.  It could also refer to a user id that you have created for yourself on the Ceph credentials page.  

<img style="width:60%;" src="{{IMAGE_PATH}}/documentation/s3/cyberduck/acl.png" />

The Canonical User ID will match the User ID shown in the Ceph credentials page:  

<img style="width: 50%" src="{{IMAGE_PATH}}/documentation/Comanage-ceph-credentials.png" alt="COmanage person menu"/>



You may have to ask other users in your organization to lookup their user id for you, or if you are an admin for your OSiRIS virtual org you can see their primary user id by finding that person under the "People" menu in Comanage.  They may have created others but everyone has at least a user id matching the OSiRIS UID identifier:

<img style="width: 50%" src="{{IMAGE_PATH}}/documentation/Comanage-identifiers.png" alt="COmanage identifiers"/>


<h3>Encryption</h3>
Cyberduck does not support SSE-C encryption.

<h3>More Information</h3>

More <a href="/documentation/s3.html">OSiRIS S3 Documentation</a>
