# POOE
In this work, we use the sequence representaions from a pre-trained LPLM (ProtTrans) as input and develop a Support Vector Machine-based method termed as POOE for predicting oomycete effectors. POOE revealed high accuracy for classifying protein sequences as effectors or non-effectors through a 5-fold cross-validation and an independent test.<br>

# Data

**1. train_data**<br>

- [Heading One](positivedata549） 549 oomycete effectors from eight species were retained and regarded as the positive data.<br>
  negativedata549     # 549 negative samples were selected from the putative 3337 non-effectors based on the positives to negatives ratios of 1:1.<br>
  negativedata1098  # 1098 negative samples were selected from the putative 3337 non-effectors based on the positives to negatives ratios of 1:2.<br>
  negativedata1670  # 1670 negative samples were selected from the putative 3337 non-effectors based on the positives to negatives ratios of 1:3.<br>

**2. additional_data**<br>

  Additional_test_38     # 38 effectors from 8 species that were not included in previous species because they were fewer than 10 effectors.<br>
  Additional_test_29     # 29 effectors newly collected effectors since 2022.<br>

**3. genome_results**<br>

We used POOE to conduct proteome-wide identification of effectors on *Phytophthora parasitica*. We showed the 324 effector proteins in *Phytophthora parasitica* and corresponding scores.<br>

# Features
Run the six encoding schemes code to generate the features.<br>

**For ESM**<br>
  esm.yaml: Conda configuration environment for ESM.<br>
  generate_ESM.py: Script for generate ESM feature.<br>
  temp.sh: Bash code for running generate_ESM.py.<br>

**For ProtTrans**<br>
  prottrans.yaml: Conda configuration environment for ProtTrans.<br>
  generate_prottrans.py: Script for generate ProtTrans feature.<br>
  temp.sh: Bash code for running generate_prottrans.py.<br>

```
# For ESM and ProtTrans
# Create the conda runtime environment from the provided yaml file
cd ./data/training_data/positivedata549.fasta
cd ./code/ProtTrans
python generate_prottrans.py
```
# Model
Five models obtained in 5-fold cross-validation of POOE.<br>

# Scripts
Run the script.sh, you will get a score and whether it is an oomycete effector. Script description in script.sh: the first parameter represents input fasta, the second one represents temporary folder, and the third one represents specificity. For example：<br>
```Bash
bash ./script.sh input.fasta tmp_dir 0.9
```

# Webserver
The webserver of POOE is freely aceesible at http://zzdlab.com/pooe/index.php. 
