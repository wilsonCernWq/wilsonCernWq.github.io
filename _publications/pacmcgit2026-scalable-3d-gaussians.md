---
title: "Scalable Training and Rendering of 3D Gaussians for Large-Scale Scientific Data"
venue: "@PACMCGIT"
authors: "Andres Sewell, Mengjiao Han, Qi Wu, and Steve Petruzza"
abstract: >-
  We present a communication-free distributed 3D Gaussian Splatting framework
  for large scientific volumes. Native simulation partitions are optimized
  independently, clipped geometrically at render time, and composited with IceT.
excerpt: "A communication-free distributed 3D Gaussian Splatting framework that scales scientific-volume training to 256 GPUs and accelerates time-series updates through temporal reuse."
preprint_url: "https://drive.google.com/file/d/1eGrxwmrtRIwIEWGE2skGLEkPvjahyoIg/view?usp=sharing"
official_url: "https://dl.acm.org/doi/10.1145/3820022"
preview: "pubs/pacmcgit2026-scalable-3d-gaussians.jpg"
teaser: "pubs/pacmcgit2026-scalable-3d-gaussians-teaser.jpg"
teaser_width: "96%"
teaser_alt: "Five reconstructed timesteps of the Johns Hopkins Turbulence dataset with training time and PSNR"
teaser_caption: "Five timesteps of the 6.0 GB Johns Hopkins Turbulence dataset trained on 128 GPUs of the Polaris supercomputer. Reusing the previous timestep reduces training from 9.3 minutes to about 2.1 minutes while retaining more than 42 dB PSNR."
project_page_style: true
date: 2026-07-01
collection: "publications"
---

<p class="project-lede"><strong>This framework maps the native spatial decomposition of an HPC simulation directly onto independent 3D Gaussian optimization tasks.</strong> Training requires no model synchronization or device-to-device exchange; boundary continuity is recovered with ghost cells and fragment-level clipping, and the local renders are combined only during sort-last compositing.</p>

<div class="project-metrics" aria-label="Key results">
  <div class="project-metric">
    <span class="project-metric__value">256 GPUs</span>
    <span class="project-metric__label">largest weak-scaling experiment with one subdomain per GPU</span>
  </div>
  <div class="project-metric">
    <span class="project-metric__value">0</span>
    <span class="project-metric__label">inter-GPU synchronization operations during model training</span>
  </div>
  <div class="project-metric">
    <span class="project-metric__value">161.3x</span>
    <span class="project-metric__label">maximum aggregate storage reduction with bounded MCMC</span>
  </div>
  <div class="project-metric">
    <span class="project-metric__value">84%</span>
    <span class="project-metric__label">maximum per-timestep training reduction through temporal reuse</span>
  </div>
</div>

### Abstract

The application of machine learning techniques to 3D Gaussian Splatting (3DGS) has enabled high-fidelity interactive rendering of complex 3D scenes on modest compute resources, offering significant potential for scientific visualization. However, reconstructing large scientific volumes at high fidelity exceeds the memory capacity of individual GPUs. Existing distributed 3DGS frameworks target urban scenes and depend on global scene analysis or frequent all-to-all communication, limiting their scalability on HPC clusters.

We present a distributed 3DGS training and rendering framework designed for large-scale scientific volume data. The method uses the native domain decomposition of HPC simulations and treats each spatial partition as an independent optimization task. It further exploits temporal coherence to accelerate later simulation timesteps. Experiments demonstrate near-ideal weak scaling by eliminating synchronization overhead. The study also characterizes the trade-off between standard 3DGS optimization, which provides higher fidelity with growing primitive counts, and MCMC optimization, which bounds model size at a dataset-dependent quality cost.

### Why Scientific Data Is Different

Distributed simulations already partition their data across ranks, know the world-space bounds of each partition, and commonly maintain halo regions for numerical methods. A scientific visualization pipeline can use that structure directly. Photogrammetry-oriented distributed 3DGS systems instead maintain a globally consistent scene through parameter exchange or centralized image and gradient aggregation.

<div class="project-table-wrap">
  <table class="project-table">
    <thead>
      <tr>
        <th scope="col">System</th>
        <th scope="col">Optimization unit</th>
        <th scope="col">Training communication</th>
        <th scope="col">Observed scaling behavior</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Grendel-GS</th>
        <td>Globally coordinated model</td>
        <td>NCCL all-to-all or all-reduce</td>
        <td>Communication bottleneck beyond 64 GPUs</td>
      </tr>
      <tr>
        <th scope="row">RetinaGS</th>
        <td>Partitioned workers with a central manager</td>
        <td>Image collection, compositing, and gradient redistribution</td>
        <td>More than 3,800 seconds at 128 GPUs; 256-GPU runs omitted</td>
      </tr>
      <tr>
        <th scope="row">This work</th>
        <td>Independent model per simulation subdomain</td>
        <td><strong>None during training</strong></td>
        <td><strong>Near-constant time through 256 GPUs</strong></td>
      </tr>
    </tbody>
  </table>
