#!/usr/bin/env python

# This is an example script that:
# 1) Creates a bucket
# 2) Creates a file (key in s3 land) with the text "Hello World!"
# 3) creates a URL to download the file that works for five minutes
# 4) deletes the file
# 5) deletes the bucket

import boto
import boto.s3.connection
import time

access_key = 'Your CephRgwToken'
secret_key = '' # value ignored by OSRIS
osiris_host = 'rgw.osris.org'
new_bucket = 'testcou-my-new-bucket'
new_public_bucket = 'testcou-public-bucket'

# Setup a connection
print "=> Connecting to {0}\n".format(osiris_host)
conn = boto.connect_s3( aws_access_key_id = access_key, aws_secret_access_key = secret_key, host = osiris_host, calling_format = boto.s3.connection.OrdinaryCallingFormat(),)

# create new bucket
print "=> Creating new bucket {0}\n".format(new_bucket)
bucket = conn.create_bucket(new_bucket)

print("=> Listing current buckets\n")
# List of buckets that you own
print("bucket name\tcreation time")
print("--------------------------")
for mybucket in conn.get_all_buckets():
    print("{name}\t{created}".format(
        name = mybucket.name,
        created = mybucket.creation_date,
        ))

print("\n=> Creating file \"hello.txt\" in bucket {0}\n".format(new_bucket))
# Create an object
key = bucket.new_key('hello.txt')
key.set_contents_from_string('Hello World!\n')

# Create a key from the file, set ACL, and generate a URL
# (we could reuse the 'key' from above but shown for example)
print "=> Getting key hello.txt from bucket"
hello_key = bucket.get_key('hello.txt')
print "=> Setting a canned acl 'private' on hello.txt"
hello_key.set_canned_acl('private')
hello_url = hello_key.generate_url(3600, query_auth=True, force_http=False)
print "=> Signed download URL to hello.txt that expires in 60 minutes (3600 seconds):\n{0}\n".format(hello_url)

# Set public ACL on a bucket
# create new bucket
print "=> Creating new bucket {0}\n".format(new_public_bucket)
bucket = conn.create_bucket(new_public_bucket)
print "=> Setting public-read acl on {0}\n".format(new_public_bucket)
bucket.set_canned_acl('public-read')

print("=> Creating file \"hello-public.txt\" in bucket {0}\n".format(new_public_bucket))
# Create an object
key = bucket.new_key('hello-public.txt')
key.set_contents_from_string('Hello World!\n')

print "=> Unsigned download URL to hello.txt that does not expire\n"
key.set_canned_acl('public-read')
hello_url = key.generate_url(0, query_auth=False,force_http=False)
print(hello_url) 

print "=> Listing all files in all buckets\n"
print("file\tsize\tlast modified")
print("--------------------------")
for key in bucket.list():
    print("{name}\t{size}\t{modified}".format(
        name = key.name,
        size = key.size,
        modified = key.last_modified,
        ))

# delete key
#bucket.delete_key('hello.txt')

# Delete the bucket
# conn.delete_bucket(bucket.name)

print ""
