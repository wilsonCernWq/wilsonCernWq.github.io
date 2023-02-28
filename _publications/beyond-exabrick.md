---
title: "Beyond ExaBricks: GPU Volume Path Tracing of AMR Data"
collection: publications
permalink: /publication/beyond-exabrick
excerpt: 'Adaptive Mesh Refinement (AMR) is becoming a prevalent data representation for scientific visualization. Resulting from large fluid mechanics simulations, the data is usually cell centric, imposing a number of challenges for high quality reconstruction at sample positions. While recent work has concentrated on real-time volume and isosurface rendering on GPUs, the rendering methods used still focus on simple lighting models without scattering events and global illumination. As in other areas of rendering, key to real-time performance are acceleration data structures; in this work we analyze the major bottlenecks of data structures that were originally optimized for camera/primary ray traversal when used with the incoherent ray tracing workload of a volumetric path tracer, and propose strategies to overcome the challenges coming with this.'
date: 2022-11-18
venue: 'ArXiv Preprint'
authors: 'Stefan Zellmann, Qi Wu, Alper Sahistan, Kwan-Liu Ma, and Ingo Wald'
paperurl: 'https://arxiv.org/abs/2211.09997'
citation: 'Zellmann, Stefan, Qi Wu, Alper Sahistan, Kwan-Liu Ma, and Ingo Wald. &quot;Beyond ExaBricks: GPU Volume Path Tracing of AMR Data.&quot; ArXiv preprint arXiv:2211.09997 (2022).'
---

<a href='https://arxiv.org/abs/2211.09997'>Download paper here</a>

Adaptive Mesh Refinement (AMR) is becoming a prevalent data representation for scientific visualization. Resulting from large fluid mechanics simulations, the data is usually cell centric, imposing a number of challenges for high quality reconstruction at sample positions. While recent work has concentrated on real-time volume and isosurface rendering on GPUs, the rendering methods used still focus on simple lighting models without scattering events and global illumination. As in other areas of rendering, key to real-time performance are acceleration data structures; in this work we analyze the major bottlenecks of data structures that were originally optimized for camera/primary ray traversal when used with the incoherent ray tracing workload of a volumetric path tracer, and propose strategies to overcome the challenges coming with this.

Recommended citation: Zellmann, Stefan, Qi Wu, Alper Sahistan, Kwan-Liu Ma, and Ingo Wald. "Beyond ExaBricks: GPU Volume Path Tracing of AMR Data." ArXiv preprint arXiv:2211.09997 (2022).

{% raw %}
```
@article{zellmann2022beyond,
 title={Beyond ExaBricks: GPU Volume Path Tracing of AMR Data},
 author={Zellmann, Stefan and Wu, Qi and Sahistan, Alper and Ma, Kwan-Liu and Wald, Ingo},
 journal={arXiv preprint arXiv:2211.09997},
 year={2022}
}
```
{% endraw %}
