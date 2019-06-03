---
layout: default
title : AWSCLI
tagline: Using AWS CLI with OSiRIS S3
header : AWSCLI
---
{% include JB/setup %}

AWS CLI is a tool provided by Amazon for command line interaction with various services that they offer.  In the context of OSiRIS it can be used to interact with OSiRIS S3 storage.  Easy to use bundled installers with no dependencies are provided.  Our own S3 <a href="s3fuse.html">fuse client bundle</a> installs awscli during setup to facilitate listing and creating buckets.  

<h2>Installation</h2>

You can install awscli with Python Pip or you can install a standalone bundle.  The bundle includes everything required to run awscli and has no external dependencies except Python.  

For complete installation instructions the best reference is the original documentation:  
<a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html">https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html</a>

Here is an example of using the bundled installer.  You would then run it using ~/bin/aws.  You could put ~/bin into your PATH variable as well.  
<pre>
curl -s "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
unzip -q awscli-bundle.zip

./awscli-bundle/install -b ~/bin/aws
</pre>

The installer also accepts -i to specify an installation directory (default is ~/.local/lib/aws)

Alternately, if you download the <a href="https://github.com/MI-OSiRIS/osiris-bundle/releases/latest/download/osiris-bundle.tgz">OSiRIS client bundle</a> and run the setup script then awscli will be installed at ~/osiris-bundle/awscli/bin/aws.  The OSiRIS setup script will also configure a credentials file.  The userid you specify will be used as the profile (given to --profile argument to aws utility).  You can change it to 'default' to avoid specifying it.  If you do so and are also using the osiris-mount utility please change the AWSPROFILE setting in ~/osiris-bundle/osiris-config (only relevant for our osiris-mount command, awscli does not use this file).    

<h2>Using AWSCLI with OSiRIS S3</h2>

<ol class="bolditem">
<li>
    <p>
        <span>Create credentials file: </span> The awscli utility can be used to setup your credential file:
    </p>
<pre>
/bin/aws configure set aws_access_key_id ABC234
/bin/aws configure set aws_secret_access_key Abc123
</pre>
<p>
    The userid, access key, and secret key are available from <a href="https://comanage.osris.org">OSiRIS COmanage</a>.  The credentials will be placed under the 'default' profile.  If you wish to have multiple profiles for different credentials use the --profile= option to point to different configuration profiles.
</p>

<p>The resulting file looks like this (you can also create it manually):</p>
<pre>
# ~/.aws/credentials 
[default]
aws_access_key_id = ABC234
aws_secret_access_key = Abc123
</pre>  
</li>
<li>
    <p>
        <span>Use the utility: </span> You need to specify the correct endpoint argument to the aws utility to use OSiRIS S3.  If you have multiple credential profiles use the --profile= option to specify which one (otherwise 'default' is used).  Examples:
    </p>
<pre>
# list your S3 buckets
~/bin/aws s3 --endpoint-url https://rgw.osris.org ls"

# make a new S3 bucket
~/bin/aws s3 --endpoint-url https://rgw.osris.org mb s3://yourcou-bucketname"
</pre>
</li>