</div>

### System Design

<div class="project-steps" aria-label="Distributed training and rendering pipeline">
  <div class="project-step">
    <span class="project-step__number">01</span>
    <strong>Decompose</strong>
    <p>Use native simulation partitions or transfer-function-weighted recursive bisection, plus one ghost-cell layer.</p>
  </div>
  <div class="project-step">
    <span class="project-step__number">02</span>
    <strong>Generate locally</strong>
    <p>Sample initial Gaussians from voxels and render 306 deterministic training views for each domain.</p>
  </div>
  <div class="project-step">
    <span class="project-step__number">03</span>
    <strong>Train independently</strong>
    <p>Assign one subdomain to each GPU and optimize using only local data, images, and gradients.</p>
  </div>
  <div class="project-step">
    <span class="project-step__number">04</span>
    <strong>Render globally</strong>
    <p>Clip fragments to primary domain bounds and use IceT to composite local color and depth buffers.</p>
  </div>
</div>

<figure class="project-figure" style="--figure-width:96%;">
  <img src="/images/pubs/pacmcgit2026-scalable-3d-gaussians-system.png" alt="Five-stage distributed 3D Gaussian training and rendering architecture" loading="lazy">
  <figcaption>The system follows the simulation's spatial decomposition from local ground-truth generation through communication-free training. Communication is deferred to the final sort-last rendering stage.</figcaption>
</figure>

#### Domain decomposition and initialization

The evaluation harness recursively bisects the volume along its longest physical axis, selecting split planes that balance accumulated transfer-function opacity rather than raw voxel count. Highly visible structures receive smaller spatial partitions, while mostly transparent regions receive larger ones. Each partition receives the same initial primitive budget.

One ghost-cell layer extends each partition across shared boundaries. This supplies both neighboring optimizers with the same underlying scalar field around the split plane. Production simulation codes already maintain such halo data, so the method does not require a new category of boundary storage. Each subdomain initializes from 250,000 randomly sampled voxel centers and uses 300 Fibonacci-sphere views plus six axis-aligned views for deterministic 360-degree coverage.

#### Communication-free optimization

Every GPU trains a self-contained local 3DGS model from its own volume slice, ground-truth images, and gradients. No parameter consensus, gradient reduction, or global loss is computed during optimization. The wall-clock time is therefore governed by the slowest local partition rather than by a growing collective-communication cost.

### Seamless Domain Boundaries

Independent Gaussians naturally extend beyond their assigned partitions. Discarding a Gaussian by its center creates gaps, while rendering its full projected footprint produces overlapping seams. The method instead modifies the 3DGUT rasterizer to intersect each ray with the primary domain's axis-aligned bounding box. Contributions outside the box are rejected per fragment, retaining the useful portion of a Gaussian that straddles the boundary.

<figure class="project-figure" style="--figure-width:85%;">
  <img src="/images/pubs/pacmcgit2026-scalable-3d-gaussians-fragment-clipping.png" alt="Comparison of projected 2D culling and 3D ray-based fragment clipping" loading="lazy">
  <figcaption>Projected 2D culling loses the spatial information needed to cut a Gaussian correctly. Ray-box testing in 3D rejects only the fragments outside the local domain.</figcaption>
</figure>

<figure class="project-figure" style="--figure-width:88%;">
  <div class="project-image-grid" role="group" aria-label="Boundary handling comparison on the Blunt Fin dataset">
    <div class="project-image-grid__item">
      <img src="/images/pubs/pacmcgit2026-scalable-3d-gaussians-boundary-ground-truth.png" alt="Ground-truth Blunt Fin rendering" loading="lazy">
      <span>Ground truth</span>
    </div>
    <div class="project-image-grid__item">
      <img src="/images/pubs/pacmcgit2026-scalable-3d-gaussians-boundary-no-culling.png" alt="Blunt Fin rendering without boundary culling" loading="lazy">
      <span>No culling</span>
    </div>
    <div class="project-image-grid__item">
      <img src="/images/pubs/pacmcgit2026-scalable-3d-gaussians-boundary-center-culling.png" alt="Blunt Fin rendering with center-based culling" loading="lazy">
      <span>Center culling</span>
    </div>
    <div class="project-image-grid__item">
      <img src="/images/pubs/pacmcgit2026-scalable-3d-gaussians-boundary-fragment-clipping.png" alt="Blunt Fin rendering with fragment clipping" loading="lazy">
      <span>Fragment clipping</span>
    </div>
  </div>
  <figcaption>Boundary ablation on Blunt Fin. No culling creates opaque overlap lines; center-based culling removes valid Gaussian support; fragment clipping reconstructs a continuous result.</figcaption>
