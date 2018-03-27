---
layout: default
title : Enrolling in OSiRIS
header : Enrolling in OSiRIS
---
{% include JB/setup %}
OSiRIS is a storage infrastructure for research universities for the state of Michigan.  Users of OSiRIS belong to virtual organizations which are called 'COU' within OSiRIS.  

There are 3 supported data storage protocols available:
 <ul>
    <li>S3 - The S3 protocol is best known from Amazon S3 services.  This is a well established ecosystem with many compatible clients.  S3 is based on simple http operations such as GET / PUT / HEAD / DELETE.  You will need to set appropriate bucket ACLs if you wish to share data with other OSiRIS S3 users inside or outside your org.  You may also see this referred to as 'Ceph Rados Gateway' or 'RGW'.
    </li>
    <li>
    CephFS - This is a typical Posix/unix style filesystem which we provide to you via Globus or via ssh/scp gateways at /osiris/yourcou.  For our primary OSiRIS member campuses we can also setup an NFSv4 export for you to mount on campus. 
    </li>
    <li>
    RADOS - Direct access to Ceph object store.  Your organization will have a data pool called cou.YourOrg.rados.  This access method requires a <a href="http://docs.ceph.com/docs/master/rados/api/librados-intro/">rados</a> client or library.  If necessary we can configure additional pools.  We will have to work with you to open network access to your client(s) to use this method although OSiRIS member campuses will already be able to reach the requisite services. 
    </li>  
</ul>

Please be aware that S3 and CephFS do not share the same data backend.  Data you store in CephFS is not visible in S3 nor the reverse.  There is no requirement to use only one or the other protocol exclusively - you may use both protocols to store data on OSiRIS.  

To get started using OSiRIS the first requirement is to establish an identity.  This identity is based on authentication with your existing institutional credentials.  Your OSiRIS identity can be linked to one or more OSiRIS virtual organizations.

<h3>Getting started</h3>

You can enroll at this URL:  <a href="https://comanage.osris.org/enroll">https://comanage.osris.org/enroll</a>

Your institutional identity will be used to login.  The beginning screen prompts users to choose an organization, for example, the University of Michigan. 

<img style="width: 60%" src="{{IMAGE_PATH}}/documentation/enrollment/Comanage-institution-selector.png" alt="COmanage institution selection screen"/>

If this is your first time logging into OSiRIS from your organization you may be asked to agree to release information to us.  The information released includes email, affiliation, and full name.  This is required to login and use OSiRIS.  

<img style="width: 60%" src="{{IMAGE_PATH}}/documentation/enrollment/Login-information-consent.png" alt="Example of information consent"/>

Generally you'll want to just send it automatically in the future (though the choice is up to you if you prefer to be asked every time).

You'll be asked to enter some basic information about yourself.  Make sure to enter a valid email, this will be used to verify your enrollment.  You should choose your virtual organization, or "COU" on this enrollment information page.  

<img style="width: 80%" src="{{IMAGE_PATH}}/documentation/enrollment/Comanage-user-signup.png" alt="COmanage enrollment information screen"/>

After submitting the form you'll see a confirmation that says 'Petition Created'.  It is normal at this point to see a notice that your identifier is not registered.

<img style="width: 100%" src="{{IMAGE_PATH}}/documentation/enrollment/Comanage-post-enroll.png" alt="COmanage post enrollment message"/>

Check your email at this point and look for a message from Comanage with subject "Invitation to Join OSiRIS" containing a link to verify your enrollment.  

<img style="width: 80%" src="{{IMAGE_PATH}}/documentation/enrollment/confirmationEmail.png" alt="COmanage confirmation email"/>

After you have verified your email an OSiRIS administrator or your virtual organization administrator will approve your enrollment.  Another email will be sent.

<font style="font-weight: bold">IMPORTANT:</font>  At this point you need to login to comanage again to refresh your capabilities.  You can use the link from the comanage "not registered" message or <a href="https://comanage.osris.org/registry/auth/login" target="_new">click here</a> to open the comanage login page in a new window.  

Once logged in there will be a screen to select collaboration.  Please click on 'OSiRIS'.

<img style="width: 70%" src="{{IMAGE_PATH}}/documentation/enrollment/Comanage-collaborations.png" alt="COmanage collaboration screen"/>

<h3>What Next?</h3>

To access OSiRIS CephFS with ssh/scp/sftp you need to <a href="sshkey.html">upload an SSH key</a>. 

To use OSiRIS CephFS with Globus please see the <a href="globus.html">globus instructions</a>.  

To access OSiRIS S3 please see the <a href="s3.html">S3 instructions</a>.  

To access OSiRIS Rados please see the <a href="rados.html">Rados instructions.  


<h3>Who needs to enroll</h3>

Depending on how you share data you may not need to enroll every person you collaborate with.  

For ssh/scp/sftp access:  Every user needing to login and read data must enroll and upload an ssh key.

For Globus access:  A single user can configure Globus shares accessible by Globus users or groups.  The other users do not need to enroll in OSiRIS, they only need to be able to login to Globus with CIlogon and be allowed to access your share.  Please have a look at the <a href="https://docs.globus.org/how-to/share-files/">Globus.org documentation</a> for information.

For S3 access:  Every user needing to login via S3 needs to enroll into OSiRIS.  You will need to configure bucket ACLs to share your data buckets with other users.  This is described in the <a href="s3.html">S3 instructions</a>.

For RADOS access:  Every user needing to access RADOS services will need to enroll in OSiRIS.  However, in many cases it is typical to build another service on top of RADOS rather than providing direct user access (much like S3 and CephFS are themselves services on top of RADOS).  Please let us know if you have some ideas for leveraging RADOS directly and we'll be happy to work with you.  

<h3>Non-Institutional Users<a name="idp"></a></h3>

If you do not belong to an institution/group which is part of the <a href="https://www.incommon.org/">InCommon Federation</a> you can still authenticate to OSiRIS using one of the 'public' identity providers below.  After establishing an account at one of these providers use that provider to login to OSiRIS Comanage.

<ul>
    <li><a href="https://go.ncsa.illinois.edu/idp-guest">National Center for Supercomputing Applications</a> </li>
    <li><a href="https://app.unitedid.org/signup/">UnitedID</a></li>
</ul>

<h3>What is my COU?</h3>

If unsure what your COU name is please look under the 'person menu' on the upper-right of COmanage and click 'My OSiRIS Identity'.  Under 'Role Attributes' you can see the COU you are in.  You may be in several.  

<img style="width: 100%" src="{{IMAGE_PATH}}/documentation/Comanage-role-attr.png" alt="COmanage role attributes"/>

