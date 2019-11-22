# Assignment 10- Workflow

This assignment uses the Snakemake workflow to define rules for creating a plot of genes & samples.

To acquire the data files needed:

`$wget GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz`
`$wget GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt`

The `get_gene_counts.py` and `get_tissue_samples.py` scripts were adapted from the scripts with the same name in the lecture code repository.

I was unable to write a working version of `box.py`. This is the script that plots the gene expression distribution across a set of genes for a set of tissue groups. 

The `Snakemake` file contains rules for running `get_gene_counts.py` and `get_tissue_samples.py`. Because I didn't finish box.py, the file only writes the gene text files. This is shown in the `dag.png` snakefile dependency chart.