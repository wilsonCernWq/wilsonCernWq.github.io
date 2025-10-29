---
title: "VisIt-OSPRay: toward an exascale volume visualization system"
venue: "@EGPGV"
authors: "Qi Wu, Will Usher, Steve Petruzza, Sidharth Kumar, Feng Wang, Ingo Wald, Valerio Pascucci, and Charles D. Hansen"
preprint_url: "https://drive.google.com/file/d/1ulrP4ogjIoxCR2A_oE9afemqhyK04lLA/view?usp=sharing"
official_url: "https://dl.acm.org/doi/10.5555/3293524.3293526"
preview: "pubs/egpgv2018-visit-ospray.png"
teaser: "pubs/egpgv2018-visit-ospray-teaser.png"
teaser_caption: "Figure 1: High-quality interactive volume visualization using VisIt-OSPRay: a) volume rendering of O2 concentration inside a combustion chamber; b) volume rendering of the Richtmyer-Meshkov Instability; c) visualization of a supernova simulation; d) visualization of the aneurysm dataset using volume rendering and streamlines; e) scalable volume rendering of the 966GB DNS data on 64 Stampede2 Intel® Xeon Phi™ Knight's Landing nodes."
code: "https://github.com/wilsonCernWq/VisIt-OSPRay"
date: 2018-06-04
collection: "publications"
---

### Abstract

Large-scale simulations can easily produce data in excess of what can be efficiently visualized using production visualization software, making it challenging for scientists to gain insights from the results of these simulations. This trend is expected to grow with exascale. To meet this challenge, and run on the highly parallel hardware being deployed on HPC system, rendering systems in production visualization software must be redesigned to perform well at these new scales and levels of parallelism. In this work, we present VisIt-OSPRay, a high-performance, scalable, hybrid-parallel rendering system in VisIt, using OSPRay and IceT, coupled with PIDX for scalable I/O. We examine the scalability and memory efficiency of this system and investigate further areas for improvement to prepare VisIt for upcoming exascale workloads.

### BibTex

```bibtex
@inproceedings{wu2018visit,
    author = {Wu, Qi and Usher, Will and Petruzza, Steve and Kumar, Sidharth and Wang, Feng and Wald, Ingo and Pascucci, Valerio and Hansen, Charles D.},
    title = {{VisIt-OSPRay}: Toward an Exascale Volume Visualization System},
    year = {2018},
    publisher = {Eurographics Association},
    address = {Goslar, DEU},
    booktitle = {Proceedings of the Symposium on Parallel Graphics and Visualization},
    pages = {13-24},
    numpages = {12},
    location = {Brno, Czech Republic},
    series = {EGPGV '18}
}
```
