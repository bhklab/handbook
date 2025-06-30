# Navigating PSets


When you first join the BHKLab Pharmacogenomics (PGx) team, you will likely need to familiarize yourself with our R package [`PharmacoGx`](https://www.bioconductor.org/packages/devel/bioc/html/PharmacoGx.html).  The fundamental object of `PharmacoGx` is the PSet, which is a data structured specifically designed to handle the inputs, results, and meta-data surrounding a [cell line screen](./Cell_Viability_Screens.md). 


PSets can be a bit counter-intuitive at first and so this page provides a rough guide on how to manipulate them. At present we only have tools in `R` to navigate them. 

Before we get into the basics, it is probably worth addressing a natural question: **why use PSets?**  The answer is that pharmacogenomics data is ***messy***.  Research into links between small molecules and compound effect is conducted in many instutitions, each of which has their own idiosyncratic approach to handling and annotating data. PSets allow for standardized nomenclature across datasets, meaning each PSet will ahve the same column names inside its dataframes, a common set of identifiers for drugs and for cell lines, and quality-controlled response measurements. 

This page only covers the basics. Once you've reviewed these snippets you can look at the detailed vignettes [here](https://bhklab.github.io/CBWWorkshop2024/articles/Module1.html).



### Finding PSets


In order to find PSets of interest, you can look at [PharmacoDB](https://pharmacodb.ca) or [ORCESTRA](https://orcestra.ca) and manually download them. In addition PharmacoGx has a the functions `availablePSets()` and `downloadPSet()` functions which can be used to download data. An example call is:

```
downloadPSet(
  name = "CCLE_2015",
  saveDir = "../psets", # change this directory as you see fit
  timeout = 3600,
  verbose = TRUE
)
```



### Loading PSets

The PSets will be downloaded as a `.RDS` file and so will need to be loaded via a call to `readRDS`. If your PSet is stored in `PSet.file.path` then the following script will load it:

```
library(PharmacoGx)
my.PSet <- readRDS(PSet.file.path)

my.PSet <- updateObject(ps) # update to the latest version
```

### Accessing Drug Info

To get information about the drugs used in the PSet you can use the `drugInfo` function to access information about the compounds used in the screen. 

```
drugInfo(my.PSet)
```

If you wanted to get just the compound names and their representations as molecular [SMILES](https://en.wikipedia.org/wiki/Simplified_Molecular_Input_Line_Entry_System) strings, the following will do the trick:
```
drug.data <- as.data.frame(drugInfo(my.PSet))%>% select(treatmentid,smiles)
```


### Accessing Cell Line Info

This is done via the `sampleInfo` function:

```
sample.Data <- sampleInfo(my.PSet)
```

### Accessing Treatment Response Info

To get treatment response information we need the `treatmentResponse` function. This returns a list with several items. To get the data of treament response the following will work:
```
treatmentResponse(my.PSet)$info
```


