---
layout: post
category : article
tagline: "Site Provisioning and Ceph Installation"
tags : [installation, provisioning, sdn, nmal, perfsonar]
---
{% include JB/setup %}

With hardware installed and networking details mostly worked out OSiRIS sites have started work on OS provisioning.  After bringing up VM hosts configured using libvirt we are making progress on provisioning our service VMs and Ceph storage blocks.  We're using Foreman and Puppet to do provisioning plus configuration management.  More details about the provisioning setup are posted on our [hardware overview](/components/hardware.html)

We're configuring our hosts to be ready for software defined networking by configuring to use Openvswitch for connectivity:  [OVS Config](/components/sdn.html)

Sites have brought up standard perfSonar instances for the NMAL team to begin doing experimentation and testing.  The OSiRIS NMAL team at IU has been working on packaging their Periscope components for perfSonar as well.  
