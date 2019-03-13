---
layout: default
title : s3fs-fuse
tagline: Using S3 Fuse to mount S3 storage
header : Using S3 fuse 
---
{% include JB/setup %}

Benefits of s3fs-fuse

    - Maintains s3 structure, allowing cross-use with other s3 clients.
    - Easy to use.

Installation of s3fs-fuse

    - https://github.com/s3fs-fuse/s3fs-fuse
    - Specific instructions per operating system can be found in the s3fs-fuse git repo.

    CentOS 7 Example:

        sudo yum install automake fuse fuse-devel gcc-c++ git libcurl-devel libxml2-devel make openssl-devel

        git clone https://github.com/s3fs-fuse/s3fs-fuse.git
        cd s3fs-fuse
        ./autogen.sh
        ./configure
        make
        sudo make install

Configuring s3fs-fuse

    Setup Credential File

        First, you must generate a service token:

            - Access your account on https://comanage.osris.org
            - Navigate to the OSiRIS Tokens page from the account drop-down in the upper right corner.
            - In the CephRgwToken section, click Generate Token and copy the access key.

        Next, we use the generated service token to create a credential file:

            - The file may be named anything desired, however, must only contain the content MYIDENTITY:MYCREDENTIAL
                
		- MYIDENTITY is the service token generated in previous steps.
		- MYCREDENTIAL must exist, but may contain any string which helps identify the key.
		- Note: be certain to include the colon between the strings, with no additional characters.

	    - Once created, the credential file should have permissions changed to allow only owner read/write access (600).

Mounting with s3fs-fuse

    Mounting from the command line

	Example:

	s3fs BUCKET s3fs_destination_dir -o passwd_file=s3fs.passwd -o url=https://rgw.osris.org -o use_path_request_style

	    s3fs                          - Base command for s3fs command line tool.
	    BUCKET                        - Name of existing bucket on OSiRIS.
	    s3fs_destination_dir          - Target directory on which to mount BUCKET.
	    -o passwd_file=s3fs.passwd    - Absolute or relative path to credential file created previously.
	    -o url=https://rgw.osris.org  - Address of remote gateway
	    -o use_path_request_style     - Forces older path style request, used for non-Amazon S3 implementations.

        Once mounted, you will have access to the BUCKET at the designated s3fs_destination_dir, and can perform normal file operations.

    Mounting automatically with fstab

	Example:

	s3fs#BUCKET /path/to/mountpoint fuse _netdev,allow_other,use_path_request_style,url=https://rgw.osris.org 0 0

	    s3fs#BUCKET                - Denotes s3fs is to be used, with BUCKET representing the user bucket to be mounted.
	    /path/to/mountpoint        - The path to the directory on which BUCKET should be mounted.
	    fuse                       - Uses fuse as the filesystem type to be mounted.
	    _netdev                    - Delays mount until networking has been started.
	    allow_other                - Allows a user other than that which mounted the filesystem to gain access. Recommended, as fstab is processed by the root user.
	    use_path_request_style     - Forces older path style request, used for non-Amazon S3 implementations.
	    url=https://rgw.osris.org  - Address of remote gateway.
	    0                          - Whether the filesystem should be dumped. Use of zero prevents dumps for remote filesystem.
	    0                          - Order of filesystem check. Use of zero prevents the check on the remote filesystem.

Performance with s3fs-fuse

    While the performance of S3 mounted filesystems is dependent on many factors, not the least of which being a users local network, users may expect relative stability in the performance of similar operations. The following section will provide an overview of expected performance while utlizing a s3fs-fuse mount from the OSiRIS network.

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

S3 Limitations - https://github.com/s3fs-fuse/s3fs-fuse

    Random writes or appends to files require rewriting the entire file.
    Metadata operations such as listing directories have poor performance due to network latency.
    Eventual consistency can temporarily yield stale data(Amazon S3 Data Consistency Model).
    No atomic renames of files or directories.
    No coordination between multiple clients mounting the same bucket.
    No hard links.

References

    https://github.com/s3fs-fuse/s3fs-fuse - GitHub page for s3fs
