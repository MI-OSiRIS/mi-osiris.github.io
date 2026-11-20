---
layout: post
category: article
title: "Grouper retired: OSiRIS groups are now managed in COmanage"
date: 2026-11-19
tags: [news, osiris, comanage]
---
{% include JB/setup %}

On 13 November 2026 we turned off Grouper, the separate tool OSiRIS used to manage Unix groups. Groups are now managed directly in COmanage at <a href="https://comanage.osris.org">comanage.osris.org</a>.

<!--excerpt-->

**What changes for you**

- Create groups and change their members in COmanage, under **Groups**. The [groups guide](/documentation/groups.html) shows how.
- COmanage passes each change to the OSiRIS directory right away, and OSiRIS systems see it within about a minute.
- The old link to Grouper (comanage.osris.org/grouper) no longer works.

**What stays the same**

- Your existing groups keep their names and group IDs, so files and folders owned by a group are not affected.
- The default groups for your COU (`CO_COU_YourCouName_members_active`, `CO_COU_YourCouName_admins`) work as before.

**Why**

Grouper had stopped passing group changes to the directory reliably, and it needed software we no longer run. We replaced it with a small COmanage plugin that does the same job and keeps the same group layout.

Questions or a group that doesn't look right: osiris-help@umich.edu.
