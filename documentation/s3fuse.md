---
layout: default
title : s3fs-fuse
tagline: Using S3 Fuse to mount S3 storage
header : Using S3 fuse 
---
{% include JB/setup %}

s3fs-fuse mounts your OSiRIS S3 buckets as a regular filesystem (File System in User Space - FUSE).  Using it requires that your system have appropriate packages for FUSE installed:  fuse, fuse-libs, or libfuse on Debian based distributions of linux.  

On Mac OSX you can use Homebrew to install s3fs and the fuse dependency.  

Detailed instructions for installation or compilation are available from the s3fs Github site:  
<a href="https://github.com/s3fs-fuse/s3fs-fuse">https://github.com/s3fs-fuse/s3fs-fuse</a>

s3fs-fuse does not require any dedicated S3 setup or data format.  It can be used in combination with any other S3 compatible client.  

<h2>OSiRIS s3fs bundle</h2>

Linux users have the option of using our s3fs bundle.  The bundle includes s3fs packaged with AppImage so it will work on any Linux distribution.  It also includes a setup script and wrapper script that passes all the correct parameters to s3fuse for mounting.   The wrapper will automatically mount all of your buckets or allow you to specify a single one, and it can also create a new bucket for you.  

The latest release is available for <a href="https://github.com/MI-OSiRIS/osiris-bundle/releases/latest/download/osiris-bundle.tgz">download from our Github site</a>.

<h3>Example s3fs bundle usage:</h3>

Download the bundle:

    curl -L --output osiris-bundle.tgz \
    https://github.com/MI-OSiRIS/osiris-bundle/releases/latest/download/osiris-bundle.tgz

Untar into your home directory:

    cd ~ && tar -xvzf osiris-bundle.tgz

Run the setup tool:

    ~/osiris-bundle/osiris-setup.dist

You will be prompted for your OSiRIS Virtual Organization (aka COU), an S3 userid, and S3 access key / secret.  This information is available from <a href="https://comanage.osris.org">OSiRIS COManage</a>.  Look under your User Menu at the upper right for Ceph Credentials and My Profile to determine your credentials and COU.  

Mount your buckets.  If you have not created any the tool will create one for you:

    ~/osiris-bundle/osiris-mount

When you are finished unmount:

    ~/osiris-bundle/osiris-mount -u

Optionally you can specify a bucket and have it created:
    
    ~/osiris-bundle/osiris-mount -n mycou-anyname

Buckets should be all lowercase and must be prefixed with your COU (virtual organization) or the request will be denied. 

<h2>Using s3fs-fuse</h2>

Using the OSiRIS bundle is not required to use s3fs-fuse.  To setup and use manually:  

<ol class="bolditem">
<li><p>
    <span>Setup Credential File</span> - s3fs-fuse can use the same credential format as AWS under ${HOME}/.aws/credentials.  You can download a file in this format directly from <a href="https://comanage.osris.org">OSiRIS COmanage</a> or paste your credentials from COmanage into the file:
</p>
<pre>
[default]
    aws_access_key_id = 82VA...
    aws_secret_access_key = 665WhlOM...
</pre>
<p>
    You can have multiple blocks with different names.  They can be specified with the -o profile= option to s3fs.  If no profile option is specified the 'default' block is used.  The setup script in the OSiRIS bundle also will create this file based on your input.  
</p>
<p>
    Also be sure your credential file is only readable by you:
</p>
<pre>
chmod 0600 ~/.aws/credentials
</pre>
</li>

<li>
    <p>
        <span>Create a bucket</span> - You must have a bucket to mount.  You can use any client to create a bucket.  For example, if you have installed the <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html">awscli</a> utility:
    </p>
<pre>
aws s3 --endpoint-url https://rgw.osris.org --profile=default mb s3://yourcou-newbucket
</pre>

<p>
    Please be sure to prefix your bucket names with the name of your OSiRIS virtual organization (lower case).  This is also referred to as 'COU' in the COmanage interface.  The AWSCLI utility uses the same credential file setup in the previous step.  Other utilities such as <a href="/documentation/s3cmd">s3cmd</a> may require an additional credential file.
</p>

</li>
<li>
    <p>
    <span>Mount your bucket</span> - The following example mounts yourcou-newbucket at /tmp/s3-bucket.  Unless you specify the -o allow_other option then only you will be able to access the mounted filesystem (be sure you are aware of the security implications if you allow_other - any user on the system can write to the S3 bucket in this case).
</p>

<pre>
s3fs yourcou-newbucket /tmp/s3-bucket  \
    -o profile=default -o use_path_request_style \
    -o url="https://rgw.osris.org"
</pre>

<p>
    Buckets can also be mounted system wide with fstab.  Generally in this case you'll choose to allow everyone to access the filesystem (allow_other) since it will be mounted as root.  As noted, be aware of the security implications as there are no enforced restrictions based on file ownership, etc (because it is not really a POSIX filesystem underneath).  There are nonetheless some workflows where this may be useful.
</p>

<pre>
s3fs#BUCKET /path/to/mountpoint fuse _netdev,allow_other,use_path_request_style,profile=default,url=https://rgw.osris.org 0 0
</pre>

</li>
</ol>

<h2>Performance with s3fs-fuse</h2>

The following section will provide an overview of expected performance while utlizing a s3fs-fuse mount from the OSiRIS network.  These figures are for a single client and reflect limitations of FUSE and the underlying HTTP based S3 protocol.  OSiRIS can support large numbers of clients for a higher aggregate throughput.     

<pre>
Regular block size (1M), single thread

	Mean writes - 30MB/s
	Mean reads  - 65MB/s

Regular block size (1M), multi-threaded

	Mean writes - 40MB/s
	Mean reads  - 65MB/s

Small block size (4K), single thread

	Mean writes - 26MB/s
	Mean reads  - 55MB/s

Small block size (4K), multi-threaded

	Mean writes - 31MB/s
	Mean reads  - 55MB/s
</pre>

<h2>References</h2>

More detailed instructions for using s3fs-fuse are available on the Github page: 
<a href="https://github.com/s3fs-fuse/s3fs-fuse">https://github.com/s3fs-fuse/s3fs-fuse</a>

The Amazon AWS CLI tools can be useful for various S3 operations such as making or listing buckets. s3fuse and the AWS util can use the same password credential file.  You must use the proper parameters to point the tool at OSiRIS S3 instead of Amazon:    
<a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html">AWS CLI installation</a>

The CLI tool 's3cmd' can also be used to manage buckets, etc:  <a href="/documentation/s3cmd">OSiRIS Documentation on s3cmd</a>

