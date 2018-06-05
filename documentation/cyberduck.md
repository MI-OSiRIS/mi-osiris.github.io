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
* The Access Key ID is your comanage key
* The Password field is ignored, so any value will work.

This is what you should see:

<img src="{{IMAGE_PATH}}/documentation/s3/cyberduck/create_connection_login_info.jpg" />

<h3>Using Cyberduck</h3>
Cyberduck uses the word 'folder' instead of 'bucket'.  Most operations can be done with a right click on a bucket or file.

<img style="width:50%;height:50%;" src="{{IMAGE_PATH}}/documentation/s3/cyberduck/bucket_info.png" />

While not required to change the default upload permissions, it is possible in the Preferences.

<img src="{{IMAGE_PATH}}/documentation/s3/cyberduck/set_permissions.jpg" />

<h3>Setting ACLs</h3>
To set an ACL on a file, right click on the file and select 'info' or use the keyboard combo of 'alt + enter'. ACLs can then be set under the permissions tab.

<img src="{{IMAGE_PATH}}/documentation/s3/cyberduck/acl.jpg" />

<h3>Encryption</h3>
Cyberduck does not support SSE-C encryption.
