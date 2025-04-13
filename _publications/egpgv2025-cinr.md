---
title: "From Cluster to Desktop: A Cache-Accelerated INR framework for Interactive Visualization of Tera-Scale Data"
venue: "The Eurographics Symposium on Parallel Graphics and Visualization (EGPGV)"
authors: "Daniel Zavorotny, Qi Wu, David Bauer, Kwan-Liu Ma"
abstract: "Machine learning has enabled the use of implicit neural representations (INRs) to efficiently compress and reconstruct massive scientific datasets. However, despite advances in fast INR rendering algorithms, INR-based rendering remains computationally expensive, as computing data values from an INR is significantly slower than reading them from GPU memory. This bottleneck currently restricts interactive INR visualization to professional workstations. To address this challenge, we introduce an INR rendering framework accelerated by a scalable, multi-resolution GPU cache capable of efficiently representing tera-scale datasets. By minimizing redundant data queries and prioritizing novel volume regions, our method reduces the number of INR computations per frame, achieving an average 5x speedup over the state-of-the-art INR rendering method while still maintaining high visualization quality. Coupled with existing hardware-accelerated INR compressors, our framework enables scientists to generate and compress massive datasets in situ on high-performance computing platforms and then interactively explore them on consumer-grade hardware post hoc."
preprint_url: "https://drive.google.com/file/d/1-cVZCaNBp7RAuNmVWQGBnx4huYS5Ekqj/view?usp=sharing"
preview: "pubs/egpgv2025-cinr.png"
bibtex: "@inproceedings{zavorotny2025cinr,\n    author = {Zavorotny, Daniel and Wu, Qi and Bauer, David and Ma, Kwan-Liu},\n    title = {From Cluster to Desktop: A Cache-Accelerated INR framework for Interactive Visualization of Tera-Scale Data},\n    year = {2025},\n    publisher = {Eurographics Association},\n    booktitle = {Proceedings of the Symposium on Parallel Graphics and Visualization},\n    series = {EGPGV '25}\n}"
permalink: "/publication/egpgv2025-cinr"
date: 2025-04-13
collection: "publications"
---
