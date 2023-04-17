# POOE
In this work, we use the sequence representaions from a pre-trained LPLM (ProtTrans) as input and develop a Support Vector Machine-based method termed as POOE for predicting oomycete effectors. POOE revealed high accuracy for classifying protein sequences as effectors or non-effectors through a 5-fold cross-validation and an independent test.<br>

# Data
1. positivedata549: To prepare the positive data, 1143 experimentally determined oomycete effectors were collected from the literature. CD-HIT with a 40% pairwise sequence identity cutoff was used to remove redundant sequences. Then, the species with fewer than of 10 effector sequences were deleted. As a result, 549 oomycete effectors from eight species were retained and regarded as the positive data.<br>
2. negativedata549: From the putative 3337 non-effectors, 549 negative samples were selected according to the species of positive samples based on the positives to negatives ratios of 1:1.<br>
3. negativedata1098: From the putative 3337 non-effectors, 1098 negative samples were selected according to the species of positive samples based on the positives to negatives ratios of 1:2.<br>
4. negativedata1670: From the putative 3337 non-effectors, 1670 negative samples were selected according to the species of positive samples based on the positives to negatives ratios of 1:3.<br>

#Model
Five models obtained in 5-fold cross-validation of POOE.<br>

# Webserver
The webserver of POOE is freely aceesible at http://zzdlab.com/pooe/index.php. 
