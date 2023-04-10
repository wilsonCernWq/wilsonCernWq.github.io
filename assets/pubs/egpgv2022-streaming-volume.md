<!-- ![image](/images/pubs/eurovis2019-tubes-teaser.png) -->

<!-- <figure>
<img src="/images/pubs/egpgv2022-streaming-volume-teaser.png" alt="image">
<figcaption align = "center">Figure 1: Large-scale progressive volume rendering of the deep ocean water asteroid impact dataset. A) In our system, the progressive rendering is done by breaking the volume interval into smaller segments, and only compute one segment per frame. B) Additionally, our system can also break the framebuffer into smaller tiles, and only render one tile at a time. Both method allows our rendering system to significantly reduce memory footprints.</figcaption>
</figure> -->


### Abstract

Modern simulations and experiments can produce massive amounts of high-fidelity data that are challenging to transport and visualize interactively. We have designed a data streaming system to support interactive visualization of large volume data. Our streaming system design is unique in its flexibility to support diverse data organizations and its coupling with a highly efficient CPU-based ray-tracing renderer. In this paper, we present our streaming and rendering design and demonstrate the efficacy of our system with progressive rendering of streaming tree-based AMR (TAMR) volume data and radial basis function (RBF) particle volume data. With our system, interactive visualization can be achieved using only a mid-range workstation with a single CPU and a modest quantity of RAM.
