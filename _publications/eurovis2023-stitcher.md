---
title: "Memory-Efficient GPU Volume Path Tracing of AMR Data Using the Dual Mesh"
venue: "The Eurographics Conference on Visualization (EuroVis)"
authors: "Stefan Zellmann, Qi Wu, Kwan-Liu Ma, and Ingo Wald"
abstract: "A common way to render cell-centric adaptive mesh refinement (AMR) data is to compute the dual mesh and visualize that with a standard unstructured element renderer. While the dual mesh provides a high-quality interpolator, the memory requirements of the dual mesh data structure are significantly higher than those of the original grid, which prevents rendering very large data sets. We introduce a GPU-friendly data structure and a clustering algorithm that allow for efficient AMR dual mesh rendering with a competitive memory footprint. Fundamentally, any off-the-shelf unstructured element renderer running on GPUs could be extended to support our data structure just by adding a gridlet element type in addition to the standard tetrahedra, pyramids, wedges, and hexahedra supported by default. We integrated the data structure into a volumetric path tracer to compare it to various state-of-the-art unstructured element sampling methods. We show that our data structure easily competes with these method in terms of rendering performance, but is much more memory-efficient."
preprint_url: "https://drive.google.com/file/d/1oW1ZMzcH_Yxh7ST7gMfreQqTFrhlpmWo/view?usp=share_link"
preview: "pubs/eurovis2023-stitcher.png"
teaser: "pubs/eurovis2023-stitcher-teaser.png"
teaser_caption: "Figure 1: Overview of our method. Given a block-structured or octree-AMR data set (left) we first create the dual mesh (middle) and split that into the truly unstructured elements used to stitch the level boundaries (red) and those that are regular voxels (blue/white checkered). We then cluster voxels to become agridletso. Right: gridlets colorized by their ID. We build a bounding volume hierarchy over the gridlets and the remaining unstructured elements. The result is a sampleable representation that generates the exact same result as sampling on the dual mesh directly, but with significantly lower memory overhead and higher sampling speed. On our largest data sets, we see memory savings of up to 3x compared to highly compressed state-of-the-art unstructured mesh representations."
permalink: "/publication/eurovis2023-stitcher"
date: 2023-02-27
collection: "publications"
---
<!-- leave empty for now -->
