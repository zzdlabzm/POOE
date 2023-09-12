# POOE
In this work, we use the sequence representations from a pre-trained LPLM (ProtTrans) as input and develop a Support Vector Machine-based method termed as POOE for predicting oomycete effectors. POOE revealed high accuracy for classifying protein sequences as effectors or non-effectors through a 5-fold cross-validation and an independent test.<br>

# Data

**1. train_data**<br>

* positivedata549： 549 oomycete effectors from eight species were regarded as the positive data.<br>
* negativedata549： 549 negative samples were selected from the putative 3337 non-effectors based on the positives to negatives ratios of 1:1.<br>
* negativedata1098： 1098 negative samples were selected from the putative 3337 non-effectors based on the positives to negatives ratios of 1:2.<br>
* negativedata1670： 1670 negative samples were selected from the putative 3337 non-effectors based on the positives to negatives ratios of 1:3.<br>

**2. additional_data**<br>

* Additional_test_38： 38 effectors from 8 species that were not included in positivedata549 because they were fewer than 10 effectors for individual species.<br>
* Additional_test_29： 29 recently reported effectors (since 2022) that were not included in positivedata549 and additional_test_38.<br>

**3. genome_results**<br>

We used POOE and EffectorO to conduct proteome-wide identification of effectors on *Phytophthora parasitica*. We showed the 324 and 406 effector proteins in *Phytophthora parasitica* and corresponding scores predicted by POOE and EffectorO, respectively.<br>

**4. train_test_seqname**<br>
We showed sequence names of the training and test sets with five-fold cross-validation based on the positives to negatives ratio of 1:3.<br>

# Features
Codes for generating six encoding schemes reported in our POOE article.<br>

**For ESM**<br>
* esm.yaml:  Conda configuration environment for ESM.<br>
* generate_ESM.py:  Script for generating ESM feature.<br>
* example.sh:  Bash code for running generate_ESM.py.<br>

**For ProtTrans**<br>
* prottrans.yaml:  Conda configuration environment for ProtTrans.<br>
* generate_prottrans.py:  Script for generate ProtTrans feature.<br>
* example.sh:  Bash code for running generate_prottrans.py.<br>

# Model
Final prediction models of POOE obtained in 5-fold cross-validation.<br>

# Scripts
* training_SVM: Training and testing code for SVM.
* Run the script.sh, you will get a score and whether it is an oomycete effector. Script description in script.sh: the first parameter represents input fasta, the second one represents temporary folder, and the third one represents specificity. For example：<br>
```Bash
bash ./script.sh input.fasta tmp_dir 0.9
```

# Webserver
The webserver of POOE is freely accessible at http://zzdlab.com/pooe/index.php. 
