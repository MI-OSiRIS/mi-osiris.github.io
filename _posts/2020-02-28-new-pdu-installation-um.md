---
layout: post
category : article
title: New PDU Installed at University of Michigan
tags : [ hardware, um ]
---
{% include JB/setup %}

<div class="imgwrap lf" style="width: 28%">
<a href="{{IMAGE_PATH}}/umpdu/umich-pdu3-3.jpg">
    <img style="width: 100%" src="{{IMAGE_PATH}}/umpdu/umich-pdu3-2.jpg" alt="New Power Distribution Unit at UM" />
</a>
New Power Distribution Unit [PDU] Installed at University of Michigan
</div>

OSiRIS intalled a new third Power Distribution Unit [PDU] in rack 16EB to balance the load after the installation of 11 new servers at UM last year. 

<!--excerpt-->

In order to increase the resiliency against power failure, we installed a third Power Distribution Unit (PDU) to help balance the power load for the server rack hosting the new 11 Dell PowerEdge R7425 nodes that were installed last year at U-M. Previously, the rack was supported by two 30-amps PDUs which means that multiple systems could fail if one PDU or power source is down. So we have estimated the power consumptions for all the systems on that rack, and then rearranged them into three groups having roughly equal power consumption needs so that we can dedicate one PDU for each group. We also reconfigured those systems, where possible, to allow them to concurrently use both of their power supply units (PSUs) which was critical for estimating the power load drawn by every PSU, and for analyzing how the load from one PDU would split, in the event of failure, across the other two PDUs. The goal was to confirm that any two PDUs can still support the new power load resulting from the third PDU failing, and that we won’t have a cascade effect in which the failed PDU will cause another PDU to be overloaded, and then eventually cause that PDU to fail too.



