---
title: "Efficient Compression of Structured and Unstructured Volumes via Learned 3D Gaussian Representation"
venue: "@arxiv"
authors: "Landon Dyken, Sharmistha Chakrabarti, Nathan Debardeleben, Steve Petruzza, Qi Wu, Will Usher, and Sidharth Kumar"
abstract: >-
  We introduce W-VEG, an explicit learned 3D Gaussian representation for directly
  queryable compression of structured and unstructured volume data. The model
  jointly represents scalar values and, for unstructured data, the volume domain.
excerpt: "W-VEG compresses structured and unstructured volumes into directly queryable 3D Gaussians, including the domain geometry needed to remove exterior mesh storage."
preprint_url: "https://arxiv.org/pdf/2607.01164"
arxiv_url: "https://arxiv.org/abs/2607.01164"
preview: "pubs/arxiv2026-wveg.jpg"
teaser: "pubs/arxiv2026-wveg-teaser.jpg"
teaser_width: "60%"
teaser_alt: "Ground-truth and W-VEG reconstructions of the Impact volume at 1024x compression"
teaser_caption: "Volume rendering of the 17.9 GB unstructured Impact dataset and its 17.5 MB W-VEG+S reconstruction. At 1024x compression, the model retains 38.43 dB PSNR and 0.984 SSIM while storing both the scalar field and its domain."
project_page_style: true
date: 2026-07-01
collection: "publications"
---

<p class="project-lede"><strong>W-VEG represents a volume as a compact set of learned 3D Gaussians that can be queried directly in world space.</strong> Unlike prior implicit models for unstructured data, W-VEG+S can encode both the scalar field and the shape of its valid domain, removing the need to retain an exterior mesh.</p>

<div class="project-metrics" aria-label="Key results">
  <div class="project-metric">
    <span class="project-metric__value">38.08 dB</span>
    <span class="project-metric__label">average PSNR across the structured-volume benchmarks</span>
  </div>
  <div class="project-metric">
    <span class="project-metric__value">14.91x</span>
    <span class="project-metric__label">average training speedup over IVNR trained for 200k steps</span>
  </div>
  <div class="project-metric">
    <span class="project-metric__value">17.48x</span>
    <span class="project-metric__label">average training speedup over AMGSRN</span>
  </div>
  <div class="project-metric">
    <span class="project-metric__value">1024x</span>
    <span class="project-metric__label">real unstructured compression without exterior surface storage</span>
  </div>
</div>

<figure class="project-figure" style="--figure-width:60%;">
  <img src="/images/pubs/arxiv2026-wveg-impact-reconstruction.jpg" alt="W-VEG reconstruction of the unstructured Impact dataset" loading="lazy">
  <figcaption>The Impact reconstruction sampled from a 17.5 MB W-VEG+S model. The original unstructured volume occupies 17.9 GB.</figcaption>
</figure>

### Abstract

Recent work has shown that implicit neural representations can effectively compress structured and unstructured volume data, allowing direct data querying with a reduced memory footprint. Existing INR methods for unstructured volumes, however, do not encode geometry and therefore require partial mesh storage for later sampling, limiting the achievable compression ratio. We introduce an explicit volume compression model based on learned 3D Gaussian primitives. Collections of 3D Gaussians are reinterpreted as a representation of a volume scalar field, with scalar values reconstructed at arbitrary spatial locations through weighted aggregation of intersecting Gaussians. CUDA-accelerated pipelines support structured and unstructured sampling, continuity-aware losses, and sampling-error-based densification. By encoding both scalar values and domain geometry, the representation removes mesh storage for unstructured volumes while maintaining competitive reconstruction quality and substantially faster training.

### Why Geometry Matters

A structured volume stores values on a regular grid, so its domain is implicit in the grid bounds. An unstructured volume can occupy an arbitrary region and must normally retain mesh geometry to determine whether a query lies inside the domain. Existing unstructured INRs compress the scalar field but still depend on an exterior surface for arbitrary queries and visualization.

For the datasets in this study, that surface alone limits effective compression to roughly 7-24x, regardless of how small the learned scalar model becomes. W-VEG+S instead uses the support of its learned Gaussians to encode the valid domain, allowing the model to answer both questions at once: *is this position defined, and what is its scalar value?*

<figure class="project-figure" style="--figure-width:60%;">
  <img src="/images/pubs/arxiv2026-wveg-volume-types.png" alt="Comparison of sampling on regular structured grids and irregular unstructured volume domains" loading="lazy">
  <figcaption>Structured volumes have an implicit regular domain. Unstructured volumes require an explicit geometry and may be undefined at arbitrary query positions.</figcaption>
</figure>

