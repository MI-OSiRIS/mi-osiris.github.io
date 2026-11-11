---
layout: default
title: Globus
tagline : Using Globus with OSiRIS CephFS
group: documentation
subnavgroup: documentation
---
{% include JB/setup %}

OSiRIS CephFS storage is accessible using our Globus endpoints.  

<strong>The Globus CephFS endpoints are:</strong>

osiris@um <br />
osiris@wsu <br />
osiris@msu <br />

All have an identical view of the OSiRIS data on CephFS as you also can see via <a href="sshkey.html">ssh/scp</a> access

If you are planning to access OSiRIS via Globus then you will need to go to <a href="https://cilogon.org/">cilogon.org</a> and login with any identity provider.  It does not have to be the same provider used for OSiRIS (but most likely is).  

Send to osiris-help@umich.edu the "Certificate Subject" given to you by CIlogon and request globus access in the email.  The subject will resemble this string:
<pre>
/DC=org/DC=cilogon/O=YourOrg/CN=Your Name A12345
</pre>

Once we have configured your account for Globus access login and transfer data at <a href="https://app.globus.org/file-manager">globus.org</a>. 

Search for 'osiris' and you should see our endpoints:  

<img style="width: 70%" src="{{IMAGE_PATH}}/documentation/globus/Globus-endpoint-search.png" alt="Globus endpoint search"/>

Ignore any endpoints with '#' in the name. They are left for the convenience of some existing users but should not be used going forward.  

<h3>Globus Permissions and Shares</h3>

When you access Globus CephFS endpoints your access is determined by Posix (unix-style) permissions for CephFS.  Please look at information about <a href="groups.html">OSiRIS default groups</a> for more details and how to create additional groups for other OSiRIS-enrolled collaborators.  

Globus also offers Globus Share functionality where you create a share belonging to your identity and choose to share it with other Globus identities or groups.  This is entirely self-managed outside the scope of OSiRIS.  Your Globus share has the same effective permissions in OSiRIS as your identity.  This is a good option for sharing data with Globus-only users since they do not have to enroll in OSiRIS.

Please be aware that Globus Shares are specific to the endpoint you create them on.  You can create a share on all of our endpoints separately.  In this case it is recommended to create a Globus group to manage sharing permissions; you can then use the same group for each share.  

Globus users have to have an available identity through an organization on CIlogon.  If you need to share with someone who is not part of a typical academic institution please point them at <a href="enrollment.html#idp">Non-Institutional Identity Providers</a> on the Enrollment page.  They can establish an identity for CIlogon use and/or OSiRIS enrollment.  

The <a href="https://docs.globus.org/how-to/share-files/">Globus.org website</a> is the best place to learn about Globus shares.

You may want to create <a href="https://docs.globus.org/how-to/managing-groups/">Globus groups</a> to more easily manage your sharing permissions.
