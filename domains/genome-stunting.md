---
layout: default
title : OSiRIS Research Highlight
tagline: Effect of the Placental Epigenome on Stunting in a Longitudinal African Cohort  
---
{% include JB/setup %}

<img style="width: 40%" class="lf" src="{{IMAGE_PATH}}/logos/isr_logo.png" alt="UM ISR Logo"/>

<br style="clear: both;" />

C. Vincenz, University of Michigan ISR

<div class="imgwrap rf" style="width: 40%">
    <a href="{{IMAGE_PATH}}/domains/vincenz-tiogou.jpg"><img style="width: 100%" src="{{IMAGE_PATH}}/domains/vincenz-tiogou.jpg" alt="Village in Mali where researchers work"/></a>
     Village in Mali where researchers work
</div>

Stunting is a global health problem that is common in low and middle-income
countries where one third of children under 5 years of age are affected. Small
mothers tend to give birth to small babies, but the epigenetic mechanisms that
underlie this correlation are poorly understood. Our study of 95 imprinted genes in
placentas from 600 mothers will test the hypothesis that genetic imprinting plays a
role in the inter-generational transmission of stunting. We take advantage of a
prospective cohort study of a rural African population in which 1144 subjects (F1
generation) are followed from infancy, through childhood, to first parenthood. We
combine longitudinal data, spanning 3 generations, with the analysis of allele-specific
expression of placental genes.

We perform expression analysis using RNAseq on an Illumina platform. In order to
distinguish maternal from paternal transcripts we have to generate sufficient
sequences at positions where the two transcripts differ. This requires deep
sequencing resulting in large files (~300x10 6 sequences/sample, ~ 17 Gb sequence
file). The mapping of these sequences to the genome generates BAM files that are
also large (~ 7 Gb). <span class="light-em">Because it is computationally expensive to generate BAM files
we take advantage to archive the files on OSiRIS for re-analysis with more up to
date workflows.</span> Analysis of allele specific expression is challenging from a bio-
informatics point of view and new refined workflows are proposed frequently, some
of which we want to test on our dataset requiring re-analysis of the archived files.

Allele specific expression also requires the sequence of the genomic DNA to identify
the positions at which the maternal allele differs from the paternal allele. The
resulting data are not only necessary for our analysis but it also represents a
population level allele frequency table. The study population speaks a language that
does not group with other West African languages and the geographical origins of
the group are uncertain. Thus, there is interest by population geneticists to use our
data to determine genetic affinities with other ethnic groups to solve the question of
their origin and time of isolation. <span class="light-em">We will use the OSiRIS platform to share the data
with population geneticists at the University of Michigan.</span>

As stunting leads to a wide array of health problems from poor cognitive function to
metabolic syndrome, it is important to understand how it is transmitted to the next
generation. The ongoing study is generating the basic science input that is
necessary for the eventual discovery of interventions and policies that prevent
stunting and its adverse effects on the quality of life.