<div class="project-table-wrap">
  <table class="project-table">
    <thead>
      <tr>
        <th scope="col">Representation</th>
        <th scope="col">Scalar field</th>
        <th scope="col">Domain geometry</th>
        <th scope="col">Exterior surface needed</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Unstructured INR</th>
        <td>Implicit neural function</td>
        <td>No</td>
        <td>Yes</td>
      </tr>
      <tr>
        <th scope="row">W-VEG</th>
        <td>Explicit 3D Gaussians</td>
        <td>No</td>
        <td>Yes</td>
      </tr>
      <tr>
        <th scope="row">W-VEG+S</th>
        <td>Explicit 3D Gaussians</td>
        <td><strong>Yes</strong></td>
        <td><strong>No</strong></td>
      </tr>
    </tbody>
  </table>
</div>

### Gaussian Volume Representation

Each world-space volume encoding Gaussian stores a center $\mu_i$, scale $S_i$, rotation $R_i$, scalar value $v_i$, and learnable weight $w_i$. For the Gaussians that influence a query point $p$, W-VEG estimates the scalar field with normalized Gaussian kernel regression:

$$
\Phi(p) =
\frac{\sum_{i=0}^{N} w_i v_i G_i(p)}
     {\sum_{i=0}^{N} w_i G_i(p)},
\qquad
G_i(p) =
\exp\left(
-\frac{1}{2}(p-\mu_i)^\top R_i^\top S_i^{-2}R_i(p-\mu_i)
\right).
$$

This is a world-space reconstruction rule, not an image-space splatting rule. It makes the compressed model directly sampleable at arbitrary 3D positions and therefore usable by downstream volume algorithms without first reconstructing a dense grid.

<div class="project-parameter-grid" aria-label="Gaussian parameters">
  <div class="project-parameter"><strong>\(\mu_i\)</strong>World-space center</div>
  <div class="project-parameter"><strong>\(S_i, R_i\)</strong>Anisotropic extent and orientation</div>
  <div class="project-parameter"><strong>\(v_i\)</strong>Encoded scalar value</div>
  <div class="project-parameter"><strong>\(w_i\)</strong>Learned influence on nearby queries</div>
</div>

### Training and Sampling

<div class="project-steps" aria-label="W-VEG training pipeline">
  <div class="project-step">
    <span class="project-step__number">01</span>
    <strong>Initialize</strong>
    <p>Seed isotropic Gaussians from a subset of volume vertices and their scalar values.</p>
  </div>
  <div class="project-step">
    <span class="project-step__number">02</span>
    <strong>Sample</strong>
    <p>Evaluate a regular-grid CUDA rasterizer or an irregular-position BVH sampler.</p>
  </div>
  <div class="project-step">
    <span class="project-step__number">03</span>
    <strong>Optimize</strong>
    <p>Backpropagate reconstruction, continuity, and optional domain-boundary losses.</p>
  </div>
  <div class="project-step">
    <span class="project-step__number">04</span>
    <strong>Adapt</strong>
    <p>Prune weak primitives and add Gaussians at high-error samples until the size target is met.</p>
  </div>
</div>

#### Structured volumes

For regular grids, W-VEG adapts tile-based Gaussian rasterization to 3D voxel blocks. It computes each Gaussian's block-aligned bounding box, sorts Gaussian-block intersections by block, and cooperatively loads intersecting Gaussians into shared memory. The backward pass is organized per Gaussian-block intersection, reducing atomic gradient updates by approximately the volume block size.

<figure class="project-figure">
  <img src="/images/pubs/arxiv2026-wveg-structured-pipeline.png" alt="Forward and backward CUDA sampling pipeline for structured volumes" loading="lazy">
  <figcaption>Structured sampling. The forward pass bins Gaussians into grid blocks and estimates cell values; the backward pass reuses the intersection list to accumulate gradients with less atomic contention.</figcaption>
</figure>

#### Unstructured volumes

Irregular sample positions cannot use the regular-grid pipeline. W-VEG instead builds a CUDA-accelerated bounding volume hierarchy over the requested sample positions. One warp cooperatively traverses the BVH for each Gaussian, computes contributions only for intersected leaves, and atomically accumulates values before normalization. The same traversal structure is reused in the backward pass.

<figure class="project-figure">
  <img src="/images/pubs/arxiv2026-wveg-unstructured-pipeline.png" alt="BVH-based sampling pipeline for arbitrary positions in unstructured volumes" loading="lazy">
  <figcaption>Unstructured sampling. A BVH over arbitrary query positions is traversed with each Gaussian's bounding box, avoiding any regular-grid assumption.</figcaption>
</figure>

#### Error-guided densification

The model has a fixed compression target but a dynamic spatial allocation. Every 100 iterations after iteration 500, the method can prune low-weight Gaussians and use the freed capacity in poorly reconstructed regions. The proposed strategy creates new Gaussians directly at the $k$ samples with highest reconstruction error, which is especially effective when spatial complexity is highly nonuniform.