</figure>

### Evaluation at Scale

<div class="project-scope" aria-label="Evaluation setup">
  <div><strong>Polaris supercomputer</strong><span>Four NVIDIA A100 GPUs per node</span></div>
  <div><strong>1-256 domains</strong><span>Strict one-GPU-per-subdomain mapping</span></div>
  <div><strong>4 static volumes</strong><span>16 MB Skull through 7.5 GB RMI</span></div>
  <div><strong>5 temporal volumes</strong><span>6.0 GB per Johns Hopkins Turbulence step</span></div>
</div>

<figure class="project-figure" style="--figure-width:78%;">
  <img src="/images/pubs/pacmcgit2026-scalable-3d-gaussians-results.png" alt="Four scientific datasets reconstructed with 256 independently trained domains" loading="lazy">
  <figcaption>Composited 256-GPU results for Skull, Kingsnake, Chameleon, and Richtmyer-Meshkov Instability. Each image combines 256 independently trained and clipped models.</figcaption>
</figure>

The communication-free GS pipeline maintains roughly constant per-dataset training time after the initial transition from one to multiple domains. Grendel-GS is faster at small GPU counts but its communication cost rises sharply after 64 GPUs. RetinaGS exceeds 3,800 seconds at 128 GPUs across completed runs, approximately 7.5-9x slower than this method, while its RMI reconstruction does not converge.

<figure class="project-figure" style="--figure-width:70%;">
  <img src="/images/pubs/pacmcgit2026-scalable-3d-gaussians-scaling.png" alt="Training time and PSNR scaling curves for four datasets and four distributed methods" loading="lazy">
  <figcaption>Weak-scaling comparison. The proposed GS and bounded MCMC variants avoid the increasing synchronization cost seen in Grendel-GS and RetinaGS; standard GS retains the strongest fidelity on complex data.</figcaption>
</figure>

### Standard GS or Bounded MCMC?

Independent standard-GS optimizers can each densify freely. This gives them enough capacity for high-frequency structures, but their aggregate primitive count grows with the number of domains. The MCMC variant divides the primitive count of a monolithic GS baseline among all subdomains, keeping the global budget nearly constant and reducing both training time and storage.

<div class="project-table-wrap">
  <table class="project-table">
    <thead>
      <tr>
        <th scope="col">Dataset at 256 GPUs</th>
        <th scope="col">GS PSNR</th>
        <th scope="col">GS time</th>
        <th scope="col">MCMC PSNR</th>
        <th scope="col">MCMC time</th>
        <th scope="col">MCMC storage reduction</th>
      </tr>
    </thead>
    <tbody>
      <tr><th scope="row">Skull</th><td><strong>42.70 dB</strong></td><td>454.66 s</td><td>35.32 dB</td><td><strong>265.31 s</strong></td><td>60.07x</td></tr>
      <tr><th scope="row">Kingsnake</th><td><strong>46.48 dB</strong></td><td>547.35 s</td><td>29.51 dB</td><td><strong>318.76 s</strong></td><td>112.5x</td></tr>
      <tr><th scope="row">Chameleon</th><td><strong>44.57 dB</strong></td><td>476.43 s</td><td>41.23 dB</td><td><strong>290.57 s</strong></td><td><strong>161.3x</strong></td></tr>
      <tr><th scope="row">RMI</th><td><strong>39.31 dB</strong></td><td>718.45 s</td><td>22.15 dB</td><td><strong>263.37 s</strong></td><td>71.6x</td></tr>
    </tbody>
  </table>
</div>

<p class="project-table-note">Storage reduction compares aggregate standard-GS and bounded-MCMC model footprints at 256 domains. Training time is the total time-to-solution reported by the evaluation.</p>

<p class="project-note"><strong>The memory bound is not free.</strong> MCMC works well when a downloadable model size is a hard constraint, but a monolithic primitive budget can starve complex local optimizers. On turbulent RMI data, bounded MCMC falls to roughly 22 dB at 256 domains; unrestricted GS is the appropriate choice when fidelity is the priority.</p>

### Temporal Fine-Tuning

