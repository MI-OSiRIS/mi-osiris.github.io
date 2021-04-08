---
layout: post
category : article 
title: Use of OSiRIS by SEAS Master's Students
tags : [ um, storage, comanage, s3]
---
{% include JB/setup %}

In the winter 2021 term at the University of Michigan, OSiRIS was used by four students in the School of the Environment and Sustainability (SEAS) for their Master's project, for which the SEAS course number 699 is used.

<!--excerpt-->

Master's students typically do not have access to funding, so they ran computations on Open Science Grid (OSG), which is also fee-free, and the data were accessed from the OSG execute nodes using OSiRIS's S3 interface.

The project modeled the biomass of the Washtenaw County, MI, Greenbelt from LiDAR images collected by overflight and distributed by NOAA. There were 3,220 images in the initial dataset, and 789 were modeled. The models were fit using the R programming language. Only a modest amount of disk was used (approximately 500 GB), but being able to access it directly from OSG was of crucial importance. OSiRIS staff were very helpful in getting things set up. Without OSiRIS and OSG, the initial estimate of approximately four hours per image showed that computations would have taken longer than the time available in the academic semester using the students's available computers.  Working with UM and OSG consultants, they were able to reduce the processing time significantly and complete it in time for their project to be evaluated and their degrees granted.
