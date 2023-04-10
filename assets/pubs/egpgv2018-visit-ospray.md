
<!-- 
<figure>
<img src="/images/pubs/egpgv2018-visit-ospray-teaser.png" alt="image">
<figcaption align = "center">Figure 1: High-quality interactive volume visualization using VisIt-OSPRay: a) volume rendering of O2 concentration inside a combustion chamber; b) volume rendering of the Richtmyer-Meshkov Instability; c) visualization of a supernova simulation; d) visualization of the aneurysm dataset using volume rendering and streamlines; e) scalable volume rendering of the
966GB DNS data on 64 Stampede2 Intel® Xeon Phi™ Knight’s Landing nodes.</figcaption>
</figure> -->


### Abstract

Large-scale simulations can easily produce data in excess of what can be efficiently visualized using production visualization software, making it challenging for scientists to gain insights from the results of these simulations. This trend is expected to grow with exascale. To meet this challenge, and run on the highly parallel hardware being deployed on HPC system, rendering systems in production visualization software must be redesigned to perform well at these new scales and levels of parallelism. In this work, we present VisIt-OSPRay, a high-performance, scalable, hybrid-parallel rendering system in VisIt, using OSPRay and IceT, coupled with PIDX for scalable I/O. We examine the scalability and memory efficiency of this system and investigate further areas for improvement to prepare VisIt for upcoming exascale workloads.