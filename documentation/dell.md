---
layout: default
title : Hardware
tagline: Required hardware modifications
group: documentation
subnavgroup: documentation
---
{% include JB/setup %}

<h2>Dell branded LSI  HBA330</h2>

We have found some Dell HBA cards based on LSI SAS3008 to require a modification to the manufacturer configuration portion of the card itself to properly function.

<font style="font-weight: bold"># lspci -nnv -s &lt;PCI Address of the HBA card&gt;</font>
<pre>
# lspci -nnv -s 61:00.0
61:00.0 Serial Attached SCSI controller [0107]: Broadcom / LSI SAS3008 PCI-Express Fusion-MPT SAS-3 [1000:0097] (rev 02)
   Subsystem: Dell HBA330 Adapter [1028:1f45]
   Flags: bus master, fast devsel, latency 0, IRQ 111, NUMA node 3
   I/O ports at 6000 [size=256]
   Memory at ce500000 (64-bit, non-prefetchable) [size=64K]
   Memory at ce400000 (64-bit, non-prefetchable) [size=1M]
   Expansion ROM at &lt;ignored&gt; [disabled]
   Capabilities: [50] Power Management version 3
   Capabilities: [68] Express Endpoint, MSI 00
   Capabilities: [a8] MSI: Enable- Count=1/1 Maskable+ 64bit+
   Capabilities: [c0] MSI-X: Enable+ Count=96 Masked-
   Capabilities: [100] Advanced Error Reporting
   Capabilities: [1e0] #19
   Capabilities: [1c0] Power Budgeting <?>
   Capabilities: [190] #16
   Capabilities: [150] Single Root I/O Virtualization (SR-IOV)
Capabilities: [148] Alternative Routing-ID Interpretation (ARI)
   Kernel driver in use: mpt3sas
   Kernel modules: mpt3sas
</pre>

We have found simply booting to a <a href="https://www.dell.com/support/article/us/en/19/sln305214/dell-poweredge-how-to-download-and-use-the-support-live-image?lang=en">Dell Live ISO Image</a> will make the required change however this can be time consuming for a large number of systems.

The first sign of this issue is the apperance of "overriding NVDATA EEDPTagMode setting" during the initial EL7 boot process.

The second sign of the issue is receiving "kernel: blk_update_request: I/O error, dev sda, sector 0" errors when attempting to access the disk device where sda is the target drive.

The incorrect value location "page type: <font style="font-weight: bold">9</font>, page number: <font style="font-weight: bold">11</font>, address 0x09" of the HBA 330 card itself.  A value of 0 will cause the previously mentioned overriding NVDATA error and I/O errors when attempting to access the device.  A value of 1 resolves this issue.

The method we have successfully used to update this value from the command line is through the use of <a href="https://github.com/mute55/LSIUtil">lsiutil</a>.

SYNTAX: -p &lt;portNumber&gt; # Probably 1 unless you have multiple cards
SYNTAX: -a &lt;Desired keystrokes with ,=enter to perform the desired action&gt;

In the below example, we choose to...
* communicate with controller/port#1
* 9 = "<font style="font-weight: bold">9</font>.  Read/change configuration pages"
* 9 = "Enter page type: <font style="font-weight: bold">9</font>"
* 11 = "Enter page number: <font style="font-weight: bold">11</font>"
* 0 = "<font style="font-weight: bold">0</font>=NVRAM"
* y = "Do you want to make changes?  [<font style="font-weight: bold">Y</font>es or No, default is No] "
* 0008 = "Enter offset of value to change:  [0004-0044 or RETURN to quit] <font style="font-weight: bold">0008</font>"
* 00000104 = "Enter value:  [00000000-FFFFFFFF or RETURN to not change] <font style="font-weight: bold">00000104</font>"
* , = "Enter offset of value to change:  [0004-0044 or <font style="font-weight: bold">RETURN</font> to quit] "
* y = "Do you want to write your changes?  [Yes or No, default is No] <font style="font-weight: bold">y</font>"
* , = "Enter page type:  [0-255 or <font style="font-weight: bold">RETURN</font> to quit]"
* 0 = "Main menu, select an option:  [1-99 or e/p/w or 0 to quit] <font style="font-weight: bold">0</font>"

<font style="font-weight: bold"># lsiutil -p1 -a 9,9,11,0,y,0008,00000104,,y,,0, </font>
<pre>

LSI Logic MPT Configuration Utility, Version 1.72, Sep 09, 2014

1 MPT Port found

     Port Name         Chip Vendor/Type/Rev    MPT Rev  Firmware Rev  IOC
      1.  ioc0              LSI Logic SAS3008 C0      205      10000800     0

      Main menu, select an option:  [1-99 or e/p/w or 0 to quit] 9

      Enter page type:  [0-255 or RETURN to quit] 9
      Enter page number:  [0-255 or RETURN to quit] 11
      Read NVRAM or current values?  [0=NVRAM, 1=Current, default is 0] 0

      0000 : 290b1200
      0004 : 80123278
      0008 : 00000<font style="font-weight: bold">0</font>04
      000c : 00100000
      0010 : 07f28155
      0014 : 00000000
      0018 : 00000000
      001c : 00000000
      0020 : 00000000
      0024 : 00000000
      0028 : 00000000
      002c : 00000000
      0030 : ffffffff
      0034 : ffffcfff
      0038 : efffffff
      003c : fff7efff
      0040 : ffffefff
      0044 : 7fffffff

      Do you want to make changes?  [Yes or No, default is No] y
      Enter offset of value to change:  [0004-0044 or RETURN to quit] 0008
      Enter value:  [00000000-FFFFFFFF or RETURN to not change] 00000<font style="font-weight: bold">1</font>04
      Enter offset of value to change:  [0004-0044 or RETURN to quit] 

      Do you want to write your changes?  [Yes or No, default is No] y
      Changes have been written

      Enter page type:  [0-255 or RETURN to quit] 

      Main menu, select an option:  [1-99 or e/p/w or 0 to quit] 0
</pre>


<!-- <img style="width: 50%" src="{{IMAGE_PATH}}/documentation/Comanage-person-menu.png" alt="COmanage Identity Menu"/> -->

