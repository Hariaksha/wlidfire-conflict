# Smoke and Strife: Wildfire Exposure and Social Conflict in Indonesia

Research project estimating the causal effect of wildfire-driven air pollution on social conflict in Indonesia, using a wind-direction instrument to isolate exogenous variation in local smoke exposure.

The current draft working paper is in this repository: [`paper/draft.pdf`](paper/draft.pdf) ([source](paper/draft.tex)).

---

## Overview

Indonesia experiences recurring, large-scale peat and forest fires, driven by land-clearing practices and intensified during El Niño-induced dry seasons, that generate severe transboundary haze across the western archipelago. This project asks whether short-run exposure to that fire-driven air pollution causally affects the incidence of social conflict at the district-month level.

Local fire activity is plausibly endogenous to local conflict: land disputes, weak governance, and economic distress that drive conflict may also drive land-clearing fires. To address this, the project instruments local fire intensity with **upwind fire radiative power**, fire activity in locations whose smoke plumes the prevailing wind would carry toward a district, but which are not themselves affected by that district's local conditions.

---

## Headline Findings

- In the **full sample** (447 districts, Feb. 2015–Jun. 2025), instrumented fire intensity has **no detectable average effect** on conflict event counts, robust to a Poisson IV control-function specification.
- In **conflict-active districts** (those with conflict in ≥30% of sample months), fire intensity has an economically meaningful **negative** effect on conflict events and political-violence events.
- An **event-type decomposition** shows this negative effect is concentrated entirely in **riots and protests**, and is a precise zero for battles and organized violence, consistent with a mechanism in which severe haze disrupts public gathering and street-level collective action rather than organized armed conflict.
- This riots/protests-specific result is the one finding that survives every robustness check applied (a placebo test using a randomly-assigned distant district's instrument, a check for shared regional seasonal cycles, and Conley spatial-correlation standard errors); the broader all-events and political-violence results are comparatively more sensitive to these checks.
- No robust evidence that fire exposure affects conflict-related **fatalities**.

See [`paper/draft.pdf`](paper/draft.pdf) for the full results, the Related Literature section, and detailed robustness analysis.

---

## Data

- **Fire detections:** NASA VIIRS active fire product (Suomi-NPP / NOAA-20, 375m resolution), via NASA FIRMS.
- **Wind fields:** ERA5 reanalysis (Copernicus Climate Data Store), monthly mean 10m wind components.
- **Conflict events:** ACLED (Armed Conflict Location & Event Data Project), Indonesia.
- **Administrative boundaries:** GADM v4.1, Level 2 (kabupaten/kota).

See the Data Availability Statement in the paper for details on reconstructing the raw inputs, most of which exceed GitHub's file-size limits and are linked to their public sources rather than hosted directly.

---

## Methodology

- **Upwind instrument:** for each district-month, the total fire radiative power of detections lying upwind of the district within a fixed radius and angular cone defined by that month's wind direction.
- **Two-stage least squares (IV)** with district and year-month fixed effects, province-clustered standard errors.
- **Poisson IV control function** (two-stage residual inclusion) to address extreme zero-inflation in the conflict-count outcomes.
- **Robustness:** conflict-activity-threshold heterogeneity, event-type decomposition, a placebo/falsification test, a province-by-calendar-month seasonal-confound check, and Conley spatial-correlation standard errors.

---

## 📁 Repository Structure

```text
climate-conflict/
├── paper/             # Draft working paper (draft.tex / draft.pdf), references.bib, figures/
├── analysis/          # Jupyter notebooks: wind-IV.ipynb (main analysis), fixed-effects.ipynb (preliminary correlational evidence), generate_maps.py
├── data/              # Raw and intermediate datasets (administrative, climate, unrest, wellbeing)
├── literature/         # Background papers cited in the project, plus lit-review.xlsx (annotated source list)
├── publications/      # Conference poster and abstract materials (urca-2026)
└── info.md            # Project notes
```

---

## Contents

### `paper/`
The draft working paper, `draft.tex`/`draft.pdf`, with its bibliography (`references.bib`) and figures (`figures/`). This is the primary, up-to-date research output of this project.

### `analysis/`
`wind-IV.ipynb` is the main analysis notebook: data construction, upwind-instrument construction, first- and second-stage IV estimation, and all robustness checks. `fixed-effects.ipynb` contains preliminary, non-instrumented correlational models that motivate the IV design (Section 4 of the paper). `generate_maps.py` produces the geographic figures used in the paper.

### `data/`
Raw and processed datasets: fire detections, wind fields, conflict events, administrative boundaries, and supplementary socioeconomic data.

### `literature/`
PDFs of the papers cited in the paper's Related Literature section and elsewhere, plus `lit-review.xlsx`, an annotated spreadsheet of each source's findings and relevance to this project.

### `publications/`
Poster and abstract materials from prior conference presentations of this work.

---

## Author

**Hariaksha Gunda**
University of Alabama

Repository: [https://github.com/Hariaksha/climate-conflict](https://github.com/Hariaksha/climate-conflict)

---

## Citation

If you use or reference this project, please cite it as an unpublished working paper:

> Gunda, H. *Smoke and Strife: Wind-Instrumented Fire Exposure and Social Conflict in Indonesia.* Working paper, [paper/draft.pdf](paper/draft.pdf).
