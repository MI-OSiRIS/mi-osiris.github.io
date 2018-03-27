---
layout: default
title : Using OSiRIS Ceph RADOS 
header : Using OSiRIS Ceph RADOS
---
{% include JB/setup %}


OSiRIS is built on top of the Ceph object storage cluster.  To leverage Ceph directly you can use <a href="http://docs.ceph.com/docs/master/man/8/rados/">clients that understand rados</a> or you can build applications that use <a href="http://docs.ceph.com/docs/master/rados/api/">librados</a>.

How exactly you might implement librados or leverage a rados client is beyond the scope of this document but we are happy to work with you if you are interested in trying something!  

Every COU has a pool named <strong>cou.YourOrg.rados</strong>.  As currently implemented every member of your COU can retrieve a key to read and write to this pool.  We can create other pools for you with more limited access.  

If unsure what your COU name is please look under 'My OSiRIS Identity':

<img style="width: 50%" src="{{IMAGE_PATH}}/documentation/Comanage-identity-menu.png" alt="COmanage Identity Menu"/>

<br />

<img style="width: 100%" src="{{IMAGE_PATH}}/documentation/Comanage-role-attr.png" alt="COmanage role attributes"/>


You can retrieve a Ceph client key with access to your organization default RADOS-only pool from COmanage:

<img style="width: 40%" src="{{IMAGE_PATH}}/documentation/Comanage-token-menu.png" alt="COmanage token menu"/>

Put this key into your client keyring.  You can also download a file suitable for directly referencing with your client.

<img style="width: 100%" src="{{IMAGE_PATH}}/documentation/Comanage-cephkey.png" alt="COmanage ceph key on service token page"/>


