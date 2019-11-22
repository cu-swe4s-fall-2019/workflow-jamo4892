#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest
# Testing framework.

pycodestyle get_gene_counts.py
pycodestyle get_tissue_samples.py
pycodestyle box.py
# Verify formatting standards.

run gene_test python get_gene_counts.py 'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz' 'SDHB' SDHB_counts.txt
assert_exit_code 0
# Test output of get_gene_counts.py

run sample_test python get_tissue_samples.py 'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt' 'Blood' 'Blood_samples.txt'
assert_exit_code 0
# Test output of get_tissue_samples.py

run blood_test python box.py -tissue Blood -genes SDHB -out_name Blood.png
assert_exit_code 0
# Test output of box.py.