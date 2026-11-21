---
layout: post
category: article
title: "Autumn 2026: OSiRIS infrastructure refresh"
date: 2026-11-19
tags: [news, osiris, horus, ceph]
---
{% include JB/setup %}

Since October we have upgraded or rebuilt most of the systems behind OSiRIS and HORUS, as part of keeping both services running on a best-effort basis through February 2027.

<!--excerpt-->

**Storage**

- The Ceph cluster runs **Ceph Tentacle (20.2.4)**, deployed with cephadm. It has about 1,230 disks (OSDs) at UM, MSU and WSU, about 11 PiB of raw storage, and keeps three copies of the data, one at each site.

**Servers**

- Most servers were patched and rebooted in a round between 26 October and 5 November, the first in years for many of them. The servers run **AlmaLinux 9** and are moving to AlmaLinux 9.9 in the regular patch rounds.
- Configuration management is moving from Puppet 7 to **OpenVox 8**, the community continuation of Puppet maintained by Vox Pupuli. A first set of servers already runs the new agent.

**Identity and accounts**

- The directory servers (LDAP) were rebuilt, and **COmanage** was upgraded to version 4.6.1.
- **Grouper has been retired.** Groups are now managed in COmanage, which passes changes to the directory automatically ([details]({% post_url 2026-11-19-grouper-retired %})).

**HORUS computing**

- Slurm was upgraded to 26.05, and jobs are now held to the memory they request ([HORUS news](https://horus-ci.org/)).
- The Open OnDemand portal's login was renewed with a new CILogon registration.

**Operations**

- Logging and monitoring were rebuilt, and an internal operations wiki now documents how the services are run.

Questions: osiris-help@umich.edu.