<figure class="project-figure" style="--figure-width:76%;">
  <img src="/images/pubs/arxiv2026-wveg-densification.png" alt="Comparison of 3DGS, MCMC, and sample-error-based Gaussian densification" loading="lazy">
  <figcaption>Three density-control strategies evaluated in the paper. Error-based densification places new primitives where the sampled scalar field is reconstructed least accurately.</figcaption>
</figure>

#### Learning the unstructured domain

An explicit Gaussian set can fail in two ways. A false negative occurs when a valid volume position has insufficient Gaussian support; a false positive occurs when the model defines a value outside the original domain. Randomized within-cell sampling and a false-negative loss preserve coverage. W-VEG+S adds samples just outside the surface and a false-positive loss that suppresses support beyond the domain boundary.

<figure class="project-figure" style="--figure-width:72%;">
  <img src="/images/pubs/arxiv2026-wveg-domain-errors.png" alt="False-negative and false-positive domain errors in a Gaussian volume model" loading="lazy">
  <figcaption>False negatives create holes inside the valid domain; false positives extend Gaussian support beyond it. W-VEG+S explicitly penalizes both cases.</figcaption>
</figure>

### Evaluation

<div class="project-scope" aria-label="Evaluation setup">
  <div><strong>4 structured datasets</strong><span>537 MB to 32.21 GB</span></div>
  <div><strong>6 unstructured datasets</strong><span>174 MB to 17.93 GB</span></div>
  <div><strong>3 compression targets</strong><span>64x, 256x, and 1024x</span></div>
  <div><strong>NVIDIA A100</strong><span>In-memory model sizes; no file compression</span></div>
</div>

The evaluation measures volumetric PSNR and end-to-end training time. Structured experiments compare against InstantVNR (IVNR) and AMGSRN. Unstructured experiments compare against UGINR and separately report *real compression ratio*, which includes the exterior surface whenever a model still requires one.

#### Structured-volume results

Across all four datasets and three compression ratios, W-VEG matches the reconstruction quality of substantially longer-trained neural baselines. Its average PSNR is 38.08 dB, compared with 37.76 dB for IVNR 200k and 38.04 dB for AMGSRN.

<div class="project-table-wrap">
  <table class="project-table">
    <thead>
      <tr>
        <th scope="col">Method</th>
        <th scope="col">Average PSNR</th>
        <th scope="col">Training schedule</th>
        <th scope="col">W-VEG speedup</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">W-VEG</th>
        <td><strong>38.08 dB</strong></td>
        <td>Convergence in 1k-4k steps</td>
        <td>Reference</td>
      </tr>
      <tr>
        <th scope="row">IVNR 20k</th>
        <td>36.09 dB</td>
        <td>20k steps</td>
        <td>1.52x</td>
      </tr>
      <tr>
        <th scope="row">IVNR 200k</th>
        <td>37.76 dB</td>
        <td>200k steps</td>
        <td><strong>14.91x</strong></td>
      </tr>
      <tr>
        <th scope="row">AMGSRN</th>
        <td>38.04 dB</td>
        <td>30k steps</td>
        <td><strong>17.48x</strong></td>
      </tr>
    </tbody>
  </table>
</div>

<figure class="project-figure" style="--figure-width:90%;">
  <img src="/images/pubs/arxiv2026-wveg-adaptive-density.jpg" alt="Ground truth, W-VEG reconstruction, error, and Gaussian density for Miranda and Richtmyer volumes" loading="lazy">
  <figcaption>Adaptive memory allocation at 1024x compression. Gaussian density remains relatively uniform for Miranda, but concentrates around Richtmyer's mixing surface where the scalar field is most complex.</figcaption>
</figure>

#### Unstructured-volume results

When only the scalar field is encoded, W-VEG achieves the best PSNR and training time on every tested dataset. On the three smaller volumes, it improves PSNR over UGINR by 33.81 dB on average. On Valley and Earthquake, it improves PSNR by 3.13 dB while training 34.9x faster on average. UGINR cannot train on the 17.9 GB Impact dataset because of memory limits.

The table below isolates the most aggressive 1024x target. Surface-dependent methods retain only 7.6-23.2x real compression on the datasets where they run. W-VEG+S removes that storage and preserves the full 1024x ratio.

