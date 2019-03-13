---
layout: default
title : RADOS 
header : Using OSiRIS Ceph RADOS
group: documentation
subnavgroup: documentation
---
{% include JB/setup %}


OSiRIS is built on top of the Ceph object storage cluster.  To leverage Ceph directly you can use <a href="http://docs.ceph.com/docs/master/man/8/rados/">clients that understand rados</a> or you can build applications that use <a href="http://docs.ceph.com/docs/master/rados/api/">librados</a>.

How exactly you might implement librados or leverage a rados client is beyond the scope of this document but we are happy to work with you if you are interested in trying something!  Please note that this service is not generally open to public networks.  If you require access please <a href="mailto:osiris-help@umich.edu">contact us</a>.  

Every COU has a pool named <strong>cou.YourOrg.rados</strong>.  As currently implemented every member of your COU can retrieve a key to read and write to this pool.  We can create other pools for you with more limited access.  


If unsure what your COU name is please look under 'My Profile':

<img style="width: 40%" src="{{IMAGE_PATH}}/documentation/Comanage-person-menu.png" alt="COmanage Identity Menu"/>

Look for 'Role Attributes' to determine your COU memberships and names.  Your Rados pool will be cou.NameOfCou.rados.  

<img style="width: 100%" src="{{IMAGE_PATH}}/documentation/Comanage-role-attr.png" alt="COmanage role attributes"/>

To obtain Ceph client credentials look for 'Ceph Credentials' in the COmanage 'person menu' on the upper-right part of the screen:

<img style="width: 40%" src="{{IMAGE_PATH}}/documentation/Comanage-person-menu-ceph.png" alt="COmanage person menu"/>

Your available Ceph Credentials will be listed, and in this case the relevant credential is "Ceph Client Key"

<img style="width: 100%" src="{{IMAGE_PATH}}/documentation/Comanage-ceph-credentials.png" alt="COmanage Ceph Credentials"/>

You can retrieve a Ceph client key with access to your organization default RADOS-only pool from this page.  You can also download it as ceph.client.osiris.yourid.keyring.  Typically Ceph clients will look for a keyring following this convention in /etc/ceph.  

All users in the organization have full access to this pool.  We can create additional pools as requested with more restricted access.  


