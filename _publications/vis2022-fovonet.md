---
title: "FoVolNet: Fast Volume Rendering using Foveated Deep Neural Networks (Best Paper Honorable Mentions)"
collection: publications
permalink: /publication/vis2022-fovonet
excerpt: 'Volume data is found in many important scientific and engineering applications. Rendering this data for visualization at high quality and interactive rates for demanding applications such as virtual reality is still not easily achievable even using professional-grade hardware. We introduce FoVolNet—a method to significantly increase the performance of volume data visualization. We develop a cost-effective foveated rendering pipeline that sparsely samples a volume around a focal point and reconstructs the full-frame using a deep neural network. Foveated rendering is a technique that prioritizes rendering computations around the user’s focal point. This approach leverages properties of the human visual system, thereby saving computational resources when rendering data in the periphery of the user’s field of vision. Our reconstruction network combines direct and kernel prediction methods to produce fast, stable, and perceptually convincing output. With a slim design and the use of quantization, our method outperforms state-of-the-art neural reconstruction techniques in both end-to-end frame times and visual quality. We conduct extensive evaluations of the system’s rendering performance, inference speed, and perceptual properties, and we provide comparisons to competing neural image reconstruction techniques. Our test results show that FoVolNet consistently achieves significant time saving over conventional rendering while preserving perceptual quality.'
date: 2022-09-26
venue: 'IEEE Visualization Conference (VIS)'
authors: 'David Bauer, Qi Wu, and Kwan-Liu Ma'
paperurl: 'https://drive.google.com/file/d/1-H7rtC_VH88oNp10kKSCacFE3IU2VCjj/view?usp=sharing'
citation: 'Bauer, David, Qi Wu, and Kwan-Liu Ma. &quot;FoVolNet: Fast Volume Rendering Using Foveated Deep Neural Networks.&quot; IEEE Transactions on Visualization and Computer Graphics (2022).'
---

<a href='https://drive.google.com/file/d/1-H7rtC_VH88oNp10kKSCacFE3IU2VCjj/view?usp=sharing'>Download paper here</a>

Volume data is found in many important scientific and engineering applications. Rendering this data for visualization at high quality and interactive rates for demanding applications such as virtual reality is still not easily achievable even using professional-grade hardware. We introduce FoVolNet—a method to significantly increase the performance of volume data visualization. We develop a cost-effective foveated rendering pipeline that sparsely samples a volume around a focal point and reconstructs the full-frame using a deep neural network. Foveated rendering is a technique that prioritizes rendering computations around the user’s focal point. This approach leverages properties of the human visual system, thereby saving computational resources when rendering data in the periphery of the user’s field of vision. Our reconstruction network combines direct and kernel prediction methods to produce fast, stable, and perceptually convincing output. With a slim design and the use of quantization, our method outperforms state-of-the-art neural reconstruction techniques in both end-to-end frame times and visual quality. We conduct extensive evaluations of the system’s rendering performance, inference speed, and perceptual properties, and we provide comparisons to competing neural image reconstruction techniques. Our test results show that FoVolNet consistently achieves significant time saving over conventional rendering while preserving perceptual quality.

Recommended citation: Bauer, David, Qi Wu, and Kwan-Liu Ma. "FoVolNet: Fast Volume Rendering Using Foveated Deep Neural Networks." IEEE Transactions on Visualization and Computer Graphics (2022).

{% raw %}
```
@artivle{bauer2022fovolnet,
 author={Bauer, David and Wu, Qi and Ma, Kwan-Liu},
 journal={IEEE Transactions on Visualization and Computer Graphics}, 
 title={FoVolNet: Fast Volume Rendering Using Foveated Deep Neural Networks}, 
 year={2022},
 volume={},
 number={},
 pages={1-11},
 doi={10.1109/TVCG.2022.3209498}}
```
{% endraw %}
