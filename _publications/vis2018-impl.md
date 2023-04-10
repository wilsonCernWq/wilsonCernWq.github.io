---
title: "CPU Isosurface Ray Tracing of Adaptive Mesh Refinement Data"
venue: "IEEE Visualization Conference (VIS)"
authors: "Feng Wang, Ingo Wald, Qi Wu, Will Usher, and Chris R. Johnson"
preprint_url: "https://drive.google.com/file/d/1cNUeMO8X8hUjtTWlrVxslmeLOdq3vdyJ/view?usp=sharing"
official_url: "https://doi.org/10.1109/TVCG.2018.2864850"
preview: "pubs/vis2018-impl.png"
bibtex: "@article{wang2018cpu,\n    author={Wang, Feng and Wald, Ingo and Wu, Qi and Usher, Will and Johnson, Chris R.},\n    journal={IEEE Transactions on Visualization and Computer Graphics}, \n    title={CPU Isosurface Ray Tracing of Adaptive Mesh Refinement Data}, \n    year={2019},\n    volume={25},\n    number={1},\n    pages={1142-1151},\n    doi={10.1109/TVCG.2018.2864850}\n}"
permalink: "/publication/vis2018-impl"
date: 2018-10-16
collection: "publications"
---

<figure><img src="/images/pubs/vis2018-impl-teaser.png" alt="image"><figcaption align = "center">Figure 1: We propose a novel rendering pipeline for fast volume rendering using optimized foveated sparse rendering and deep neural reconstruction networks. FoVolNet can faithfully reconstruct visual information from sparse inputs. With FoVolNet, developers are able to significantly improve rendering time without sacrificing visual quality.</figcaption></figure>

### Abstract

Adaptive mesh refinement (AMR) is a key technology for large-scale simulations that allows for adaptively changing the simulation mesh resolution, resulting in significant computational and storage savings. However, visualizing such AMR data poses a significant challenge due to the difficulties introduced by the hierarchical representation when reconstructing continuous field values. In this paper, we detail a comprehensive solution for interactive isosurface rendering of block-structured AMR data. We contribute a novel reconstruction strategy-the octant method-which is continuous, adaptive and simple to implement. Furthermore, we present a generally applicable hybrid implicit isosurface ray-tracing method, which provides better rendering quality and performance than the built-in sampling-based approach in OSPRay. Finally, we integrate our octant method and hybrid isosurface geometry into OSPRay as a module, providing the ability to create high-quality interactive visualizations combining volume and isosurface representations of BS-AMR data. We evaluate the rendering performance, memory consumption and quality of our method on two gigascale block-structured AMR datasets.