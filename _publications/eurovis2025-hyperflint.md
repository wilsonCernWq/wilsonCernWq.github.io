---
title: "HyperFLINT: Hypernetwork-based Flow Estimation and Temporal Interpolation for Scientific Ensemble Visualization"
venue: "@EuroVis"
authors: "Hamid Gadirov, Qi Wu, David Bauer, Kwan-Liu Ma, Jos B.T.M. Roerdink, and Steffen Frey"
official_url: "https://onlinelibrary.wiley.com/doi/full/10.1111/cgf.70134"
arxiv_url: "https://arxiv.org/abs/2412.04095"
preview: "pubs/eurovis2025-hyperflint.png"
date: 2025-05-23
collection: "publications"
# optional teaser
# teaser: "pubs/arxiv-hyperinr-teaser.png"
# teaser_caption: "Figure 1: Comparisons between HyperINR and data interpolation for the temporal super-resolution task using the vortices dataset. Listed timesteps are midpoints of different interpolation intervals. HyperINR can directly predict the weights of a regular implicit neural representation (INR) for unseen parameters. The predicted INR is in general more accurate than data interpolation results and can support interactive volumetric path tracing."
---

### Abstract
We present HyperFLINT (Hypernetwork-based FLow estimation and temporal INTerpolation), a novel deep learning-based approach for estimating flow fields, temporally interpolating scalar fields, and facilitating parameter space exploration in spatio-temporal scientific ensemble data. This work addresses the critical need to explicitly incorporate ensemble parameters into the learning process, as traditional methods often neglect these, limiting their ability to adapt to diverse simulation settings and provide meaningful insights into the data dynamics. HyperFLINT introduces a hypernetwork to account for simulation parameters, enabling it to generate accurate interpolations and flow fields for each timestep by dynamically adapting to varying conditions, thereby outperforming existing parameter-agnostic approaches. The architecture features modular neural blocks with convolutional and deconvolutional layers, supported by a hypernetwork that generates weights for the main network, allowing the model to better capture intricate simulation dynamics. A series of experiments demonstrates HyperFLINT's significantly improved performance in flow field estimation and temporal interpolation, as well as its potential in enabling parameter space exploration, offering valuable insights into complex scientific ensembles.

### BibTex
```bibtex
@article{gadirov2025hyperflint,
    author = {Gadirov, Hamid and Wu, Qi and Bauer, David and Ma, Kwan-Liu and Roerdink, Jos B.T.M. and Frey, Steffen},
    title = {HyperFLINT: Hypernetwork-based Flow Estimation and Temporal Interpolation for Scientific Ensemble Visualization},
    journal = {Computer Graphics Forum},
    volume = {44},
    number = {3},
    pages = {e70134},
    doi = {https://doi.org/10.1111/cgf.70134},
    url = {https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.70134},
    eprint = {https://onlinelibrary.wiley.com/doi/pdf/10.1111/cgf.70134},
    year = {2025}
}
```
