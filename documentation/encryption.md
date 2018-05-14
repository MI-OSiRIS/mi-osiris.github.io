---
layout: default
title : Working With Encrypted Data
tagline: Open Storage Research Infrastructure
header : Python Boto
---

{% include JB/setup %}

<h3>Getting started with uploading an encrypted file</h3>
First, get your key from comanage. This will be used for one of three variables required to create the boto connection.
The three variables are:
```
access_key = 'PUT YOUR ACCESS KEY FROM COMANAGE HERE'
secret_key = '' # value ignored by OSRIS
osris_host = 'rgw.osris.org'
```

Next we need to set up a boto connection to the host with:
```
conn = boto.connect_s3(aws_access_key_id = access_key,
                aws_secret_access_key = secret_key,
                host = osris_host,
                is_secure = True,
                port = 443,
                calling_format = boto.s3.connection.OrdinaryCallingFormat(),
                )
```
This is similar to setting up an unencrypted boto connection, but we need to specify that it is to be a secure connection and that we are using secure http.

<h3>Using SSE-C</h3>
We first need to create a header to encrypt the data over the wire. We need three variables: `x-amz-server-side-encryption-customer-algorithm`, `x-amz-server-side-encryption-customer-key`, and `x-amz-server-side-encryption-customer-key-MD5`. The encryption algorithm must be `"AES256"`; the key must be a 256 bit, base64-encoded encryption key; and the MD5 must be a base64-encoded 128-bit MD5 digest of the encryption key according to [RFC 1321](https://tools.ietf.org/rfc/rfc1321.txt). Here is an example of how to create the header:
```
key = base64.b64encode(keystring)
md5key = base64.b64encode(hashlib.md5(keystring).digest())

header = {
        "x-amz-server-side-encryption-customer-algorithm":"AES256",
        "x-amz-server-side-encryption-customer-key":key,
        "x-amz-server-side-encryption-customer-key-MD5":md5key
        }
```
Do note you **_MUST_** store your key (the variable `keystring`) somewhere. **_WE ARE UNABLE TO DECRYPT YOUR DATA! IF YOU LOOSE THE KEY, WE WILL BE UNABLE TO ASSIST YOU IN DECRYPTING THE DATA._** In the included example, we've included the steps to generate a random keystring and store it in a file.

<h3>Uploading a file</h3>
At this point, uploading a file can easily be done. We have to pass it the filepath, the header information, and set the encrypt_key to true. A copy of the header file will be needed with `ul_header = copy(header)`. This is due to the fact that the header information gets modified when used.
```
bucket = conn.create_bucket('testfile2')
k = bucket.new_key("test.txt")
k.set_contents_from_file(upload_file, headers=ul_header, encrypt_key=True)
```
Do note that there will be a performance hit when reading encrypted files.

<h3>Downloading an encrypted file</h3>
Downloading a file is very similar to uploading the file, except only the header and filepath are required. A copy of the header file will be needed with `ul_header = copy(header)`. This is due to the fact that the header information gets modified when used.
```
bucket = conn.create_bucket('testfile2')
kn = bucket.new_key("test.txt")
kn.get_contents_to_filename(download_file, headers=dl_header)
```

<h3>Force Encryption Policy</h3>
To force all objects for a bucket to be encrypted, use this json\_policy code below:
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

<h3>Examples</h3>
[encryption.py](examples/encryption.py) covers everything with the encryption.
