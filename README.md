# AAFL
AAFL: automatic association feature learning for gene signature identification of cancer subtypes in single-cell RNA-seq data
![](https://github.com/linxi159/AAFL/blob/main/figures/AAFL.jpg) 

## Description of each directory
data: the preprocessed data from real scRNA-seq data in GEO.

comparison: the utility of comparison with different methods.

results: the preprocessed results and final results.

figures: the plot for AAFL.


## How to setup

* Python (3.6 or later)

* numpy

* sklearn

* pytorch

* NVIDIA GPU + CUDA 11.50 + CuDNN v7.1

* scipy


## Quick example to use AAFL
```
* train and test the model:

* the implementation of gene signature identification between benign cells and tumor cells
python AAFL_main_gene_identification_n2_label.py

* the implementation of gene signature identification across potential cancel subtypes
python AAFL_main_gene_identification_n3_without_label.py

```



