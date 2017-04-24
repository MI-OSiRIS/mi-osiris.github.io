---
layout: post
category : article
title: "OSiRIS Engagement with Center for Trusted Scientific Computing"
tags : [ ctsc, oaa, papers ]
---
{% include JB/setup %}

<a href="https://scholarworks.iu.edu/dspace/handle/2022/21307"><img src="{{IMAGE_PATH}}/logos/ctsc_logo.png" alt="CTSC Logo" class="lf" style="width: 15%"></a>

OSiRIS recently finished a 6-month engagement with the Center for Trusted Scientific Computing.  The 2016-2017 CTSC-OSiRIS collaborative design review of OSiRIS Access Assertions produced a set of security recommendations documented in <a href="https://scholarworks.iu.edu/dspace/handle/2022/21307">this report</a> that the OSiRIS project plans to implement in its deployed cyberinfrastructure. CTSC identified no significant weaknesses in its review of the initial design of the OSiRIS access control system.   

From our perspective, the CTSC staff was helpful in ensuring that we had a well planned and secure design for OAA.  The engagment process was extremely valuable and we extend our thanks to CTSC!

<!--excerpt-->

What follows are some brief excerpts from the summary sections of the report:

After initial discussions with CTSC staff, representatives of the MI-OSiRIS project submitted a
CTSC engagement application in June 2016. From August to October 2016, CTSC and OSiRIS
staff developed the engagement plan, with the goal of conducting a joint design review of the
OSiRIS Access Assertion (OAA) system. CTSC staff conducted the engagement from October
2016 to March 2017 via a series of hour-long phone calls with OSiRIS staff to discuss and review
the OAA design. The report documents the outcomes of those discussions.

<a href="https://github.com/MI-OSiRIS/aa_services/tree/master/doc">OAA design documents</a> were the primary source materials used in the review. At the time of the review, the OAA system was in an early design and implementation phase, giving the group
the opportunity to consider a variety of design options and give input to design decisions, in
contrast to an after-the-fact security evaluation of an implemented system.

The engagement team discussed two categories of use cases for the OSiRIS system: 1)
distributed access to scientific data using <a href="http://docs.ceph.com/">Ceph</a> and 2) network discovery, monitoring, and
management using <a href="http://www.perfsonar.net/">perfSONAR</a> for reliable and high-performance use of Ceph across the
network. The former target science users, and the latter target network engineers. The OSiRIS
design includes a common authentication and authorization mechanism across these use cases,
supporting federated campus authentication via Internet2's <a href="https://incommon.org/federation/">InCommon</a> service and
group-based access control (with delegated sub-groups) using Internet2's <a href="https://www.internet2.edu/products-services/trust-identity/comanage/">COmanage</a> software.

The full <a href="https://scholarworks.iu.edu/dspace/handle/2022/21307">CTSC-OSiRIS Final Report</a> is publicly available.  