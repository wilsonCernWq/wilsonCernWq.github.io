---
title: "Instant Neural Representation for Interactive Volume Rendering"
collection: publications
permalink: /publication/arxiv-instant-vnr
excerpt: 'Neural networks have shown great potential in compressing volume data for visualization. However, due to the high cost of training and inference, such volumetric neural representations have thus far only been applied to offline data processing and non-interactive rendering. In this paper, we demonstrate that by simultaneously leveraging modern GPU tensor cores, a native CUDA neural network framework, and a well-designed rendering algorithm with macro-cell acceleration, we can interactively ray trace volumetric neural representations (10-60fps). Our neural representations are also high-fidelity (PSNR > 30dB) and compact (10-1000x smaller). Additionally, we show that it is possible to fit the entire training step inside a rendering loop and skip the pre-training process completely. To support extreme-scale volume data, we also develop an efficient out-of-core training strategy, which allows our volumetric neural representation training to potentially scale up to terascale using only an NVIDIA RTX 3090 workstation.'
date: 2022-10-24
venue: 'ArXiv Preprint'
authors: 'Qi Wu, David Bauer, Michael J. Doyle, and Kwan-Liu Ma'
paperurl: 'https://drive.google.com/file/d/1IyXgzGw7EpHWAsakZoHsE8aU9RqdjHyg/view?usp=sharing'
citation: 'Qi Wu, David Bauer, Michael J. Doyle, and Kwan-Liu Ma. &quot;Instant Neural Representation for Interactive Volume Rendering.&quot; ArXiv Preprint arXiv:2207.11620 (2022).'
---

<a href='https://drive.google.com/file/d/1IyXgzGw7EpHWAsakZoHsE8aU9RqdjHyg/view?usp=sharing'>Download paper here</a>

Neural networks have shown great potential in compressing volume data for visualization. However, due to the high cost of training and inference, such volumetric neural representations have thus far only been applied to offline data processing and non-interactive rendering. In this paper, we demonstrate that by simultaneously leveraging modern GPU tensor cores, a native CUDA neural network framework, and a well-designed rendering algorithm with macro-cell acceleration, we can interactively ray trace volumetric neural representations (10-60fps). Our neural representations are also high-fidelity (PSNR > 30dB) and compact (10-1000x smaller). Additionally, we show that it is possible to fit the entire training step inside a rendering loop and skip the pre-training process completely. To support extreme-scale volume data, we also develop an efficient out-of-core training strategy, which allows our volumetric neural representation training to potentially scale up to terascale using only an NVIDIA RTX 3090 workstation.

Recommended citation: Qi Wu, David Bauer, Michael J. Doyle, and Kwan-Liu Ma. "Instant Neural Representation for Interactive Volume Rendering." ArXiv Preprint arXiv:2207.11620 (2022).

{% raw %}
```
@article{wu2022instant,
 title={Instant Neural Representation for Interactive Volume Rendering},
 author={Wu, Qi and Doyle, Michael J and Bauer, David and Ma, Kwan-Liu},
 journal={arXiv preprint arXiv:2207.11620},
 year={2022}
}
```
{% endraw %}
