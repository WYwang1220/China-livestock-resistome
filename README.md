#1. cgSNPs were extracted from the core genome alignment using SNP-sites v2.5.1, and the number of cgSNPs was counted using a Python script (count_snps.py).

#2. A Python script (snp-dists.py) was used to compute the genetic distance matrix for all pairwise allelic profile comparisons. 
    Isolate pairs with pairwise cgSNP distances ≤ 100 were considered sharing pairs.

#3. A Python script (timetree.py) was used to assess the strength of the temporal signal, calculating the coefficient of determination (R²) and the significance p-value.
    Only when R² > 0.5 and p < 0.001 was the dataset considered to have a significant temporal signal suitable for reliable molecular clock inference.
