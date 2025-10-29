---
title: "A Flexible Data Streaming Design for Interactive Visualization of Large-Scale Volume Data"
venue: "@EGPGV"
authors: "Qi Wu, Michael J. Doyle, and Kwan-Liu Ma"
preprint_url: "https://drive.google.com/file/d/13laOefDThpDUr-nxfpjTVLdTI2tiNpCi/view?usp=sharing"
official_url: "https://doi.org/10.2312/pgv.20221064"
preview: "pubs/egpgv2022-streaming-volume.png"
teaser: "pubs/egpgv2022-streaming-volume-teaser.png"
teaser_caption: "Figure 1: Large-scale progressive volume rendering of the deep ocean water asteroid impact dataset. A) In our system, the progressive rendering is done by breaking the volume interval into smaller segments, and only compute one segment per frame. B) Additionally, our system can also break the framebuffer into smaller tiles, and only render one tile at a time. Both method allows our rendering system to significantly reduce memory footprints."
date: 2022-06-13
collection: "publications"
---

### Abstract
Modern simulations and experiments can produce massive amounts of high-fidelity data that are challenging to transport and visualize interactively. We have designed a data streaming system to support interactive visualization of large volume data. Our streaming system design is unique in its flexibility to support diverse data organizations and its coupling with a highly efficient CPU-based ray-tracing renderer. In this paper, we present our streaming and rendering design and demonstrate the efficacy of our system with progressive rendering of streaming tree-based AMR (TAMR) volume data and radial basis function (RBF) particle volume data. With our system, interactive visualization can be achieved using only a mid-range workstation with a single CPU and a modest quantity of RAM.

### Supplementary Video

<p>
<iframe src="https://drive.google.com/file/d/1bKMKPJ7mxvMesXRk0yne2w7FhT7lV7Gt/preview" width="960" height="540" allow="autoplay"></iframe>
</p>

### BibTex

```bibtex
@inproceedings{wu2022flexible,
    booktitle = {Eurographics Symposium on Parallel Graphics and Visualization},
    editor = {Bujack, Roxana and Tierny, Julien and Sadlo, Filip},
    title = {A Flexible Data Streaming Design for Interactive Visualization of Large-Scale Volume Data},
    author = {Wu, Qi and Doyle, Michael J. and Ma, Kwan-Liu},
    year = {2022},
    publisher = {The Eurographics Association},
    ISSN = {1727-348X},
    ISBN = {978-3-03868-175-5},
    DOI = {10.2312/pgv.20221064}
}
```
