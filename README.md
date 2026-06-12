# Climate Conflict in Indonesia

Research project on the causal effects of wildfire exposure on conflict probability and conflict intensity in Indonesia, with a focus on identifying whether climate-related environmental shocks can meaningfully increase the risk of social unrest and violence.

A draft working paper based on this project is available on Overleaf:  
[https://www.overleaf.com/read/wmwmpqvgtfvv#38ab4a](https://www.overleaf.com/read/wmwmpqvgtfvv#38ab4a)

This repository organizes the data, analysis notebooks, literature, and presentation materials for an ongoing empirical project using panel data methods, including fixed effects and wind-based instrumental variables approaches.

---

## Overview

Climate change may shape conflict indirectly by increasing environmental stress, disrupting livelihoods, worsening air quality, and heightening competition over scarce resources. This project studies that relationship in the Indonesian context by examining whether wildfire exposure affects both the likelihood and intensity of conflict.

The empirical goal is to move beyond simple correlation and estimate causal effects. To do that, the project combines geospatial and panel data with econometric strategies designed to isolate exogenous variation in wildfire exposure.

---

## Research Question

The core question of the project is:

**What is the causal effect of wildfire exposure on conflict probability and conflict intensity in Indonesia?**

Related questions include:

- Do wildfire shocks increase the probability that conflict occurs in a district-month?
- Do wildfire shocks increase the intensity of conflict where conflict already exists?
- Are these effects stronger in particular regions or seasons?
- Can wind patterns be used as an instrument to identify plausibly exogenous wildfire exposure?

---

## Methodology

The project uses panel data methods to estimate the relationship between wildfire exposure and conflict outcomes over time and across locations.

### Main empirical approaches

- **Fixed effects models** to control for time-invariant district characteristics and common time shocks
- **Time and district fixed effects** to absorb unobserved heterogeneity
- **Wind instrumental variables models** to isolate exogenous variation in wildfire smoke or wildfire exposure
- **Robustness checks** across specifications, outcome definitions, and subsamples

### Why Indonesia?

Indonesia is a strong setting for studying climate-conflict relationships because wildfire activity is both environmentally significant and spatially uneven, while conflict outcomes also vary across districts and time. This creates a useful empirical setting for testing whether climate-related shocks contribute to instability.

---

## 📁 Repository Structure
```text
climate-conflict/
├── analysis/         # Analysis notebooks and empirical modeling
├── data/             # Raw, intermediate, or processed datasets
├── literature/       # Relevant papers, references, and reading materials
├── publications/     # Posters, writeups, slides, or project outputs
├── info.md           # Project notes or metadata
└── Updates.docx      # Progress updates
```

---

## Contents

### `analysis/`
Contains Jupyter notebooks used for estimation, model development, and robustness checks. The GitHub history shows work on a `fixed-effects.ipynb` notebook, indicating that the repository includes notebook-based empirical analysis. [page:1]

### `data/`
Stores project datasets used in the analysis workflow. This likely includes wildfire, conflict, geographic, and merged panel data inputs used for estimation. [page:1]

### `literature/`
Contains background reading and papers relevant to climate-conflict research, environmental shocks, causal inference, and Indonesian political economy. [page:1]

### `publications/`
Houses outward-facing research materials such as posters, slides, or presentation-ready outputs. [page:1]

---

## Current Focus

The current repository description states that the project is focused on studying the causal effects of wildfire exposure on conflict probability and intensity in Indonesia using fixed effects and wind instrumental variables models. [page:1]

In practice, that means the project is centered on building a credible identification strategy for climate-conflict inference rather than only presenting descriptive correlations. The emphasis is on careful econometric design, reproducible notebook-based analysis, and research outputs that can support conference presentations or future paper development. [page:1]

---

## Potential Applications

This research can contribute to several areas:

- **Climate adaptation policy:** Identifying where climate shocks may heighten instability can improve preparedness and targeting.
- **Conflict prevention:** Governments and NGOs may use environmental early-warning indicators to anticipate social unrest.
- **Environmental peacebuilding:** Results can inform interventions that reduce climate vulnerability while also supporting social stability.
- **Academic research:** The project can add evidence to debates over whether and how environmental shocks translate into conflict.
- **Indonesian regional policy:** Findings may help prioritize high-risk districts for mitigation, monitoring, or resilience investments.

---

## Tools and Workflow

The repository is primarily composed of Jupyter Notebook content according to GitHub’s language summary, suggesting that the analysis workflow is notebook-driven. [page:1]

A typical workflow for the project may include:

1. Cleaning and merging wildfire and conflict data
2. Constructing exposure measures
3. Estimating baseline fixed effects models
4. Implementing instrumental variables specifications
5. Producing tables, figures, and presentation materials

---

## Project Status

This is an active research repository with recent commits across analysis and data folders, indicating ongoing development. The repository history visible on GitHub shows dozens of commits and updates to both notebooks and data-related files. [page:1]

---

## Author

**Hariaksha Gunda**  
University of Alabama

Repository: [https://github.com/Hariaksha/climate-conflict](https://github.com/Hariaksha/climate-conflict)

---

## Citation

If you use or reference this repository, please cite it as an unpublished research project unless a formal paper or presentation version is available in the `publications/` folder.

---
