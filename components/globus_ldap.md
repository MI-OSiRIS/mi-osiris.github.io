---
layout: default
title : Globus LDAP Callout
tagline : Installation and Use
subnavgroup: components
group: components
---
{% include JB/setup %}
<h3>Purpose</h3>
Globus can be configured to use <a href="https://www.cilogon.org/">CIlogon</a> for authentication.  After the user authenticates to CILogon via their identity provider the Globus server receives from CILogon a certificate Distinguished Name (DN) unique to the user.  We can then map this DN to a local unix user. 

Typically Globus uses a 'grid-mapfile' with lines specifying a DN to username mapping.  At one time in OSiRIS we generated this file from user DN stored in our LDAP directory.  At the time of this writing we use the module described here to directly lookup DN from LDAP and do not use a Globus grid-mapfile.  

To store certificate DN in LDAP we use the voPerson schema and DS389 LDAP server.  The schema defines many attributes useful for identities in a virtual organization:  <a href="https://voperson.org/">voperson.org</a>


<h3>Set up</h3>
Before beginning setup, install Globus by following the <a href="https://docs.globus.org/globus-connect-server-installation-guide">Globus installation guide</a>. 


To simplify troubleshooting we recommend you have a functional Globus installation before trying to configure and use this module.  


The steps below will help guide you to build your LDAP module for use.
<ol>
    <li>
        Clone <a href = "https://github.com/MI-OSiRIS/globus-toolkit">https://github.com/MI-OSiRIS/globus-toolkit</a>
<pre>git clone https://github.com/MI-OSiRIS/globus-toolkit
cd globus-toolkit</pre>
</li>
    <li>
    Initialize the repository:
<pre>autoreconf -i
./configure</pre>
    </li>
    <li>
        Build the LDAP module:
        <pre>make globus_gridmap_ldap_callout</pre>
    </li>
    <li>
        Copy the .so file from gsi/gridmap_ldap_callout/.libs/libglobus_gridmap_ldap_callout.so to /usr/local/lib64/ or a location of your choice.
    </li>
    <li>
        Set LDAP module configurations and certifications in /etc/grid-security/gsi-authz.conf:
        <pre>globus_mapping  /path/to/libglobus_gridmap_ldap_callout.so globus_gridmap_ldap_callout ENV:LDAP_SERVER="ldaps://ldap.example.org" LDAP_ROOT="ou=People,dc=example,dc=org"</pre>
        The module does a certificate dn attribute query to find a matching certificate dn for Globus credentials.
    </li>
    <li>
        In Globus /etc/globus-connect-server.conf, set IdentityMethod to CIlogon and AuthorizationMethod to Gridmap. 
<pre>IdentityMethod = CILogon
AuthorizationMethod = Gridmap</pre>
</li>
<li>
        If the LDAP module fails to find the CILogon DN it will fall back to the Gridmap authorization defined in the server config file and handled by the usual bundled Globus modules.   
    </li>
    <li>
        If anything had to be changed in the globus-connect-server.conf file run the 'globus-connect-server-setup' script again.   
    </li>
</ol>

<h3>LDAP Options</h3>
Additional optional variables that can be set in the LDAP module config file. Note only read attributes are required as the search query only reads LDAP entries.
<ul>
    <li>
        <b>LDAP_BIND_DN, LDAP_BIND_PASSWORD</b> <br />
        LDAP_BIND_DN is a username and the LDAP_BIND_PASSWord is the password. If login fails, the module defaults to gridmap_lookup.
    </li>
    <li>
        <b>UID_ATTRIBUTE</b> <br />
        The User ID attribute defaults to "uid". This is the attribute which the module will return from the ldap entry it finds through the search query.
    </li>
    <li>
        <b>LDAP_CERT_DN_ATTRIBUTE</b> <br/>
        The LDAP certificate dn attribute marks the ldap attribute containing the certificate dn string.
    </li>
    <li>
        <b>LDAP_OBJECT_CLASS</b> <br/>
        The LDAP object class defaults to * (searches for anything). This limits the search to only objects whose object class attribute is equal to the object class paramater. 
    </li>
    <li>
        <b>LOGFILE</b> <br />
        The logfile is the path to the debugging output is unintended for regular use. It is over-written on each invocation of the module.
    </li>
</ul>

<h3>Additional Information</h3>
<p>
This module has been tested to work with RPM-based installation on RHEL7 (globus-connect-server-4.0.59-1.el7+gt6, globus-gridftp-server-12.19-1.el7+gt6).
</p>
<p>
The original globus Github repository can be found <a href = "https://github.com/globus/globus-toolkit">here</a>. 
</p>
<p>
 If you are using CILogon only to authenticate users for your institution then you most likely don't need to do this.  You can configure Globus to use only a specific identity provider.  Globus will use the unqualified username portion of the EPPN (username@my.edu without @my.edu) which will in many cases be the same as what is used to authenticate to campus systems.  The configuration described here is targeted at projects needing to map user identities from many institutions.  
</p>
