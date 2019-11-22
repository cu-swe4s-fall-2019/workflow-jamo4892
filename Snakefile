GENES = ["SDHB", "MEN1", "KCNH2", "MSH2", "MYL2", "BRCA2"]
TISSUES = ["Brain", "Heart", "Blood", "Skin"]

rule get_gene_counts:
    input:
        "GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz"
    output:
        expand("{gene}_counts.txt", gene=GENES)
    shell: "for gene in {GENES}; do python get_gene_counts.py {input} $gene $gene\_counts.txt; done"
    
rule get_tissue_samples:
    input:
        "GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt"
    output:
        expand("{tissue}_samples.txt", tissue=TISSUES)
    shell:
        "for tissue in {TISSUES}; do python get_tissue_samples.py {input} $tissue $tissue\_samples.txt; done"