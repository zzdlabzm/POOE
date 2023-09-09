# POOE
In this work, we use the sequence representaions from a pre-trained LPLM (ProtTrans) as input and develop a Support Vector Machine-based method termed as POOE for predicting oomycete effectors. POOE revealed high accuracy for classifying protein sequences as effectors or non-effectors through a 5-fold cross-validation and an independent test.<br>

# Data

**1. train_data**<br>

· positivedata549: To prepare the positive data, 1143 experimentally determined oomycete effectors were collected from the literature. CD-HIT with a 40% pairwise sequence identity cutoff was used to remove redundant sequences. Then, the species with fewer than of 10 effector sequences were deleted. As a result, 549 oomycete effectors from eight species were retained and regarded as the positive data.<br>
· negativedata549: 549 negative samples were selected from the putative 3337 non-effectors based on the positives to negatives ratios of 1:1.<br>
· negativedata1098: 1098 negative samples were selected from the putative 3337 non-effectors based on the positives to negatives ratios of 1:2.<br>
· negativedata1670: 1670 negative samples were selected from the putative 3337 non-effectors based on the positives to negatives ratios of 1:3.<br>

**2. additional_data**<br>

· Additional_test_38: 38 effectors from 8 species that were not included in previous species because they were fewer than 10 effectors using the 1:3 ratio of positive to negative samples.<br>
· Additional_test_29: 29 effectors newly collected effectors since 2022 using the 1:3 ratio of positive to negative samples.<br>

**3. genome_results**<br>

We used POOE to conduct proteome-wide identification of effectors on *Phytophthora parasitica*. After the initial filtering, 1515 out of 22979 proteins in *Phytophthora parasitica* were predicted as secreted proteins without transmembrane regions and were further submitted to POOE. At a Specificity control of 89.8% (i.e., false positive rate at 10.2%), 324 effector proteins were predicted in *Phytophthora parasitica*. We showed the 324 effector proteins and corresponding scores.<br>

# Model
Five models obtained in 5-fold cross-validation of POOE.<br>

# features
Run the six encoding schemes code to generate the features.<br>
```
# For ESM and ProtTrans
# Create the conda runtime environment from the provided yaml file
# Example
cd ./data/training_data/positivedata549.fasta
cd ./code/ProtTrans
python generate_prottrans.py
```

# Scripts
Run the script.sh, you will get a score and whether it is an oomycete effector. Script description in script.sh: the first parameter represents input fasta, the second one represents temporary folder, and the third one represents specificity. For example：<br>
```Bash
bash ./script.sh input.fasta tmp_dir 0.9
```

# Webserver
The webserver of POOE is freely aceesible at http://zzdlab.com/pooe/index.php. 
