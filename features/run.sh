python ./generate_CT.py  ../data/training_data/all_pos_and_neg.fasta ./CT/all_pos_and_neg_CT.pkl
python ./generate_DPC.py  ../data/training_data/all_pos_and_neg.fasta ./DPC/all_pos_and_neg_DPC.pkl

#before run the command below, you need set you psiblast soft and psiblast uniref50 search db in the ./generate_PSSM.py first.
python ./generate_PSSM.py
python ./generate_doc2vec.py

