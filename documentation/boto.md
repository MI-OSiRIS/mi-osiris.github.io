---
layout: default
title : Using Python Boto
tagline: Open Storage Research Infrastructure
header : Python Boto
---

{% include JB/setup %}

- [Getting Started](#gettingStarted)
- [Creating a connection to OSRIS](#newConn)
- [Working with Buckets](#buckets)
   - [Listing owned buckets](#ownedBucketListing)
   - [Creating a bucket](#createBucket)
   - [Deleting a bucket](#deleteBucket)
   - [Listing a bucket's content](#listBucketContent)
   - [Changing a bucket ACL](#ObjectACL)
- [Working with Objects](#objects)
   - [Creating an object](#createObject)
   - [Changing an object's ACL](#objectACL)
   - [Delete an object](#delObject)
   - [Downloading an object to a file](#downloadFile)
   - [Generating an object download URL](#downloadURL)
- [Server Side Encryption](#sse)
   - [Uploading an encrypted object](#uploadEncrypt)
   - [Downloading an encrypted object](#downloadEncrypted)
   - [Force Encryption Policy](#encryptionPolicy)
- [Sample Scripts](#examples)
- [More Information](#moreInfo)

<a name="gettingStarted" />
<h3>Getting started with ACL and boto</h3>

1. Install boto with pip: `pip install boto`
2. Create (if required) and get your [access key](s3).
3. Modify the example code to use your own access key.
4. Run the example code to test that you are able to connect to the S3 endpoint.

<a name="newConn" />
<h3>Creating a connection to OSRIS</h3>
Using boto in a python script requires you to import both boto and boto.s3.connection as follows:
```
#!/usr/bin/env python
import boto
import boto.s3.connection
```
The value for `access_key` needs to be changed to your OSiRIS access key. You can get your access key from OSiRIS COmanage under the 'OSiRIS Tokens' in the menu at upper right of the screen.  The token screen look like the image below.  For more information please have a look at our [S3 Instructions page](s3)
<img src="{{IMAGE_PATH}}/documentation/enrollment/Comanage-token-generated.png" alt="COmanage token screen after generating S3 token"/>
The `secret_key` value is ignored, so we keep it as a blank string. We also specify the `osris_host` to our S3 endpoint. We are then able to create a boto connection object to work from.
```
access_key = 'CephRgwToken from Comanage'
secret_key = ''
osris_host = 'rgw.osris.org'

# Setup a connection
conn = boto.connect_s3(aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = osris_host,
	is_secure = True,
	port = 443,
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )
```

<a name="buckets" />
<a name="ownedBucketListing" />
<h3>Listing owned buckets</h3>
The following example gets a list of Buckets that you own. It will print the bucket name and the creation date of each bucket.
```
for bucket in conn.get_all_buckets():
        print "{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
        )
```
The result should look something like this:
```
mahbuckat1   2011-04-21T18:05:39.000Z
mahbuckat2   2011-04-21T18:05:48.000Z
mahbuckat3   2011-04-21T18:07:18.000Z
```

<a name="createBucket" />
<h3>Creating a bucket</h3>
Creating a new bucket is simple:
```
bucket = conn.create_bucket('testcou-my-new-bucket')
```
Please note that buckets on OSRIS should start with your COU. The COU will be after your user id. In the example below, it will be `testcou`.

<img style="width: 80%" src="{{IMAGE_PATH}}/documentation/s3/Comanage-s3user.png" alt="COmanage S3 user"/>

<a name="deleteBucket" />
<h3>Deleting a bucket</h3>
Deleting a bucket is also simple:
```
conn.delete_bucket(bucket.name)
```
Note that the bucket must be empty in order to delete it. There is no way to force a non-empty bucket to be deleted.

<a name="createObject" />
<h3>Creating an object</h3>
This creates a file `hello.txt` with the string `Hello World!`
```
key = bucket.new_key('hello.txt')
key.set_contents_from_string('Hello World!')
```

<a name="listBucketContent" />
<h3>Listing a bucket's content</h3>
`bucket.list()` gets a list of objects in the bucket. The example below prints out the name, file size, and last modified date of each object.
```
for key in bucket.list():
        print "{name}\t{size}\t{modified}".format(
                name = key.name,
                size = key.size,
                modified = key.last_modified,
                )
```
<a name="objects">
<a name="createObject" />
<h3>Creating an object</h3>
This creates a file `hello.txt` with the string `Hello World!`
```
key = bucket.new_key('hello.txt')
key.set_contents_from_string('Hello World!')
```

<a name="objectACL" />
<h3>Change an object's ACL</h3>
The ACL can be assigned to a file as shown below:
```
public_hello = bucket.get_key('hello.txt')
public_hello.set_canned_acl('public-read')
private_hello = bucket.get_key('private_hello.txt')
private_hello.set_canned_acl('private')
```
<a name="bucketAcl" />
A similar process can be used for assigning an ACL to a bucket:
```
bucket.set_canned_acl('public-read')
```
Information on bucket ACLs can be found [here](http://boto3.readthedocs.io/en/latest/guide/s3-example-access-permissions.html)

<a name="delObject" />
<h3>Delete an object</h3>
This deletes the object hello.txt
```
bucket.delete_key('hello.txt')
```

<a name="downloadFile" />
<h3>Download an object to a file</h3>
This example downloads the object hello.txt and saves it in /tmp.
```
key = bucket.get_key('hello.txt')
key.get_contents_to_filename('/tmp/hello.txt')
```

<a name="downloadURL" />
<h3>Generate a signed or unsigned object download URL</h3>
An unsigned download URL works when a key is publically readable.
```
hello_key = bucket.get_key('hello.txt')
hello_url = hello_key.generate_url(0, query_auth=False)
print hello_url
```
The output will look something like:
```
https://rgw.osris.org/mycou-bucket/hello.txt
```
With signed download URLs will work for the time specified (in seconds) even if the object is private, though the URL will stop working when the time period is up.
```
plans_key = bucket.get_key('secret_plans.txt')
plans_url = plans_key.generate_url(3600, query_auth=True)
print plans_url
```
The output will look something like:
```
https://rgw.osris.org/mycou-bucket/secret_plans.txt?Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXX&Expires=1316027075&AWSAccessKeyId=XXXXXXXXXXXXXXXXXXX
```

<a name="sse" />
<h3>Using Server Side Encryption (SSE-C)</h3>
We first need to create a header to encrypt the data over the wire. We need three variables: `x-amz-server-side-encryption-customer-algorithm`, `x-amz-server-side-encryption-customer-key`, and `x-amz-server-side-encryption-customer-key-MD5`. The encryption algorithm must be `"AES256"`; the key must be a 256 bit, base64-encoded encryption key; and the MD5 must be a base64-encoded 128-bit MD5 digest of the encryption key.  More information on SSE-C is available from the [Amazon S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html). Here is an example of how to create the header:
```
# Don't lose this secret, it is required to decrypt your data!
keystring = '32characterSecretStringXXXXXXXX'
key = base64.b64encode(keystring)
md5key = base64.b64encode(hashlib.md5(keystring).digest())

header = {
        "x-amz-server-side-encryption-customer-algorithm":"AES256",
        "x-amz-server-side-encryption-customer-key":key,
        "x-amz-server-side-encryption-customer-key-MD5":md5key
        }
```
It is your responsibility to store your key string (the variable `keystring`) somewhere. **_WE ARE UNABLE TO DECRYPT YOUR DATA! IF YOU LOSE THE KEY, WE WILL BE UNABLE TO ASSIST YOU IN DECRYPTING THE DATA._** In the sample script  [encryption.py](examples/encryption.py), we've included the steps to generate a random keystring and store it in a file for re-use.

<a name="uploadEncrypt" />
<h3>Uploading a file</h3>
We have to pass our upload method the filepath, the header information, and set the encrypt_key to true. We make a copy of our header dict with `ul_header = copy(header)`. This is due to the fact that the header variable content gets modified when used - we make a copy each time so we can re-use our original dictionary for future operations.
```
ul_header = copy(header)
bucket = conn.create_bucket('testcou-testfile2')
k = bucket.new_key("test.txt")
k.set_contents_from_file(upload_file, headers=ul_header, encrypt_key=True)
```
There will be a performance difference vs unencrypted objects when reading objects.

<a name="downloadEncrypted" />
<h3>Downloading an encrypted file</h3>
Downloading a file is very similar to uploading the file, except only the header and filepath are required. Again we make a copy of the header file. 
```
dl_header = copy(header)
bucket = conn.create_bucket('testcou-testfile2')
kn = bucket.new_key("test.txt")
kn.get_contents_to_filename(download_file, headers=dl_header)
```

<a name="encryptionPolicy" />
<h3>Force Encryption Policy</h3>
To force all objects uploaded to a bucket to be encrypted, use this json\_policy code below:
```
json_policy = """{
   "Version":"2018-05-24",
   "Id":"PutObjPolicy",
   "Statement":[{
         "Sid":"DenyUnEncryptedObjectUploads",
         "Effect":"Deny",
         "Principal":{
            "AWS":"*"
         },
         "Action":"s3:PutObject",
         "Resource":"arn:aws:s3:::%s/*",
         "Condition":{
            "StringNotEquals":{
               "s3:x-amz-server-side-encryption":"AES256"
            }
         }
      }
   ]
}"""
```
Then you can set the policy with `bucket.set_policy(json_policy % bucket.name)`
<a name="examples" />
<h3>Sample Script</h3>

* [osiris-boto-example.py](examples/osiris-boto-example.py) - This script creates two buckets and an object in each bucket. It then gives an signed URL for one of the objects and an unsigned URL for the other object. The example also shows how to delete an object.
* [encryption.py](examples/encryption.py) covers everything with the encryption.

<a name="moreInfo" />
<h3>More Information</h3>

<a href="http://docs.ceph.com/docs/master/radosgw/s3/python/">More examples at ceph.com</a>

<a href="http://boto.cloudhackers.com/en/latest/s3_tut.html">S3 Docs for Boto2</a>

Most of these examples are adapted from the docs linked above at ceph.com.  

These examples and other examples at ceph.com refer to boto2 but you may be using the most current boto3.  Docs for that version are at the URL below:

<a href="http://boto3.readthedocs.io/en/latest/guide/s3-examples.html">S3 Docs for Boto3</a>
