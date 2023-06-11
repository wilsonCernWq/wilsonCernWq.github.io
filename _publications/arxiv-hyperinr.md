---
title: "HyperINR: A Fast and Predictive Hypernetwork for Implicit Neural Representations via Knowledge Distillation"
venue: "ArXiv Preprint"
authors: "Qi Wu, David Bauer, Yuyang Chen, and Kwan Liu Ma"
abstract: "Implicit Neural Representations (INRs) have recently exhibited immense potential in the field of scientific visualization for both data generation and visualization tasks. However, these representations often consist of large multi-layer perceptrons (MLPs), necessitating millions of operations for a single forward pass, consequently hindering interactive visual exploration. While reducing the size of the MLPs and employing efficient parametric encoding schemes can alleviate this issue, it compromises generalizability for unseen parameters, rendering it unsuitable for tasks such as temporal super-resolution. In this paper, we introduce HyperINR, a novel hypernetwork architecture capable of directly predicting the weights for a compact INR. By harnessing an ensemble of multiresolution hash encoding units in unison, the resulting INR attains state-of-the-art inference performance (up to 100x higher inference bandwidth) and can support interactive photo-realistic volume visualization. Additionally, by incorporating knowledge distillation, exceptional data and visualization generation quality is achieved, making our method valuable for real-time parameter exploration. We validate the effectiveness of the HyperINR architecture through a comprehensive ablation study. We showcase the versatility of HyperINR across three distinct scientific domains: novel view synthesis, temporal super-resolution of volume data, and volume rendering with dynamic global shadows. By simultaneously achieving efficiency and generalizability, HyperINR paves the way for applying INR in a wider array of scientific visualization applications."
preprint_url: "https://drive.google.com/file/d/1CY2WSxNTNXOap0vDW4euh4S6xJQf8UE7/view?usp=share_link"
arxiv_url: "https://arxiv.org/abs/2304.04188"
preview: "pubs/arxiv-hyperinr.png"
teaser: "pubs/arxiv-hyperinr-teaser.png"
teaser_caption: "Figure 1: Comparisons between HyperINR and data interpolation for the temporal super-resolution task using the vortices dataset. Listed timesteps are midpoints of different interpolation intervals. HyperINR can directly predict the weights of a regular implicit neural representation (INR) for unseen parameters. The predicted INR is in general more accurate than data interpolation results and can support interactive volumetric path tracing."
permalink: "/publication/arxiv-hyperinr"
date: 2023-03-31
collection: "publications"
---
<!-- adding a comment here to avoid being captured by sitemap -->

<figure>
<img src="/images/pubs/arxiv-hyperinr-teaser-2.png" alt="image">
<figcaption align = "center">Figure 2: The architecture of HyperINR. HyperINR is composed of a shared MLP denoted as S and a collection of multiresolution hash encoding parameters E, with each parameter associated with a set of values {a,b,c,...}. A) In high dimensions, a KD-tree is utilized, B) while in 1D, the encoding parameters are arranged in a linear array. C) The input parameter q is utilized to query the data structure, and the queried encoding parameters are interpolated and combined with the shared MLP to construct an INR. The resulting INR enables interactive visualization and real-time parameter exploration.</figcaption>
</figure>
