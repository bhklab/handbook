# Covidence

[Covidence](https://www.covidence.org/) is an online tool designed to simplify and streamline the systematic review process. It is particularly helpful for managing and screening large numbers of studies in a collaborative, step-by-step workflow.

## Overview

Covidence enables researchers and teams to:

- Import large sets of references from literature searches (e.g., PubMed keyword or MeSH queries).
- Automatically fetch abstracts and full-text PDFs when available.
- Conduct reviews in structured phases: abstract screening, full-text review, and data extraction.

## Workflow

### 0. Setup

- To use Covidence, you should first prepare a list of studies you want to include in your systematic review.
- You can either manually add a list of studies you want to review, or bulk-add a list from a query.
- One way to collect many studies programmatically is to use the PubMed API and export the results in a format that Covidence can import such as EndNote XML.
- Some example code of doing so using Biopython and MeSH queries is seen in [PredictRx](https://github.com/bhklab/PredictRx/tree/main/archive/modules/query_papers) (Note: You must be logged into GitHub and have access to BHKLAB organization).

### 1. Abstract Screening

- Covidence first presents all study abstracts for initial screening.
- Reviewers can approve or exclude papers, with the option to annotate reasons for exclusion.
- Highlight terms of interest in abstracts to help with decision-making.
- Reviews can be configured to require single or multiple reviewers per paper.

### 2. Full-Text Review

- For studies that pass abstract screening, the full text can be reviewed.
- Covidence attempts to retrieve the full PDFs automatically.
- Reviewers again decide whether to include or exclude, with optional comments or rationale.

### 3. Data Extraction / Export

- Once the final set of studies is selected, users can extract relevant data within Covidence.
- Alternatively, the finalized list can be exported for use in other tools or reporting.
- Covidence also saves the review history, which is helpful in producing a consort diagram to show how many studies were included from the beginning, how many were excluded at each stage, and the reasons for exclusion.

## Access

- You can access **one free systematic review** with a UofT email address.
- Only one person needs to create the review; other team members (with free accounts) can be added as collaborators.
- If you need to restart or delete a review, contact Covidence support and they will handle the deletion on your behalf.

For more details, see their official site: [https://www.covidence.org/](https://www.covidence.org/).
