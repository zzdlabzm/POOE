#! /usr/bin/python3
# coding = utf-8

import re, pickle
import numpy as np
import pandas as pd
from os.path import join
from collections import Counter
from collections import defaultdict
import multiprocessing
from Bio import SeqIO
# from gensim.models.doc2vec import Doc2Vec, TaggedDocument
def get_documents(seq_list, seq_ids, k, extract_method):
    """
    :param seq_list:
    :param seq_ids:
    :param k:
    :param extract_method
    Example sequence: MALFFFNNN
    doc2vec parameters: k, extract_method, vector_size, window
    extract_method: [1, 2, 3]
        sequence example: MALFFFNNN
        1) ['MAL', 'ALF', 'LFF', 'FFF', 'FFN', 'FNN', 'NNN']
        2) ['MAL', 'FFF', 'NNN', 'ALF', 'FFN', 'LFF', 'FNN']
        3) ['MAL', 'FFF', 'NNN']
           ['ALF', 'FFN']
           ['LFF', 'FNN']
    vector_size: [64]
    window [3]
    :return:
    """
    from gensim.models.doc2vec import TaggedDocument
    documents = []
    for seq, seq_id in zip(seq_list, seq_ids):
        end = len(seq)
        codes = seq[0: end]
        if extract_method == 1:
            # output: ['MAL', 'ALF', 'LFF', 'FFF', 'FFN', 'FNN', 'NNN']
            words = [codes[i: i + k] for i in range(len(codes) - (k - 1))]
            documents.append(TaggedDocument(words, tags=[seq_id]))
        elif extract_method == 2:
            # output: ['MAL', 'FFF', 'NNN', 'ALF', 'FFN', 'LFF', 'FNN']
            words = [codes[j: j + k] for i in range(k) for j in range(i, len(codes) - (k - 1), k)]
            documents.append(TaggedDocument(words, tags=[seq_id]))
        elif extract_method == 3:
            """
            # output:
                ['MAL', 'FFF', 'NNN']
                ['ALF', 'FFN']
                ['LFF', 'FNN']
            """
            for i in range(k):
                words = [codes[j: j + k] for j in range(i, len(codes) - (k - 1), k)]
                documents.append(TaggedDocument(words, tags=[seq_id + '_%s' % i]))
    return documents

# read corpus
seqs = dict()
count_for_test=1000
for i in SeqIO.parse("./doc2vec/swissprot_30-5000_50_pos+neg.fasta","fasta"):#load your corpus
    if "|" in i.id:
        k=i.id.split("|")[1]
        if ":" in k:
            k=k.split(":")[0]
    else:
        k=i.id
    v = str(i.seq)
    seqs[k]=v
    count_for_test -=1
    if count_for_test ==0 :
        break

seqs_train = dict()
for i in SeqIO.parse("../data/training_data/all_pos_and_neg.fasta","fasta"):
    if "|" in i.id:
        k=i.id.split("|")[1]
        if ":" in k:
            k=k.split(":")[0]
    else:
        k=i.id
    v = str(i.seq)
    seqs_train[k]=v


def doc2vector(seqs, k_len, extract_method, vector_size, window, epoch):
    """
    :param seq_list:
    :param seq_ids:
    :param start:
    :param end:
    :return: feature_matrix, feature name
    """
    seq_ids = [k for k,v in seqs.items()]
    seq_list = [v for k,v in seqs.items()]
    from gensim.models.doc2vec import Doc2Vec
    feature_matrix = []  
    documents = get_documents(seq_list, seq_ids, k_len, extract_method)
    print('doc2vec sequence length', len(documents))
    # https://radimrehurek.com/gensim/models/doc2vec.html
    name_list = [str(k_len), str(window)]
    model = Doc2Vec(documents, window=window, vector_size=vector_size, dm=1, workers=20)
    print("training")
    model.train(documents, total_examples=model.corpus_count, epochs=epoch)
    model.save('./doc2vec/'+str(k_len)+'_'+str(vector_size)+'doc2vec.model')
    print('doc2vec model training finished')
    pssm_features = dict()
    for k,v in seqs.items():
        if extract_method == 3:
            pssm_features[k] = [np.mean([model[k + '_%s' % j][i] for j in range(k_len)]) for i in range(vector_size)]
        else:
            pssm_features[k] = [model[k][i] for i in range(vector_size)]	
    return pssm_features, ['vector size: ' + str(vector_size)], model

Feature,name,M = doc2vector(seqs,3,3,32,6,70)

import pickle 
with open("./doc2vec/doc2vec.pkl","wb") as f:
    pickle.dump(Feature,f)





