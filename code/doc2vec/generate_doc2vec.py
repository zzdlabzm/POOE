#! /usr/bin/python3
# coding = utf-8

# # model.save('/home/mzhao/data/oomycete/doc2vec/doc2vec_test.model')
import re, pickle
import numpy as np
import pandas as pd
from os.path import join
from collections import Counter
from collections import defaultdict
import multiprocessing

# from gensim.models.doc2vec import Doc2Vec, TaggedDocument
def get_documents(seq_list, seq_ids, k, extract_method):
    """
    :param seq_list:
    :param seq_ids:
    :param start:
    :param end:
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
def loadfile(name):
	f = open(name,'r')
	data = [line.strip() for line in f.readlines()]
	f.close()
	return data
data = loadfile('./swissprot_30-5000_50_pos+neg.fasta')
seq = {}
for i in data:
	if i[0]=='>':
		name = i
	else:
		seq[name] = i
dic1 = seq
# print(dic1)
sequences = []
ids = []
for k,v in dic1.items():
    sequences.append(v)
    ids.append(k)

def doc2vector(seq_list, seq_ids, k, extract_method, vector_size, window, epoch):
    """
    :param seq_list:
    :param seq_ids:
    :param start:
    :param end:
    :return: feature_matrix, feature name
    """
    from gensim.models.doc2vec import Doc2Vec
    feature_matrix = []  
    documents = get_documents(seq_list, seq_ids, k, extract_method)


    print('doc2vec sequence length', len(documents))
    # https://radimrehurek.com/gensim/models/doc2vec.html
    name_list = [str(k), str(window)]
    model = Doc2Vec(documents, window=window, vector_size=vector_size, dm=1, workers=20)
    model.train(documents, total_examples=model.corpus_count, epochs=epoch)
    model.save('./'+str(k)+'_'+str(vector_size)+'doc2vec.model')

    print('doc2vec model training finished')

    for index, seq_id in enumerate(seq_ids):
        if extract_method == 3:
            # contain k sub-sequences
            feature_matrix.append([np.mean([model[seq_id + '_%s' % j][i] for j in range(k)]) for i in range(vector_size)])
        else:
            feature_matrix.append([model[seq_id][i] for i in range(vector_size)])

    return feature_matrix, ['vector size: ' + str(vector_size)], model
Feature,name,M = doc2vector(sequences,ids,3,3,32,6,70)

###read positivedata and negativedata
from gensim.models.doc2vec import Doc2Vec
def loadfile(name):
    f = open(name,'r')
    data = [line.strip() for line in f.readlines()]
    f.close()
    return data
pos_data = loadfile('./../data/training_data/positivedata549.fasta')
neg_data1670 = loadfile('./../data/training_data/negativedata1670.fasta')

k = 3
vector_size = 32
model = Doc2Vec.load('./'+str(k)+'_'+str(vector_size)+'doc2vec.model')

pos_seq = {}
for i in pos_data:
    if i[0]=='>':
        name = i
    else:
        pos_seq[name] = i

f = open('./'+str(k)+'_'+str(vector_size)+'pos549_vector.txt','w')
for seq_id in pos_seq.keys():
    feature_matrix = []
    feature_matrix.append([np.mean([model.dv[seq_id + '_%s' % j][a] for j in range(k)]) for a in range(vector_size)])
    f.write(str(feature_matrix)+'\n')
f.close()


neg_seq1670 = {}
for i in neg_data1670:
    if i[0]=='>':
        name = i
    else:
        neg_seq1670[name] = i

f = open('./'+str(k)+'_'+str(vector_size)+'neg1670_vector.txt','w')
for seq_id in neg_seq1670.keys():
    feature_matrix = []
    feature_matrix.append([np.mean([model.dv[seq_id + '_%s' % j][a] for j in range(k)]) for a in range(vector_size)])
    f.write(str(feature_matrix)+'\n')
f.close()









