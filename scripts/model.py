import numpy as np
import sys
import re
from joblib import load

#1.Read three parameters
step4_path  = sys.path[0]
print(sys.argv)
if len(sys.argv)-1 == 3:
    query_prottrans_emb_fname, tmp_dir ,specificity = sys.argv[1:]
else:
    print("error")
   
#2.Load features and models
#2.1 Load features
query_prottrans_emb = np.load(query_prottrans_emb_fname, allow_pickle=True)
query_ids = query_prottrans_emb.keys()
x_prottrans = [query_prottrans_emb[k] for k in query_ids]

#2.2 Load models
model1 = load('../model/SVM_model_1.pkl')
model2 = load('../model/SVM_model_2.pkl')
model3 = load('../model/SVM_model_3.pkl')
model4 = load('../model/SVM_model_4.pkl')
model5 = load('../model/SVM_model_5.pkl')


#3.Calculate predicted score
#3.1 Calculate the predicted score for each model
#There may be multiple sequences
y_scores1 = model1.predict_proba(x_prottrans)[:,1]
y_scores2 = model2.predict_proba(x_prottrans)[:,1]
y_scores3 = model3.predict_proba(x_prottrans)[:,1]
y_scores4 = model4.predict_proba(x_prottrans)[:,1]
y_scores5 = model5.predict_proba(x_prottrans)[:,1]


#3.2 Average the results
#Fold one-dimensional vectors up and down into a two-dimensional matrix, putting the first vector on the first row, the second row, and so on
#The scores two-dimensional matrix, the number of rows is equal to the number of models, the number of columns is equal to the number of samples
scores = np.vstack([y_scores1,y_scores2,y_scores3,y_scores4,y_scores5,])
#                   
scores = scores.mean(0)#Average the rows, and the result is the number of columns, that is, the number of query samples.

#4.Save the result
#ProteinID PredictionScore IsOomyceteEffector
with open(f"{tmp_dir}/jobresult.txt","w") as f:
    line_header = f"ProteinID\tPredictionScore\tspecificity\tIsOomyceteEffector\n"
    print(line_header,end="")
    for tmp_id,tmp_sc in zip(query_ids,scores):
        if specificity=='0.90':
            threshold=0.80  
        elif specificity=='0.80':
            threshold=0.50
        else:
            threshold=0.50

        tmp_IsOomyceteEffector = 'Yes' if tmp_sc >=threshold else 'No'
        line = f"{tmp_id}\t{tmp_sc}\t{specificity}\t{tmp_IsOomyceteEffector}\n"
        print(line,end="")
        f.write(line)


