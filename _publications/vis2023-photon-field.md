---
title: "Photon Field Networks for Dynamic Real-Time Volumetric Global Illumination"
venue: "@VIS"
authors: "David Bauer, Qi Wu, and Kwan Liu Ma"
preprint_url: "https://drive.google.com/file/d/1R6bVLlHLQfcy-evgUDIdIMKCJkZzuC45/view?usp=sharing"
official_url: "https://ieeexplore.ieee.org/document/10297590"
arxiv_url: "https://arxiv.org/abs/2304.07338"
preview: "pubs/vis2023-photon-field.png"
teaser: "pubs/vis2023-photon-field-teaser.png"
teaser_caption: "Figure 1: Our photon field networks replace the global illumination term of the rendering equation. With our approach we are able to achieve comparable results for volumetric rendering in a fraction of the time it takes a conventional path tracer. The photon fields are light-weight and can be trained in seconds."
date: 2023-03-30
collection: "publications"
---

### Abstract

Volume data is fundamental in many scientific disciplines, like medicine, physics, and biology. Experts rely on robust scientific visualization techniques to extract valuable insights from the data. Recent years have shown path tracing to be the preferred approach for volumetric rendering, given its high levels of realism. However, real-time volumetric path tracing often suffers from stochastic noise and long convergence times, limiting interactive exploration. In this paper, we present a novel method to enable real-time global illumination for volume data visualization. We develop Photon Field Networks---a phase-function-aware, multi-light neural representation of indirect volumetric global illumination. The fields are trained on multi-phase photon caches that we compute a priori. Training can be done within seconds, after which the fields can be used in various rendering tasks. To showcase their potential, we develop a custom neural path tracer, with which our photon fields achieve interactive framerates even on large datasets. We conduct in-depth evaluations of the method's performance, including visual quality, stochastic noise, inference and rendering speeds, and accuracy regarding illumination and phase function awareness. Results are compared to state-of-the-art scientific rendering techniques. Our findings show that Photon Field Networks can faithfully represent indirect global illumination across the phase spectrum while exhibiting less stochastic noise and rendering at a significantly faster rate than traditional methods.

### BibTex

```bibtex
@article{bauer2023photon,
  author={Bauer, David and Wu, Qi and Ma, Kwan-Liu},
  journal={IEEE Transactions on Visualization and Computer Graphics}, 
  title={Photon Field Networks for Dynamic Real-Time Volumetric Global Illumination}, 
  year={2024},
  volume={30},
  number={1},
  pages={975-985},
  doi={10.1109/TVCG.2023.3327107}
}
```
