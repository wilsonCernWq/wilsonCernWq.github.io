---
title: "Glyph-Based Multiscale Visualization of Turbulent Multi-Physics Statistics"
venue: "@arxiv"
authors: "Arisa Cowe, Tyson Neuroth, Qi Wu, Martin Rieth, Jacqueline Chen, Myoungkyu Lee, and Kwan-Liu Ma"
official_url: "https://onlinelibrary.wiley.com/doi/full/10.1111/cgf.70134"
arxiv_url: "https://arxiv.org/abs/2506.23092"
preview: "pubs/arxiv-cowe.png"
date: 2025-06-29
collection: "publications"
# optional teaser
teaser: "pubs/arxiv-cowe-teaser.png"
teaser_caption: "Figure 1. Fields $X_i$ are input to the scale decomposition, and surface features are input to the LSRCVT. Aggregation of spectral energy is done for each scale of each field based on the LSRCVT regions. Glyphs are generated interactively based on the aggregated data. The top two glyphs show the strength glyph design, the left encoding mean spectral energy for 1 field and 3 scale bins, and the right encoding spectral energy for 5 fields and 3 scale bins. The one below the two shows the starplot glyph encoding 5 fields and 1 scale bin."
---

### Abstract
We present HyperFLINT (Hypernetwork-based FLow estimation and temporal INTerpolation), a novel deep learning-based approach for estimating flow fields, temporally interpolating scalar fields, and facilitating parameter space exploration in spatio-temporal scientific ensemble data. This work addresses the critical need to explicitly incorporate ensemble parameters into the learning process, as traditional methods often neglect these, limiting their ability to adapt to diverse simulation settings and provide meaningful insights into the data dynamics. HyperFLINT introduces a hypernetwork to account for simulation parameters, enabling it to generate accurate interpolations and flow fields for each timestep by dynamically adapting to varying conditions, thereby outperforming existing parameter-agnostic approaches. The architecture features modular neural blocks with convolutional and deconvolutional layers, supported by a hypernetwork that generates weights for the main network, allowing the model to better capture intricate simulation dynamics. A series of experiments demonstrates HyperFLINT's significantly improved performance in flow field estimation and temporal interpolation, as well as its potential in enabling parameter space exploration, offering valuable insights into complex scientific ensembles.


<figure>
<img src="/images/pubs/arxiv-cowe-figure.png" alt="image">
<figcaption align = "center">Figure 5. The two views on the left show the same information, spectral energy contribution of the highest frequencies for 3 variables, using the starplot glyph (left) and strength glyph (right). The user can interactively switch between the two glyph types. The top two glyphs on the right show averages over all glyphs. While color-based encoding makes it easy to see variation from afar, a user’s perceptual mapping between colors to values can be more complex or error-prone since it requires referencing color legends, and depends on the user’s perception of color. Distance-based value encoding tends to be perceived more intuitively and precisely. The bottom two glyphs on the right show mean spectral energy for 3 variables and 3 scale bins. Using separate color maps for each variable makes it easier to tell different variables apart at a glance, but makes comparing values across variables more difficult. The bottom right glyph uses the same color map for all 3 variables to make comparison easier.</figcaption>
</figure>

<figure>
<img src="/images/pubs/arxiv-cowe-case.png" alt="image">
<figcaption align = "center">Figure 8. Radial glyph rendering with 3 scale bins for temperature in the combustion data. Left zoom: glyphs are configured to show temperature and hydroxyl radical (OH) together (left side and right side of glyph respectively). In some areas, the balance of scale contributions is very similar between the fields, while in other areas we see a major difference, e.g., the purple area where the medium scales are very dominant for OH compared to temperature. The zoomed-in regions are sized to give a sense of what the visualization might look like fully zoomed out on a high-resolution monitor. While the visibility of the glyphs from afar can be limited depending on the coarseness and size of the glyphs, patterns can still be perceived throughout and zoomed in on to see more precise
detail.</figcaption>
</figure>

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
