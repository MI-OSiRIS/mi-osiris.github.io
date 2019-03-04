---
layout: default
title : Creating and Uploading an SSH key
header : Creating and Uploading an SSH key
---
{% include JB/setup %}

To use ssh/scp/sftp login to OSIRIS xfer nodes you must use an SSH keypair.  

Your ssh key should work to login to the following nodes which have the OSiRIS CephFS mounted at /osiris.  Your COU will have a directory named the same as your COU but in lowercase (/osiris/mycou).  

um-xfer01.osris.org <br />
wsu-xfer01.osris.org <br />
msu-xfer01.osris.org <br />

<h2>Generating a keypair</h2>

If you do not already a key use ssh-keygen to generate one. 
<font style="font-weight: bold">Do not leave the passphrase blank.</font>The only exception is if you must use the key in an automated process.  We recommend generating a 2nd key used only for this purpose if that is the case.  You can upload as many keys as you like to OSiRIS.  
<pre>
[user@host ~]$ ssh-keygen 
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
 
Your identification has been saved in /home/user/.ssh/id_rsa.
Your public key has been saved in /home/user/.ssh/id_rsa.pub.
</pre>

Keep the 'id_rsa' file private and protected.  The contents of id_rsa.pub will be uploaded to OSiRIS.  

<h2>Uploading public key to OSiRIS</h2>

After your OSiRIS enrollment has been approved login to <a href="https://comanage.osris.org">OSiRIS COmanage</a>.  Open your identity using the Person menu at the upper right:


<img style="width: 50%" src="{{IMAGE_PATH}}/documentation/Comanage-person-menu.png" alt="COmanage Identity Menu"/>

Scroll down.  You will see a section for 'ssh keys'.  Click on Add.   You can add multiple keys by repeating this process.

<img style="width: 80%" src="{{IMAGE_PATH}}/documentation/sshkey/Comanage-ssh-add.png" alt="COmanage SSH key add button"/>

On the following screen you can specify an ssh keyfile to upload.  This will be the id_rsa.pub file created in the example.  You will  have to copy this file to your computer if it was created on another machine.  Be sure to only copy and upload the .pub file - the other id_rsa or id_dsa file should remain private.  

<img style="width: 70%" src="{{IMAGE_PATH}}/documentation/sshkey/Comanage-ssh-upload.png" alt="COmanage SSH key upload screen"/>

Once attached to your identity you can login to one of the xfer gateways noted above.  Note that your username can be found under Identifiers on the same 'My OSiRIS Identity' page.
<img style="width: 80%" src="{{IMAGE_PATH}}/documentation/Comanage-identifiers.png" alt="COmanage identifiers"/>

So for this example the user name is 'eben':
<pre>
ssh eben@um-xfer01.osris.org
</pre>