The first simulation step is trained from voxel initialization for 30,000 iterations. Each later step starts from the optimized positions, covariances, spherical harmonics, and colors of the preceding model and fine-tunes for 4,000 iterations. At 128 GPUs, the baseline takes 557 seconds and subsequent steps take about 124-127 seconds.

<figure class="project-figure" style="--figure-width:80%;">
  <img src="/images/pubs/pacmcgit2026-scalable-3d-gaussians-temporal-scaling.png" alt="Total sequence training time and PSNR across one to 128 GPUs" loading="lazy">
  <figcaption>Five-step Johns Hopkins Turbulence sequence. Spatial scaling reduces total sequence time, while temporal reuse keeps later steps inexpensive and preserves high reconstruction quality.</figcaption>
</figure>

<div class="project-table-wrap">
  <table class="project-table">
    <thead>
      <tr>
        <th scope="col">128-GPU timestep</th>
        <th scope="col">Initialization</th>
        <th scope="col">Iterations</th>
        <th scope="col">PSNR</th>
        <th scope="col">Training time</th>
      </tr>
    </thead>
    <tbody>
      <tr><th scope="row">1000</th><td>Voxel samples</td><td>30,000</td><td>45.20 dB</td><td>557.06 s</td></tr>
      <tr><th scope="row">1001</th><td>Previous step</td><td>4,000</td><td><strong>45.25 dB</strong></td><td>125.87 s</td></tr>
      <tr><th scope="row">1010</th><td>Previous step</td><td>4,000</td><td>45.14 dB</td><td>126.60 s</td></tr>
      <tr><th scope="row">1100</th><td>Previous step</td><td>4,000</td><td>42.83 dB</td><td><strong>123.36 s</strong></td></tr>
      <tr><th scope="row">1400</th><td>Previous step</td><td>4,000</td><td>42.14 dB</td><td>124.19 s</td></tr>
    </tbody>
  </table>
</div>

Quality declines as the physical interval between test frames grows. Fine-tuning every step sequentially and fine-tuning each step directly from the original baseline show similar degradation, indicating that physical change, rather than compounding optimization drift, is the dominant cause.

<figure class="project-figure" style="--figure-width:82%;">
  <img src="/images/pubs/pacmcgit2026-scalable-3d-gaussians-temporal-drift.png" alt="Temporal fine-tuning quality and training cost compared with independent training" loading="lazy">
  <figcaption>Temporal-drift study. Sequential reuse and direct reuse from the initial model follow similar quality trajectories, while both cost a fraction of independent 30,000-iteration training.</figcaption>
</figure>

### Practical Configuration

<div class="project-parameter-grid" aria-label="Recommended experimental settings">
  <div class="project-parameter"><strong>306 views</strong>300 Fibonacci-sphere cameras plus six axis-aligned views provide reliable coverage.</div>
  <div class="project-parameter"><strong>1024 x 1024</strong>Doubling image resolution costs 1.5-2.5x more with negligible PSNR benefit.</div>
  <div class="project-parameter"><strong>35 dB target</strong>PSNR-based early termination avoids over-optimizing visually simple subdomains.</div>
  <div class="project-parameter"><strong>2k-4k steps</strong>Four thousand fine-tuning steps are conservative; 2,000 often retain similar quality at roughly half the cost.</div>
</div>

### Limitations

- **Aggregate model growth:** unrestricted standard GS can produce a distributed model larger than the source volume. MCMC bounds storage but can underfit high-frequency data.
- **Visual-complexity sensitivity:** small, low-detail partitions may lack enough local features to constrain optimization, reducing PSNR at very high domain counts.
- **Tail latency:** overall training finishes when the slowest partition converges. A future asynchronous task queue could improve utilization.
- **Distributed rendering:** local models render at 237-450 FPS at single-domain scale, but IceT compositing limits the 256-domain result to roughly 9-11 FPS.
- **No direct concatenation:** fragment clipping depends on per-domain bounds, so local models cannot be joined into one artifact without a global boundary-aware fine-tuning pass.

### BibTeX

~~~bibtex
@article{sewell2026scalable,
  author = {Sewell, Andres and Han, Mengjiao and Wu, Qi and Petruzza, Steve},
  title = {Scalable Training and Rendering of 3D Gaussians for Large-Scale Scientific Data},
  journal = {Proceedings of the ACM on Computer Graphics and Interactive Techniques},
  year = {2026},
  volume = {9},
  number = {4},
  articleno = {55},
  numpages = {25},
  publisher = {Association for Computing Machinery},
  doi = {10.1145/3820022},
  url = {https://doi.org/10.1145/3820022}
}
~~~
