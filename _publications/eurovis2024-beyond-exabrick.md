---
title: "Beyond ExaBricks: GPU Volume Path Tracing of AMR Data"
venue: "@EuroVis"
authors: "Stefan Zellmann, Qi Wu, Alper Sahistan, Kwan-Liu Ma, and Ingo Wald"
official_url: "https://onlinelibrary.wiley.com/doi/10.1111/cgf.15095"
preprint_url: "https://drive.google.com/file/d/1-nYUIsiEqGLvnYhrMomyycOQyF-T5OFu/view?usp=sharing"
arxiv_url: "https://arxiv.org/abs/2211.09997"
preview: "pubs/eurovis2024-beyond.png"
teaser: "pubs/eurovis2024-beyond-teaser.png"
teaser_caption: "Figure 1: AMR rendering comparison using ExaBrick vs. our extended framework. Top-left: original 'sci-vis style' renderingwith ray marching, local shading with on-the-fly gradients, and a delta light source. Bottom-right: volumetric path tracing with multiscattering, isotropic phase function and ambient lighting. The original software used two RTX 8000 GPUs to render a convergence frame with allquality settings set to maximum at 4 frames/sec.; our framework, with the best combination of optimizations discussed in this paper, renderspath-traced convergence frames with full global illumination at 6.7 frames/sec."
date: 2024-05-01
collection: "publications"
---

### Abstract

Adaptive Mesh Refinement (AMR) is becoming a prevalent data representation for scientific visualization. Resulting from large fluid mechanics simulations, the data is usually cell centric, imposing a number of challenges for high quality reconstruction at sample positions. While recent work has concentrated on real-time volume and isosurface rendering on GPUs, the rendering methods used still focus on simple lighting models without scattering events and global illumination. As in other areas of rendering, key to real-time performance are acceleration data structures; in this work we analyze the major bottlenecks of data structures that were originally optimized for camera/primary ray traversal when used with the incoherent ray tracing workload of a volumetric path tracer, and propose strategies to overcome the challenges coming with this.

### BibTex

```bibtex
@article{zellmann2022beyond,
    title={Beyond ExaBricks: GPU Volume Path Tracing of AMR Data},
    author={Zellmann, Stefan and Wu, Qi and Sahistan, Alper and Ma, Kwan-Liu and Wald, Ingo},
    journal={arXiv preprint arXiv:2211.09997},
    year={2022}
}
```