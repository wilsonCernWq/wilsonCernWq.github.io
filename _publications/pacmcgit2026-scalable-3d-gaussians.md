---
title: "Scalable Training and Rendering of 3D Gaussians for Large Scale Scientific Data"
venue: "@PACMCGIT"
authors: "Andres Sewell, Mengjiao Han, Qi Wu, and Steve Petruzza"
preprint_url: "https://drive.google.com/file/d/1eGrxwmrtRIwIEWGE2skGLEkPvjahyoIg/view?usp=sharing"
official_url: "https://dl.acm.org/doi/10.1145/3820022"
preview: "pubs/pacmcgit2026-scalable-3d-gaussians.jpg"
teaser: "pubs/pacmcgit2026-scalable-3d-gaussians-teaser.png"
teaser_caption: "Our scalable distributed 3DGS framework runs on the Johns Hopkins Turbulence dataset (2048 x 512 x 1536, 6.0 GB per timestep) using 128 GPUs on the Polaris supercomputer. Spatial decomposition and temporal coherence provide a 4.5x training speedup while maintaining high fidelity above 42 dB."
date: 2026-07-01
collection: "publications"
---

### Abstract

The application of machine learning techniques to 3D Gaussian Splatting (3DGS) has enabled high-fidelity interactive rendering of complex 3D scenes on modest compute resources, offering significant potential for scientific visualization. However, the memory demands of reconstructing large-scale scientific volumes at high fidelity exceed the capacity of individual GPUs. While distributed 3DGS frameworks exist for urban scenes, they rely on global scene analysis or frequent all-to-all communication, inherently limiting their scalability on High-Performance Computing (HPC) clusters. In this paper, we present a scalable distributed 3DGS training and rendering framework designed for large-scale scientific volumetric data. Leveraging the native domain decomposition of HPC simulations, our approach treats each spatial partition as an independent optimization task that avoids device-to-device communication. We further exploit temporal coherence in simulation data to accelerate training on subsequent timesteps. We perform experimental studies demonstrating that our approach achieves near-ideal weak scaling by eliminating synchronization overhead. Additionally, we evaluate the trade-offs of the standard 3DGS optimization strategy against a Markov Chain Monte Carlo (MCMC) approach. We find that while standard 3DGS produces higher quality reconstructions with larger Gaussian footprints, MCMC effectively bounds the primitive count at scale in exchange for a minor reduction in fidelity. Furthermore, we demonstrate that our temporal fine-tuning strategy for time-series data remains robust at scale, establishing a reliable path towards *in situ* applications of 3DGS for massive scientific simulations.

### System Overview

<figure>
  <img src="/images/pubs/pacmcgit2026-scalable-3d-gaussians-system.png" alt="Distributed 3D Gaussian Splatting system architecture" style="display:block; width:90%; max-width:900px; margin:0 auto;">
  <figcaption align="center">Figure 2: Simulation data is partitioned using native domain decomposition and expanded with ghost cells to maintain boundary continuity. Training runs as a purely data-parallel task with zero inter-GPU synchronization. Independent renders are resolved through fragment-level clipping and sort-last compositing.</figcaption>
</figure>

### Key Contributions

- A distributed 3D Gaussian Splatting framework tailored to large-scale scientific volumetric data and native HPC domain decomposition.
- Independent per-partition optimization without device-to-device communication, enabling near-ideal weak scaling.
- A comparison of standard 3DGS optimization and MCMC-based optimization, characterizing the trade-off between reconstruction quality and bounded primitive counts.
- A temporal fine-tuning strategy that reuses coherence between simulation timesteps and remains robust as the workload scales.

### Results at Scale

<figure>
  <img src="/images/pubs/pacmcgit2026-scalable-3d-gaussians-results.png" alt="Composited renders of four scientific datasets" style="display:block; width:68%; max-width:720px; margin:0 auto;">
  <figcaption align="center">Figure 5: Composited renders of four datasets partitioned into 256 domains and trained in parallel using 256 GPUs. The communication-free spatial decomposition approach maintains high visual fidelity across datasets with different structures and scales.</figcaption>
</figure>

<figure>
  <img src="/images/pubs/pacmcgit2026-scalable-3d-gaussians-scaling.png" alt="Weak scaling performance and reconstruction quality charts" style="display:block; width:72%; max-width:760px; margin:0 auto;">
  <figcaption align="center">Figure 6: Weak-scaling performance and reconstruction quality across four datasets. The communication-free pipeline maintains stable training times at large GPU counts, while synchronization-based baselines encounter increasing communication overhead.</figcaption>
</figure>

### BibTex

```bibtex
@article{sewell2026scalable,
  author = {Sewell, Andres and Han, Mengjiao and Wu, Qi and Petruzza, Steve},
  title = {Scalable Training and Rendering of 3D Gaussians for Large Scale Scientific Data},
  journal = {Proceedings of the ACM on Computer Graphics and Interactive Techniques},
  year = {2026},
  volume = {9},
  number = {4},
  pages = {1--25},
  doi = {10.1145/3820022}
}
```
