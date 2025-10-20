---
title: "From Cluster to Desktop: A Cache-Accelerated INR framework for Interactive Visualization <br> of Tera-Scale Data"
venue: "@EGPGV"
authors: "Daniel Zavorotny, Qi Wu, David Bauer, and Kwan-Liu Ma"
preprint_url: "https://drive.google.com/file/d/1-cVZCaNBp7RAuNmVWQGBnx4huYS5Ekqj/view?usp=sharing"
official_url: "https://diglib.eg.org/items/d04e0485-4347-4ea5-9950-aa9a6967a732"
arxiv_url: "https://arxiv.org/abs/2504.18001"
preview: "pubs/egpgv2025-cinr.png"
date: 2025-04-13
collection: "publications"
teaser: "pubs/egpgv2025-cinr-teaser.png"
teaser_caption: "Image quality comparison of our multi-resolution pipeline with Wu et al.'s single resolution INR pipeline as our ground truth. The leftmost column of each comparison depicts pixel differences visually using FLIP, lighter is better. Additionally, we calculate PSNR, MSSIM, and LPIPs quality metrics based on both rendered images for each dataset. Results show that our cached pipeline maintains decent reconstruction quality while achieving the performance results."
---

### Abstract
Machine learning has enabled the use of implicit neural representations (INRs) to efficiently compress and reconstruct massive scientific datasets. However, despite advances in fast INR rendering algorithms, INR-based rendering remains computationally expensive, as computing data values from an INR is significantly slower than reading them from GPU memory. This bottleneck currently restricts interactive INR visualization to professional workstations. To address this challenge, we introduce an INR rendering framework accelerated by a scalable, multi-resolution GPU cache capable of efficiently representing tera-scale datasets. By minimizing redundant data queries and prioritizing novel volume regions, our method reduces the number of INR computations per frame, achieving an average 5x speedup over the state-of-the-art INR rendering method while still maintaining high visualization quality. Coupled with existing hardware-accelerated INR compressors, our framework enables scientists to generate and compress massive datasets in situ on high-performance computing platforms and then interactively explore them on consumer-grade hardware post hoc.

### BibTex 
```bibtex
@inproceedings{zavorotny2025cinr,
    author = {Zavorotny, Daniel and Wu, Qi and Bauer, David and Ma, Kwan-Liu},
    title = {From Cluster to Desktop: A Cache-Accelerated INR framework for Interactive Visualization of Tera-Scale Data},
    year = {2025},
    publisher = {Eurographics Association},
    booktitle = {Proceedings of the Symposium on Parallel Graphics and Visualization},
    series = {EGPGV '25}
}
```
