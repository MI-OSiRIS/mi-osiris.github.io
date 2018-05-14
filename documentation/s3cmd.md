---
layout: default
title : Using s3cmd
tagline: Open Storage Research Infrastructure
header : s3cmd
---

{% include JB/setup %}

<h3>Obtaining S3cmd</h3>
Since S3cmd needs to be version 2.0 or greater, you can get the most recent version on [SourceForge](https://sourceforge.net/projects/s3tools/files/s3cmd/). Not all package managers will have the current version. To check the version your system has, you can run `s3cmd --version`.

<h3>Config file</h3>
The following config file needs to be placed in the user's home directory. Please update the access key to match that in your comanage account.
```
[default]
access_key  = YOUR ACCESS KEY HERE
secret_key  =
host_base   = rgw.osris.org
host_bucket = rgw.osris.org/%(bucket)s
use_https   = True
```

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
> put test.txt s3://testBucket
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
$ s3cmd mb s3://test_TESTBUCKET
Bucket 's3://test_TESTBUCKET/' created
```

Listing buckets:
```
$ s3cmd ls
2018-06-01 21:07  s3://test_TESTBUCKET
```

Removing buckets:
```
$ s3cmd rb s3://test_TESTBUCKET
Bucket 's3://test_TESTBUCKET/' removed
```

Uploading a file:
```
$ cat test.txt 
Hello World!
$ s3cmd put test.txt s3://test_TESTBUCKET
upload: 'test.txt' -> 's3://test_TESTBUCKET/test.txt'  [1 of 1]
 13 of 13   100% in    0s    77.87 B/s  done
```
A directory of files can be uploaded at once by adding the `--recursive` flag:
```
$ s3cmd --recursive put test_files/ s3://testBucket
upload: 'test_files/boto.pdf' -> 's3://testBucket/boto.pdf'  [1 of 4]
 3118319 of 3118319   100% in    0s     3.80 MB/s  done
upload: 'test_files/boto_keystring_example' -> 's3://testBucket/boto_keystring_example'  [2 of 4]
 32 of 32   100% in    0s   148.15 B/s  done
upload: 'test_files/s3cfg' -> 's3://testBucket/s3cfg'  [3 of 4]
 143 of 143   100% in    0s  1264.54 B/s  done
upload: 'test_files/test.txt' -> 's3://testBucket/test.txt'  [4 of 4]
 12 of 12   100% in    0s   112.39 B/s  done
```

Listing files:
```
$ s3cmd la
2018-06-01 21:17        13   s3://test_TESTBUCKET/test.txt
```

Downloading a file:
```
$ s3cmd get s3://test_TESTBUCKET/test.txt test_download.txt
download: 's3://test_TESTBUCKET/test.txt' -> 'test_download.txt'  [1 of 1]
 13 of 13   100% in    0s   120.21 B/s  done
$ cat test_download.txt 
Hello World!
```

Deleting a file:
```
$ s3cmd rm s3://test_TESTBUCKET/test.txt
delete: 's3://test_TESTBUCKET/test.txt'
```
A file can also be deleted with the `del` command:
```
$ s3cmd del s3://testcou-testfile2/test.txt
delete: 's3://testcou-testfile2/test.txt'
```
A series of files can be delted by listing all of the files you want to delete:
```
$ s3cmd rm s3://testBucket/boto.pdf s3://testBucket/boto_keystring_example s3://testBucket/s3cfg s3://testBucket/test.txtdelete: 's3://testBucket/boto.pdf'
delete: 's3://testBucket/boto_keystring_example'
delete: 's3://testBucket/s3cfg'
delete: 's3://testBucket/test.txt'
```

<h3>More Information</h3>
Full docs for s3cmd are available on the <a href="http://s3tools.org/s3cmd">project website</a>.
