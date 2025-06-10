# Accessing Data in a *PharmacoSet*

!!! tip "This is a quick reference"

    For a more detailed introduction to PharmacoSet, see the
    *Vignettes* and *Reference Manual* in the
    [*PharmacoGx* package](https://bioconductor.org/packages/PharmacoGx/).

## Quick start: Load a tiny demo PSet

Accessor functions give you a clean, read‑only (or read‑write) gateway to
each slot. Use them instead of poking the S4 object directly.

```r
# Get started by setting up PharmacoGx
library(PharmacoGx)
data(CCLEsmall)        # ships with the package
treatmentInfo(CCLEsmall)  # peek at treatment metadata
```

??? info "What *is* an accessor?"

    Accessors are S4 methods whose names read like plain English:

    - `treatmentInfo()` returns (or sets) the `TreatmentResponse`
    - `molecularProfiles()` returns (or sets) the `MultiAssayExperiment` 

    They shield you from slot names, so your code keeps working even if the
    class internals change.
---

## Treatments

Retrieve or update treatment metadata in a single call.

??? note "Migration to Pharmacoset v2.0"
    The `drugInfo` and `drugNames` slots are deprecated in Pharmacoset v2.0.
    Use the new accessors below instead.  
    - `treatmentInfo()` replaces `drugInfo()`  
    - `treatmentNames()` replaces `drugNames()`

    Similarly, `sampleInfo` and `sampleNames` are now used for sample metadata,
    instead of `cellInfo` and `cellNames`.

=== "treatmentInfo"
    One‑row‑per‑treatment `data‑frame` holding IDs, names, targets, etc.  
    ```r
    # Getter
    info <- treatmentInfo(pSet)
    # Setter
    treatmentInfo(pSet) <- info
    ```
=== "treatmentNames"
    Character vector of treatment IDs.  
    ```r
    names <- treatmentNames(pSet)
    treatmentNames(pSet) <- names
    ```

## Samples

Keep track of cell‑line annotations without wrangling rows
manually.

=== "sampleInfo"
    Per‑sample metadata table (cell‑line, tissue, etc.).  
    ```r
    sampleInfo(pSet)
    ```
=== "sampleNames"
    Character vector of sample IDs.  
    ```r
    sampleNames(pSet)
    ```

## Molecular profiles

Treat multi‑omics data like a tidy list of matrices plus
metadata.

First, we need to know what data types are available, then we can
dive into the actual data.

??? info "Migration to Pharmacoset v2.0"
    The `molecularProfiles` slot is now a `MultiAssayExperiment` (MAE) object
    from **SummarizedExperiment**. It holds multiple assays (e.g. RNA, CNV)
    with their own metadata.

    The old approach was just a list of `SummarizedExperiment` objects,
    which is less flexible and harder to subset/filter.

=== "Get available data types"
    List available omics layers (`"rna"`, `"cnv"`, …).  
    ```r
    mDataNames(pSet)
    ```

??? example "Why two steps?"
    First ask *what* data types exist (`mDataNames`), then dive
    into a matrix with `molecularProfiles`.

=== "molecularProfiles"
    Grab an assay matrix for a chosen layer.  
    ```r
    expr <- molecularProfiles(pSet, "rna", "exprs")
    ```
=== "featureInfo"
    Row‑level feature metadata (`rowData`).  
    ```r
    featureInfo(pSet, "rna")
    ```
=== "phenoInfo"
    Column‑level sample metadata (`colData`).  
    ```r
    phenoInfo(pSet, "rna")
    ```

## Treatment Response

??? info "Migration to PharmacoSet v2.0"
    The `treatmentResponse(pSet)` accessor now returns a
    **TreatmentResponseExperiment** (TRE) object from **CoreGx**—a
    `SummarizedExperiment`‑derived container with assays (e.g. viability)
    plus `rowData` (samples) and `colData` (treatments).

    A TRE supports multi‑drug screens and high‑dimensional synergy analyses
    introduced in PharmacoGx 3.0.

    It replaces the old list‑based sensitivity slot, though legacy getters
    still work for stability.

=== "`TreatmentResponseExperiment` accessors"
    Modern workflow using a `TreatmentResponseExperiment` (TRE).  
    ```r
    tre <- treatmentResponse(pSet)

    # Get the names of the assays
    assayNames(tre)

    # Access any assay (i.e 'viability', 'computed_profiles', 'published_profiles')
    head(assay(tre, "viability"))
    rowData(tre)          # sample metadata
    colData(tre)          # treatment metadata
    ```
=== "legacy accessors"
    Old functions remain for backward compatibility.  
    ```r
    sensitivityInfo(pSet)
    sensitivityProfiles(pSet)
    sensitivityRaw(pSet)
    ```

## FAQ

* **Missing assay name?** If you skip the `assay` arg, `molecularProfiles`
  defaults to the first assay in that SummarizedExperiment.  
* **Deprecated slots?** `datasetType` and `perturbation` remain for
  backward compatibility; lean on *accessors* instead.
