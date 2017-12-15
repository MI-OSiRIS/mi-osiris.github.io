---
layout: default
title : Enrolling in OSiRIS
header : Enrolling in OSiRIS
---
{% include JB/setup %}
Introduction:
OSiRIS is a storage infrastructure for research universities for the state of Michigan. The main objective of OSiRIS is to manage data collection, storage, and sharing between Universities.  
To get started using OSiRIS the first requirement is to establish an identity.  This identity is based on authentication with your existing institutional credentials.  Your OSiRIS identity can be linked to one or more OSiRIS virtual organizations.

<h3>Getting started</h3>

You can enroll at this URL:  <a href="https://comanage.osris.org/enroll">https://comanage.osris.org/enroll</a>

Your institutional identity will be used to login.  The beginning screen prompts users to choose an organization, for example, the University of Michigan. 

<img style="width: 50%" src="{{IMAGE_PATH}}/documentation/enrollment/Comanage-institution-selector.png" alt="COmanage institution selection screen"/>

If this is your first time logging into OSiRIS from your organization you may be asked to agree to release information to us.  The information released includes email, affiliation, and full name.  This is required to login and use OSiRIS.  

<img style="width: 50%" src="{{IMAGE_PATH}}/documentation/enrollment/Login-information-consent.png" alt="Example of information consent"/>

Generally you'll want to just send it automatically in the future (though the choice is up to you if you prefer to be asked every time).

You'll be asked to enter some basic information about yourself.  Make sure to enter a valid email, this will be used to verify your enrollment.  You should choose your virtual organization, or "COU" on this enrollment information page.  

<img style="width: 70%" src="{{IMAGE_PATH}}/documentation/enrollment/Comanage-user-signup.png" alt="COmanage enrollment information screen"/>

After submitting the form you'll see a confirmation that says 'Petition Created'.  It is normal at this point to see a notice that your identifier is not registered.

<img style="width: 100%" src="{{IMAGE_PATH}}/documentation/enrollment/Comanage-post-enroll.png" alt="COmanage post enrollment message"/>

Check your email at this point and look for a message from Comanage with subject "Invitation to Join OSiRIS" containing a link to verify your enrollment.  

<img style="width: 80%" src="{{IMAGE_PATH}}/documentation/enrollment/confirmationEmail.png" alt="COmanage confirmation email"/>

After you have verified your email an OSiRIS administrator or your virtual organization administrator will approve your enrollment.  Another email will be sent.

<font style="font-weight: bold">IMPORTANT:</font>  At this point you need to login to comanage again to refresh your capabilities.  You can use the link from the comanage "not registered" message or <a href="https://comanage.osris.org/registry/auth/login" target="_new">click here</a> to open the comanage login page in a new window.  

Once logged in there will be a screen to select collaboration.  Please click on 'OSiRIS'.

<img style="width: 70%" src="{{IMAGE_PATH}}/documentation/enrollment/Comanage-collaborations.png" alt="COmanage collaboration screen"/>

You can now retrieve authentication tokens such as your Ceph client key or S3 access token.  At this time only the S3 access token is likely to be useful to you.

<img style="width: 70%" src="{{IMAGE_PATH}}/documentation/enrollment/Comanage-person-menu.png" alt="COmanage collaboration screen"/>

Initially the token will not exist, you must click the "Generate Token" button to generate the token:

<img style="width: 80%" src="{{IMAGE_PATH}}/documentation/enrollment/Comanage-token-none.png" alt="COmanage tokens before being generated"/>
<br />
<img style="width: 80%" src="{{IMAGE_PATH}}/documentation/enrollment/Comanage-token-generated.png" alt="COmanage token screen after generating S3 token"/>

The CephRgwToken access token string should be used for the "access key" in your S3 client, leaving "secret key" field blank. If your client does not accept an empty secret key any value is fine - it is ignored.  

<h3>Non-Institutional Users</h3>

If you do not belong to an institution/group which is part of the <a href="https://www.incommon.org/">InCommon Federation</a> you can still authenticate to OSiRIS using one of the 'public' identity providers below.  After establishing an account at one of these providers use that provider to login to OSiRIS Comanage.

<ul>
    <li><a href="https://go.ncsa.illinois.edu/idp-guest">National Center for Supercomputing Applications</a> </li>
    <li><a href="https://app.unitedid.org/signup/">UnitedID</a></li>
</ul>


