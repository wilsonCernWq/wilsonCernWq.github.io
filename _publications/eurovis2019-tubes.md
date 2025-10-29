---
title: "Ray Tracing Generalized Tube Primitives: Method and Applications"
venue: "@EuroVis"
authors: "Mengjiao Han, Ingo Wald, Will Usher, Qi Wu, Feng Wang, Valerio Pascucci, Charles D. Hansen, and Chris R. Johnson"
preprint_url: "https://drive.google.com/file/d/17pB_tIKD3jF6bVT1u9wpx9dwO_MqD-n6/view?usp=sharing"
official_url: "https://doi.org/10.1111/cgf.13703"
preview: "pubs/eurovis2019-tubes.png"
teaser: "pubs/eurovis2019-tubes-teaser.png"
teaser_caption: "Figure 1: Visualizations using our 'generalized tube' primitives. (a): DTI tractography data, semi-transparent fixed-radius streamlines (218K line segments). (b): A generated neuron assembly test case, streamlines with varying radii and bifurcations (3.2M l. s.). (c): Aneurysm morphology, semi-transparent streamlines with varying radii and bifurcations (3.9K l. s.) and an opaque center line with fixed radius and bifurcations (3.9K l. s.). (d): A tornado simulation, withradius used to encode the velocity magnitude (3.56M l. s.). (e): Flow past a torus, fixed-radiuspathlines (6.5M l. s.). Rendered at: (a) 0.38FPS, (b) 7.2FPS, (c) 0.25FPS, (d) 18.8FPS, with a 20482 framebuffer; (e) 23FPS with a 2048 x 786 framebuffer Performance measured on a dual Intel® Xeon® E5-2640 v4 workstation, with shadows and ambient occlusion."
code: "https://github.com/MengjiaoH/ospray-module-tubes"
date: 2019-06-01
collection: "publications"
---

### Abstract

We present a general high-performance technique for ray tracing generalized tube primitives. Our technique efficiently supports tube primitives with fixed and varying radii, general acyclic graph structures with bifurcations, and correct transparency with interior surface removal. Such tube primitives are widely used in scientific visualization to represent diffusion tensor imaging tractographies, neuron morphologies, and scalar or vector fields of 3D flow. We implement our approach within the OSPRay ray tracing framework, and evaluate it on a range of interactive visualization use cases of fixed- and varying-radius streamlines, pathlines, complex neuron morphologies, and brain tractographies. Our proposed approach provides interactive, high-quality rendering, with low memory overhead.

### BibTex
```bibtex
@inproceedings{han2019ray,
    title={Ray tracing generalized tube primitives: Method and applications},
    author={Han, Mengjiao and Wald, Ingo and Usher, Will and Wu, Qi and Wang, Feng and Pascucci, Valerio and Hansen, Charles D. and Johnson, Chris R.},
    booktitle={Computer Graphics Forum},
    volume={38},
    number={3},
    pages={467--478},
    year={2019},
    organization={Wiley Online Library}
}
```