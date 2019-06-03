---
layout: default
title : s3cmd
tagline: Using s3mcd CLI for s3
header : s3cmd
---

{% include JB/setup %}

<h2>What is s3cmd</h2>

S3cmd is a command line tool for interacting with S3 storage.  It can create buckets, download/upload data, modify bucket ACL, etc.  It will work on Linux or MacOS.  Like many Linux tools we would also expect it to work with WSL (Windows Subsystem for Linux) but we have not specifically verified that.  

<h3>Installing S3cmd</h3>

S3cmd packages are available from the EPEL repository for RHEL variants, or from the Debian base repositories.  For MacOS you will have to download below or use PIP.

If you want to be sure to have the latest version you can download it from their site:  <a href="https://s3tools.org/download">https://s3tools.org/download</a>.

You can also use Python PIP:
<pre>
# system wide...

sudo pip install s3cmd

# Or install for user only (required on MacOS, cannot modify system python)
# For MacOS add ~/Library/Python/2.7/bin to PATH 

pip install --user s3cmd
</pre>


<h3>Config file</h3>
Create a new file ~/.s3cfg with the following contents.  Access key and secret key are available from <a href="https://comanage.osris.org">OSiRIS COmanage</a>.  
```
[default]
access_key   = YOUR ACCESS KEY HERE
secret_key   =
host_base    = rgw.osris.org
host_bucket  = rgw.osris.org/%(bucket)s
use_https    = True
signature_v2 = True
```

The file contains credential information so be sure it is readable only by you:
<pre>
chmod 0600 ~/.s3cfg
</pre>

<h3>Commands</h3>
All the s3cmd options can be found by running `s3cmd --help` or looking on the [s3tools usage](http://s3tools.org/usage) page. These options can be prefexed with `s3cmd` or with the encryption shown below.

* `ls [s3://BUCKET[/PREFIX]]` - List objects or buckets
* `mb s3://BUCKET` - creates a bucket
* `rb s3://BUCKET` - deletes a bucket
* `la` - list all objects in all buckets
* `put FILE [FILE...] s3://BUCKET[/PREFIX]` - put file(s) into a bucket
* `get s3://BUCKET/OBJECT` LOCAL\_FILE - Get file from bucket
* `del s3://BUCKET/OBJECT` - Delete file from bucket
* `rm s3://BUCKET/OBJECT` - Delete file from bucket (alias for del)
* `setacl s3://BUCKET[/OBJECT]` - Modify Access control list for Bucket or Files

<h3>Encryption</h3>
To encrypt an object or bucket, we need to pass the header information as arguments:
```
s3cmd \
> --add-header=x-amz-server-side-encryption-customer-algorithm:AES256 \
> --add-header=x-amz-server-side-encryption-customer-key:"$key" \
> --add-header=x-amz-server-side-encryption-customer-key-MD5:"$key_md5" \
> put test.txt s3://mycou-bucket
```
In this example, we are uploading a file to a bucket. The commands on the last line can be changed to work with any bucket or file. To create the two variables required, the following commands can be run:
```
secret="12345678901234567890123456789012"
key=$(echo -n $secret | base64)
key_md5=$(echo -n $secret | openssl dgst -md5 -binary | base64)
```

<h3>Examples</h3>
Creating a bucket:
```
$ s3cmd mb s3://mycou-bucket
Bucket 's3://mycou-bucket/' created
```

Listing buckets:
```
$ s3cmd ls
2018-06-01 21:07  s3://mycou-bucket
```

Removing buckets:
```
$ s3cmd rb s3://mycou-bucket
Bucket 's3://mycou-bucket/' removed
```

Uploading a file:
```
$ cat test.txt 
Hello World!
$ s3cmd put test.txt s3://mycou-bucket
upload: 'test.txt' -> 's3://mycou-bucket/test.txt'  [1 of 1]
 13 of 13   100% in    0s    77.87 B/s  done
```
A directory of files can be uploaded at once by adding the `--recursive` flag:
```
$ s3cmd --recursive put test_files/ s3://mycou-bucket
upload: 'test_files/boto.pdf' -> 's3://mycou-bucket/boto.pdf'  [1 of 4]
 3118319 of 3118319   100% in    0s     3.80 MB/s  done
upload: 'test_files/boto_keystring_example' -> 's3://mycou-bucket/boto_keystring_example'  [2 of 4]
 32 of 32   100% in    0s   148.15 B/s  done
upload: 'test_files/s3cfg' -> 's3://mycou-bucket/s3cfg'  [3 of 4]
 143 of 143   100% in    0s  1264.54 B/s  done
upload: 'test_files/test.txt' -> 's3://mycou-bucket/test.txt'  [4 of 4]
 12 of 12   100% in    0s   112.39 B/s  done
```

Listing files:
```
$ s3cmd la
2018-06-01 21:17        13   s3://mycou-bucket/test.txt
```

Downloading a file:
```
$ s3cmd get s3://mycou-bucket/test.txt test_download.txt
download: 's3://mycou-bucket/test.txt' -> 'test_download.txt'  [1 of 1]
 13 of 13   100% in    0s   120.21 B/s  done
$ cat test_download.txt 
Hello World!
```

Deleting a file:
```
$ s3cmd rm s3://mycou-bucket/test.txt
delete: 's3://mycou-bucket/test.txt'
```
A file can also be deleted with the `del` command:
```
$ s3cmd del s3://testcou-testfile2/test.txt
delete: 's3://testcou-testfile2/test.txt'
```
A series of files can be delted by listing all of the files you want to delete:
```
$ s3cmd rm s3://mycou-bucket/boto.pdf s3://mycou-bucket/boto_keystring_example s3://mycou-bucket/s3cfg s3://mycou-bucket/test.txtdelete: 's3://mycou-bucket/boto.pdf'
delete: 's3://mycou-bucket/boto_keystring_example'
delete: 's3://mycou-bucket/s3cfg'
delete: 's3://mycou-bucket/test.txt'
```

<h3>More Information</h3>
Full docs for s3cmd are available on the <a href="http://s3tools.org/s3cmd">project website</a>.
