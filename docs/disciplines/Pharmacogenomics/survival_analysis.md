# Survival Analysis

Survival analysis is a key statistical approach used to study time-to-event outcomes—for example, time until disease progression, relapse, or death. Unlike traditional regression methods, survival analysis accounts for censoring (patients lost to follow-up or still alive at study end) and allows estimation of event probabilities over time.

In the **pharmacogenomics field**, survival analysis is often used to:

- Evaluate the impact of genomic biomarkers on treatment response and patient outcomes.

- Compare survival curves across patient subgroups (e.g., different mutation profiles).

- Identify predictive markers of drug benefit or toxicity.

- Build models that combine molecular, clinical, and drug-response data to guide precision medicine.

Commonly used methods include:

- **Kaplan–Meier** curves: non-parametric estimates of survival probabilities over time.

- **Cox proportional hazards model**: regression framework to evaluate covariates (e.g., gene mutations, drug classes) affecting hazard rates.

- **Random survival forests / deep learning survival models**: machine learning approaches that can capture complex interactions in high-dimensional omics datasets.

Recommended Learning Resources

- 🎥 **Video Playlist** – [Survival Analysis | Concepts and Implementation in R (YouTube)](https://www.youtube.com/playlist?list=PLqzoL9-eJTNDdnKvep_YHIwk2AMqHhuJ0)

    Great introduction to both fundamentals and applied examples in R.

- 📘 **Tutorial in R** – [Survival Analysis in R](https://www.emilyzabor.com/survival-analysis-in-r.html) [| Slide](https://www.emilyzabor.com/talks.html)

    Hands-on guidance with code snippets.

- 📄 **Article** – [An Introduction to Survival Statistics: Kaplan–Meier Analysis (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5045282/)

    Clear explanation of Kaplan–Meier methodology with biomedical applications.