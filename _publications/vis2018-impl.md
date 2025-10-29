---
title: "CPU Isosurface Ray Tracing of Adaptive Mesh Refinement Data"
venue: "@VIS"
authors: "Feng Wang, Ingo Wald, Qi Wu, Will Usher, and Chris R. Johnson"
preprint_url: "https://drive.google.com/file/d/1cNUeMO8X8hUjtTWlrVxslmeLOdq3vdyJ/view?usp=sharing"
official_url: "https://doi.org/10.1109/TVCG.2018.2864850"
preview: "pubs/vis2018-impl.png"
teaser: "pubs/vis2018-impl-teaser.png"
teaser_caption: "Figure 1: We propose a novel rendering pipeline for fast volume rendering using optimized foveated sparse rendering and deep neural reconstruction networks. FoVolNet can faithfully reconstruct visual information from sparse inputs. With FoVolNet, developers are able to significantly improve rendering time without sacrificing visual quality."
code: "https://github.com/ethan0911/module-impi"
date: 2018-10-16
collection: "publications"
---

### Abstract

Adaptive mesh refinement (AMR) is a key technology for large-scale simulations that allows for adaptively changing the simulation mesh resolution, resulting in significant computational and storage savings. However, visualizing such AMR data poses a significant challenge due to the difficulties introduced by the hierarchical representation when reconstructing continuous field values. In this paper, we detail a comprehensive solution for interactive isosurface rendering of block-structured AMR data. We contribute a novel reconstruction strategy-the octant method-which is continuous, adaptive and simple to implement. Furthermore, we present a generally applicable hybrid implicit isosurface ray-tracing method, which provides better rendering quality and performance than the built-in sampling-based approach in OSPRay. Finally, we integrate our octant method and hybrid isosurface geometry into OSPRay as a module, providing the ability to create high-quality interactive visualizations combining volume and isosurface representations of BS-AMR data. We evaluate the rendering performance, memory consumption and quality of our method on two gigascale block-structured AMR datasets.

### BibTex

```bibtex
@article{wang2018cpu,
    author={Wang, Feng and Wald, Ingo and Wu, Qi and Usher, Will and Johnson, Chris R.},
    journal={IEEE Transactions on Visualization and Computer Graphics},
    title={CPU Isosurface Ray Tracing of Adaptive Mesh Refinement Data},
    year={2019},
    volume={25},
    number={1},
    pages={1142-1151},
    doi={10.1109/TVCG.2018.2864850}
}
```
