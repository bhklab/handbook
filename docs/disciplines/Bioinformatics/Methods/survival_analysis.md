# Survival Analysis

Survival analysis is a key statistical approach used to study time-to-event outcomes like time until disease progression, relapse, or death. Unlike traditional regression methods, survival analysis accounts for censoring (patients lost to follow-up or still alive at study end) and allows estimation of event probabilities over time.

Survival analysis is often used to:

- Evaluate the impact of potential biomarkers on treatment response and patient outcomes.

- Compare survival curves across patient subgroups (e.g., different mutation profiles, treatments, methods in multicentre studies, etc.).

- Identify predictive markers of drug benefit or toxicity.

- Build models that can use multiomic data to guide precision medicine.

Commonly used methods include:

- **Kaplan–Meier curves**: non-parametric estimates of survival probabilities over time.

- **Cox proportional hazards models**: regression framework to evaluate covariates (e.g., gene mutations, drug classes) affecting hazard rates.

- **Random survival forests / survival support vector machines / deep learning survival models**: machine learning approaches that can capture complex interactions in high-dimensional omics datasets.

Recommended Learning Resources

- 🎥 **Video Playlist** - [Survival Analysis | Concepts and Implementation in R (YouTube)](https://www.youtube.com/playlist?list=PLqzoL9-eJTNDdnKvep_YHIwk2AMqHhuJ0)

    Great introduction to both fundamentals and applied examples in R.

- 📘 **Tutorial in R** – [Survival Analysis in R](https://www.emilyzabor.com/survival-analysis-in-r.html) [| Slide](https://www.emilyzabor.com/talks.html)

    Hands-on guidance with code snippets.

- 📄 **Articles** 
    * [An Introduction to Survival Statistics: Kaplan–Meier Analysis (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5045282/)  
        Clear explanation of Kaplan–Meier methodology with biomedical applications.
    * [Survival Analysis Part I: Basic concepts and first analyses](https://pmc.ncbi.nlm.nih.gov/articles/PMC2394262/)  
      [Survival Analysis Part II: Multivariate data analysis – an introduction to concepts and methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC2394368/)  
      [Survival Analysis Part III: Multivariate data analysis – choosing a model and assessing its adequacy and fit](https://pmc.ncbi.nlm.nih.gov/articles/PMC2376927/)  
      [Survival Analysis Part IV: Further concepts and methods in survival analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC2394469/)  
        A four-part series covering basic methods and terminology in survival analysis. Frequently asked questions are addressed in Part IV. 
