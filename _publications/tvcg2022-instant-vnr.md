---
title: "Interactive Volume Visualization via Multi-Resolution Hash Encoding based Neural Representation"
venue: "IEEE Transactions on Visualization and Computer Graphics (TVCG)"
authors: "Qi Wu, David Bauer, Michael J. Doyle, and Kwan-Liu Ma"
abstract: "Neural networks have shown great potential in compressing volume data for visualization. However, due to the high cost of training and inference, such volumetric neural representations have thus far only been applied to offline data processing and non-interactive rendering. In this paper, we demonstrate that by simultaneously leveraging modern GPU tensor cores, a native CUDA neural network framework, and a well-designed rendering algorithm with macro-cell acceleration, we can interactively ray trace volumetric neural representations (10-60fps). Our neural representations are also high-fidelity (PSNR > 30dB) and compact (10-1000x smaller). Additionally, we show that it is possible to fit the entire training step inside a rendering loop and skip the pre-training process completely. To support extreme-scale volume data, we also develop an efficient out-of-core training strategy, which allows our volumetric neural representation training to potentially scale up to terascale using only an NVIDIA RTX 3090 workstation."
preprint_url: "https://drive.google.com/file/d/1IyXgzGw7EpHWAsakZoHsE8aU9RqdjHyg/view?usp=sharing"
arxiv_url: "https://arxiv.org/abs/2207.11620"
official_url: "https://ieeexplore.ieee.org/document/10175377"
preview: "pubs/tvcg2022-instant-vnr.png"
teaser: "pubs/tvcg2022-instant-vnr-teaser.png"
teaser_caption: "Figure 1: A) An overview of our work. The sampling step randomly and uniformly generates sample using the ground truth (GT) data. The ground truth data can be loaded via out-of-core streaming. The training step optimizes the neural network. The rendering step renders the neural network via in-shader or sample-streaming methods. Our approach accommodates both pre-training and online-training. Our novel contributions are highlighted in yellow. B) The architecture of our neural network with the multi-resolution hash grid encoding method."
bibtex: "@article{wu2022instant,\n    author={Wu, Qi and Bauer, David and Doyle, Michael J. and Ma, Kwan-Liu},\n    journal={IEEE Transactions on Visualization and Computer Graphics}, \n    title={Interactive Volume Visualization Via Multi-Resolution Hash Encoding Based Neural Representation}, \n    year={2023},\n    volume={},\n    number={},\n    pages={1-14},\n    doi={10.1109/TVCG.2023.3293121}\n}"
permalink: "/publication/tvcg2022-instant-vnr"
code: "https://github.com/VIDILabs/instantvnr"
date: 2023-6-28
collection: "publications"
---
<!-- ![image](/images/pubs/tvcg-instant-vnr-teaser.png) -->

<!-- 
<figure>
<img src="/images/pubs/tvcg-instant-vnr-teaser.png" alt="image">
<figcaption align = "center">Figure 1: A) An overview of our work. The sampling step randomly and uniformly generates sample using the ground truth (GT) data. The ground truth data can be loaded via out-of-core streaming. The training step optimizes the neural network. The rendering step renders the neural network via in-shader or sample-streaming methods. Our approach accommodates both pre-training and online-training. Our novel contributions are highlighted in yellow. B) The architecture of our neural network with the multi-resolution hash grid encoding method.</figcaption>
</figure> -->

### Video

<p>
<iframe src="https://drive.google.com/file/d/17wSgIm_VsoeGhfyZwMpOnCYy2Mj3ydGv/preview" width="960" height="540" allow="autoplay"></iframe>
</p>

### Note

This manuscript was originally titled "Instant Neural Representation for Interactive Volume Rendering", but in response to the valuable feedback received from reviewers, the title was subsequently revised.
