---
title: "DIVA: A Declarative and Reactive Language for in situ Visualization"
venue: "@LDAV"
authors: "Qi Wu, Tyson Neuroth, Oleg Igouchkine, Konduri Aditya, Jacqueline H. Chen, and Kwan-Liu Ma"
preprint_url: "https://drive.google.com/file/d/1i_D4LDDRNM_CSOoTgT6iE3a6D2yzbUr4/view?usp=sharing"
official_url: "https://doi.org/10.1109/LDAV51489.2020.00007"
preview: "pubs/ldav2020-diva.png"
teaser: "pubs/ldav2020-diva-teaser.png"
teaser_caption: "Figure 1: A DIVA program is processed through three layers. Users typically specify their program using the declarative interface (left); then the language parser will translate it into an internal DAG representation; this representation will then be interpreted into a low-level dataflow API for execution. A) A DIVA program computes a volume rendering for every 5 timesteps, and saves the rendering on disk. B) The same program in the DAG representation. C) The same program in the low-level API. Because the C++ API is not declarative, in part C), statements have to be executed in order. Moreover, because C++ does not track data dependencies automatically, all variables declared in C) should be wrapped by lifting operators (e.g., divaCreateSource). D) The hierarchy of primitives defined by the low-level dataflow API: All values in DIVA are signals; values depending on external inputs are sources; values returning to the environment are actions (e.g., a saved image file); triggers are special primitives that decide which actions to compute based on predicates; rest values are internal to the workflow and are represented by either pure (i.e., DivaPureOp) or impure functions (i.e., DivaImpure)."
date: 2020-10-25
collection: "publications"
---

### Abstract

The use of adaptive workflow management for in situ visualization and analysis has been a growing trend in large-scale scientific simulations. However, coordinating adaptive workflows with traditional procedural programming languages can be difficult because system flow is determined by unpredictable scientific phenomena, which often appear in an unknown order and can evade event handling. This makes the implementation of adaptive workflows tedious and error-prone. Recently, reactive and declarative programming paradigms have been recognized as well-suited solutions to similar problems in other domains. However, there is a dearth of research on adapting these approaches to in situ visualization and analysis. With this paper, we present a language design and runtime system for developing adaptive systems through a declarative and reactive programming paradigm. We illustrate how an adaptive workflow programming system is implemented using our approach and demonstrate it with a use case from a combustion simulation.

### Presentation

<p>
<iframe src="https://drive.google.com/file/d/1BGlRIn7rt6gWRKLj7oNaRyGfUMQblnQM/preview" width="960" height="540" allow="autoplay"></iframe>
</p>

### BibTex

```bibtex
@inproceedings{wu2020diva,
    title={DIVA: A Declarative and Reactive Language for in situ Visualization},
    author={Wu, Qi and Neuroth, Tyson and Igouchkine, Oleg and Aditya, Konduri and Chen, Jacqueline H and Ma, Kwan-Liu},
    booktitle={2020 IEEE 10th Symposium on Large Data Analysis and Visualization (LDAV)},
    pages={1--11},
    year={2020},
    organization={IEEE}
}
```
