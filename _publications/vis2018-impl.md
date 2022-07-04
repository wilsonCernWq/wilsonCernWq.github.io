---
title: "CPU Isosurface Ray Tracing of Adaptive Mesh Refinement Data"
collection: publications
permalink: /publication/vis2018-impl
excerpt: 'Adaptive mesh refinement (AMR) is a key technology for large-scale simulations that allows for adaptively changing the simulation mesh resolution, resulting in significant computational and storage savings. However, visualizing such AMR data poses a significant challenge due to the difficulties introduced by the hierarchical representation when reconstructing continuous field values. In this paper, we detail a comprehensive solution for interactive isosurface rendering of block-structured AMR data. We contribute a novel reconstruction strategy-the octant method-which is continuous, adaptive and simple to implement. Furthermore, we present a generally applicable hybrid implicit isosurface ray-tracing method, which provides better rendering quality and performance than the built-in sampling-based approach in OSPRay. Finally, we integrate our octant method and hybrid isosurface geometry into OSPRay as a module, providing the ability to create high-quality interactive visualizations combining volume and isosurface representations of BS-AMR data. We evaluate the rendering performance, memory consumption and quality of our method on two gigascale block-structured AMR datasets.'
date: 2018-10-16
venue: 'IEEE Visualization Conference (VIS)'
paperurl: 'https://drive.google.com/file/d/1cNUeMO8X8hUjtTWlrVxslmeLOdq3vdyJ/view?usp=sharing'
citation: 'Wang, Feng, et al. &quot;CPU isosurface ray tracing of adaptive mesh refinement data.&quot; IEEE Transactions on Visualization and Computer Graphics (2018).'
---

<a href='https://drive.google.com/file/d/1cNUeMO8X8hUjtTWlrVxslmeLOdq3vdyJ/view?usp=sharing'>Download paper here</a>

Adaptive mesh refinement (AMR) is a key technology for large-scale simulations that allows for adaptively changing the simulation mesh resolution, resulting in significant computational and storage savings. However, visualizing such AMR data poses a significant challenge due to the difficulties introduced by the hierarchical representation when reconstructing continuous field values. In this paper, we detail a comprehensive solution for interactive isosurface rendering of block-structured AMR data. We contribute a novel reconstruction strategy-the octant method-which is continuous, adaptive and simple to implement. Furthermore, we present a generally applicable hybrid implicit isosurface ray-tracing method, which provides better rendering quality and performance than the built-in sampling-based approach in OSPRay. Finally, we integrate our octant method and hybrid isosurface geometry into OSPRay as a module, providing the ability to create high-quality interactive visualizations combining volume and isosurface representations of BS-AMR data. We evaluate the rendering performance, memory consumption and quality of our method on two gigascale block-structured AMR datasets.

Recommended citation: Wang, Feng, et al. "CPU isosurface ray tracing of adaptive mesh refinement data." IEEE Transactions on Visualization and Computer Graphics (2018).

{% raw %}
```
@article{wang2018cpu,
author={Wang, Feng and Wald, Ingo and Wu, Qi and Usher, Will and Johnson, Chris R.},
journal={IEEE Transactions on Visualization and Computer Graphics}, 
title={CPU Isosurface Ray Tracing of Adaptive Mesh Refinement Data}, 
year={2019},
volume={25},
number={1},
pages={1142-1151},
doi={10.1109/TVCG.2018.2864850}
}
```
{% endraw %}
