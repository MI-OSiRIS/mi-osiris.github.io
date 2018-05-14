#!/usr/bin/env python
import boto
import boto.s3.connection
import hashlib
import base64
import os
import random
import string
import sys

access_key = 'Your CephRgwToken'
secret_key = '' # value ignored by OSRIS
osris_host = 'rgw.osris.org'

# upload_file = open(sys.argv[1])
# download_file = sys.argv[2]

# Setup a connection
conn = boto.connect_s3(aws_access_key_id = access_key,
                aws_secret_access_key = secret_key,
                host = osris_host,
		is_secure = True,
		port = 443,
                calling_format = boto.s3.connection.OrdinaryCallingFormat(),
                )

# code to read your password from the saved location 
boto_key_file = "boto_keystring_example"

if os.path.isfile(boto_key_file):
    print "=> Getting key from disk (" + boto_key_file + ").\n"
    hashfile = open(boto_key_file, "r")
    keystring = hashfile.read()
else:
    print "=> Generating key.\n"
    keystring = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(32))
    print "=> Key generated: " + str(keystring) + " and storing to disk (" + boto_key_file + ")."
    hashfile = open(boto_key_file, "w+")
    hashfile.write(keystring)
hashfile.close()

print "=> Generating key and MD5 Sum\n"
key = base64.b64encode(keystring)
md5key = base64.b64encode(hashlib.md5(keystring).digest())

print "=> Generating header\n"
header = {
            "x-amz-server-side-encryption-customer-algorithm" :
            "AES256",
            "x-amz-server-side-encryption-customer-key" :
            key,
            "x-amz-server-side-encryption-customer-key-MD5" : 
	    md5key
            }

print "The header is:\n" + str(header) + "\n"

# Create copies of the header for each contact with a file
# This is due to that the header gets modified when passed.
ul_header = dict(header)
dl_header = dict(header)

print "=> Uploading an encrypted object\n"
# Upload a object
bucket = conn.create_bucket('testcou-testfile2')
k = bucket.new_key("test.txt")
# k.set_contents_from_string('Hello World!')
k.set_contents_from_string('Hello World!', headers=ul_header, encrypt_key=True)
# This is how to upload a file with encryption
# k.set_contents_from_file(fp="file.txt", headers=ul_header, encrypt_key=True)

print "=> Downloading the encrypted object\n"
# Download the object
kn = bucket.new_key("test.txt")
kn.get_contents_to_filename("test.txt", headers=dl_header)
