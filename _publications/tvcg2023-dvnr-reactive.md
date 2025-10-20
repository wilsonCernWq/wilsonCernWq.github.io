---
title: "Distributed Neural Representation for Reactive in situ Visualization"
venue: "@TVCG"
authors: "Qi Wu, Joseph Insley, Victor Mateevitsi, Silvio Rizzi, Michael Papka, and Kwan-Liu Ma"
preprint_url: "https://drive.google.com/file/d/1F2vJHvjoqXfhkIe4Glj6EcSNSQNx1pd7/view?usp=sharing"
official_url: "https://ieeexplore.ieee.org/document/10631163"
arxiv_url: "https://arxiv.org/abs/2304.10516"
preview: "pubs/tvcg2023-dvnr-reactive.png"
date: 2024-07-20
collection: "publications"
teaser: "pubs/tvcg2023-dvnr-reactive-teaser.png"
teaser_caption: "We compared the rendering of our distributed neural representations using varying numbers of training steps. The data was distributed to two MPI ranks and trained using two NVIDIA A100-40G GPUs on the ALCF Polaris supercomputer. Partition boundaries were highlighted using white lines in A) and B). C) are zoomed views of A) near partition boundaries. In 1C), an obvious discontinuity is visible at the partition boundary. With more training steps in 2), the discontinuity becomes less obvious, but high frequency noises are still visible. However, in 3), with sufficient training steps, these artifacts are no longer visible. We used flow field data generated from the S3D simulation for this experiment."
---

### Abstract

In situ visualization and steering of computational modeling can be effectively achieved using reactive programming, which leverages temporal abstraction and data caching mechanisms to create dynamic workflows. However, implementing a temporal cache for large-scale simulations can be challenging. Implicit neural networks have proven effective in compressing large volume data. However, their application to distributed data has yet to be fully explored. In this work, we develop an implicit neural representation for distributed volume data and incorporate it into the DIVA reactive programming system. This implementation enables us to build an in situ temporal caching system with a capacity 100 times larger than previously achieved. We integrate our implementation into the Ascent infrastructure and evaluate its performance using real-world simulations.

### BibTex

```bibtex
@article{wu2024distributed,
  author={Wu, Qi and Insley, Joseph A. and Mateevitsi, Victor A. and Rizzi, Silvio and Papka, Michael E. and Ma, Kwan-Liu},
  journal={IEEE Transactions on Visualization and Computer Graphics}, 
  title={Distributed Neural Representation for Reactive In Situ Visualization}, 
  year={2025},
  volume={31},
  number={9},
  pages={5199-5214},
  doi={10.1109/TVCG.2024.3432710}
}
```
