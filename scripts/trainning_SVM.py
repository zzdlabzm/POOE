###SVM

import numpy as np
import random
import numpy
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
import sklearn.metrics as metrics
from sklearn.metrics import precision_recall_curve
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import average_precision_score
from joblib import dump,load
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
import pandas as pd
from sklearn.metrics import auc
from sklearn.metrics import roc_curve
from get_features import Features as Features


#1.Read three parameters
print(sys.argv)
info_list = sys.argv[1:] if len(sys.argv)>1 else None
output_dir = f"../model/5folds_SVM_"+"_".join(info_list)
os.makedirs(output_dir,exist_ok=True)

#2. load data
#2.1 load data
train_files = [f'../data/traindata.txt' for i in range(5)] 
test_files = [f'../data/testdata.txt' for i in range(5)] 

   
#2.2 Load features
features = Features(info=info_list)
test_scores  = []

for foldn in range(5):
    print(f"fold{foldn}: load file => ",end="");sys.stdout.flush();
    train = np.genfromtxt(train_files[foldn],str)
    test  = np.genfromtxt(test_files[foldn],str)
    c2h = np.genfromtxt(c2h_files[foldn],str)
    c2p = np.genfromtxt(c2p_files[foldn],str)
    c3 = np.genfromtxt(c3_files[foldn],str)

    print("encode file =>",end="");sys.stdout.flush();#code
    X_train, y_train = train[:,:2], train[:,2].astype(np.float32)
    X_test,  y_test  = test[:,:2],  test[:,2].astype(np.float32)

    x_train = np.array([np.hstack([features.get(j,foldn) for j in i]) for i in X_train ]) 
    x_test  = np.array([np.hstack([features.get(j,foldn) for j in i]) for i in X_test  ]) 
   

    
    #GirdSearchCV
	# result = svm.SVC()
	# parameters = [
	# 	{'C':[0.01,0.1,1,10,100],'kernel':['linear']},
	# 	{'C':[0.01,0.1,1,10,100],'gamma': 2.0 ** np.arange(-10, 5),'kernel':['rbf']},
	# 	{'C':[0.01,0.1,1,10,100],'degree':[2,3,4,5],'kernel':['poly']},
	# 	{'C':[0.01,0.1,1,10,100],'coef0':[2,3,4,5],'kernel':['sigmoid']}
		
	# ]
	# from sklearn.model_selection import GridSearchCV
	# clf = GridSearchCV(result,parameters,cv=5,n_jobs=2)
	# clf.fit(x_train,y_train)
	# print('1098SVM_Prot_best_params:',clf.best_params_)
	# print(clf.best_estimator_)
	# print(clf.best_score_)
    # print("end------------------------------------")
    # break

    print("training==>",end="");sys.stdout.flush();
    model = svm.SVC(C=10, gamma=0.25, kernel='rbf',probability=True)#1670
    model.fit(x_train,y_train)

    #predict
    print("predicting..")
    y_test_pred = model.predict_proba(x_test)[:,1]
    test_score = multi_scores(y_test, y_test_pred, show=True,threshold=0.5)   
    test_scores.append(test_score)

    #save pred result
    with open(f"{output_dir}/test_pred_{foldn}.txt","w") as f:
        for line in np.hstack([X_c1_test,y_c1_test.reshape(-1,1),y_test_pred.reshape(-1,1)]):
            line = "\t".join(line) + "\n"
            f.write(line)

    #save pred score
    with open(f"{output_dir}/test_score_{foldn}.txt","w") as f:
            f.write("TP\tTN\tFP\tFN\tPPV\tTPR\tTNR\tAcc\tmcc\tf1\tAUROC\tAUPRC\n")
            f.write("\t".join([str(i) for i in test_score]))


print("5 fold average")
test_scores = np.array(test_scores)
fmat =  [1, 1,  1,  1,  3,  3,  3,  3,  3,  3,  3,      3]
with open(f"{output_dir}/test_average_score.txt",'w') as f:
    line1 = f"TP\tTN\tFP\tFN\tPPV\tTPR\tTNR\tAcc\tmcc\tf1\tAUROC\tAUPRC\n"
    line2 = '\t'.join([f'{a:.{_}f}±{b:.{_}f}' for (_,a,b) in zip(fmat,test_scores.mean(0),test_scores.std(0))])
    print(line1,end="")
    print('\t'.join([f'{a:.{_}f}' for (_,a) in zip(fmat,test_scores.mean(0))]))
    f.write(line1)
    f.write(line2)
    f.write("\n")


print("-----------------------------------")