<div class="project-table-wrap">
  <table class="project-table">
    <thead>
      <tr>
        <th scope="col">Dataset</th>
        <th scope="col">UGINR PSNR</th>
        <th scope="col">UGINR real CR</th>
        <th scope="col">W-VEG PSNR</th>
        <th scope="col">W-VEG real CR</th>
        <th scope="col">W-VEG+S PSNR</th>
        <th scope="col">W-VEG+S real CR</th>
      </tr>
    </thead>
    <tbody>
      <tr><th scope="row">RBL</th><td>20.72</td><td>9.8x</td><td><strong>75.63</strong></td><td>9.8x</td><td>58.57</td><td><strong>1024x</strong></td></tr>
      <tr><th scope="row">Mito</th><td>23.15</td><td>22.0x</td><td><strong>58.14</strong></td><td>22.0x</td><td>52.58</td><td><strong>1024x</strong></td></tr>
      <tr><th scope="row">SF1</th><td>27.05</td><td>23.2x</td><td><strong>47.49</strong></td><td>23.2x</td><td>45.45</td><td><strong>1024x</strong></td></tr>
      <tr><th scope="row">Valley</th><td>34.32</td><td>18.9x</td><td><strong>35.83</strong></td><td>18.9x</td><td>34.75</td><td><strong>1024x</strong></td></tr>
      <tr><th scope="row">Earthquake</th><td>45.97</td><td>7.6x</td><td><strong>47.13</strong></td><td>7.6x</td><td>44.11</td><td><strong>1024x</strong></td></tr>
      <tr><th scope="row">Impact</th><td>OOM</td><td>OOM</td><td><strong>44.82</strong></td><td>18.3x</td><td>44.77</td><td><strong>1024x</strong></td></tr>
    </tbody>
  </table>
</div>

<p class="project-table-note">PSNR values are volumetric measurements. OOM indicates that UGINR could not train within available GPU memory.</p>

<figure class="project-figure">
  <img src="/images/pubs/arxiv2026-wveg-unstructured-comparison.jpg" alt="Rendered comparison of UGINR, W-VEG, and W-VEG+S on Earthquake and Mito" loading="lazy">
  <figcaption>Neural volume renderings from 1024x models. Without exterior-surface intersection tests, W-VEG+S alone preserves the domain well enough to produce meaningful Earthquake and Mito renderings.</figcaption>
</figure>

#### Densification ablation

At 256x compression and a fixed 4,000-step budget, sample-error-based densification gives the highest PSNR in every structured, unstructured, and domain-encoding configuration tested. Its advantage is largest on the irregular Earthquake datasets.

<div class="project-table-wrap">
  <table class="project-table">
    <thead>
      <tr>
        <th scope="col">Model</th>
        <th scope="col">3DGS heuristic</th>
        <th scope="col">MCMC</th>
        <th scope="col">Error-based</th>
      </tr>
    </thead>
    <tbody>
      <tr><th scope="row">Miranda</th><td>35.88</td><td>33.97</td><td><strong>36.58</strong></td></tr>
      <tr><th scope="row">Chameleon</th><td>45.74</td><td>41.53</td><td><strong>47.86</strong></td></tr>
      <tr><th scope="row">Earthquake</th><td>43.79</td><td>46.97</td><td><strong>52.25</strong></td></tr>
      <tr><th scope="row">Earthquake+S</th><td>42.23</td><td>38.84</td><td><strong>50.85</strong></td></tr>
      <tr><th scope="row">Impact</th><td>46.53</td><td>44.61</td><td><strong>48.74</strong></td></tr>
      <tr><th scope="row">Impact+S</th><td>46.89</td><td>45.27</td><td><strong>48.16</strong></td></tr>
    </tbody>
  </table>
</div>

### Limitations and Future Work

- Reported sizes are in-memory models. The current method does not yet apply quantization, vector coding, or other 3D Gaussian file-compression techniques.
- W-VEG+S learns unstructured boundaries lossily. Domain accuracy depends on geometric complexity and trades off against scalar reconstruction quality at very small model sizes.
- The model supports arbitrary sampling, but task-specific accuracy for operations beyond volume rendering remains to be studied.
- Time-varying and multivariate volumes, signed-distance-based boundary losses, and a renderer designed directly around W-VEG are promising extensions.

<p class="project-note"><strong>Compression-ratio interpretation.</strong> Model CR compares only learned model size with the original volume. Real CR also counts any exterior mesh that must remain available. W-VEG+S is the only evaluated method whose model CR and real CR are identical for unstructured data.</p>

### BibTeX

~~~bibtex
@misc{dyken2026efficient,
  title = {Efficient Compression of Structured and Unstructured Volumes via Learned 3D Gaussian Representation},
  author = {Dyken, Landon and Chakrabarti, Sharmistha and Debardeleben, Nathan and Petruzza, Steve and Wu, Qi and Usher, Will and Kumar, Sidharth},
  year = {2026},
  eprint = {2607.01164},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  doi = {10.48550/arXiv.2607.01164},
  url = {https://arxiv.org/abs/2607.01164}
}
~~~
