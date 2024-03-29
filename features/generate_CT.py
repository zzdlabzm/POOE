import numpy as np
from Bio import SeqIO
from multiprocessing import Pool
import sys
import pickle
import os

def ct(k,seq):
    aminos = "AGVCDEFILPHNQWKRMSTY"
    ct_category = {
                'A':'0','G':'0','V':'0',
                'C':'1',
                'D':'2','E':'2',
                'F':'3','I':'3','L':'3','P':'3',
                'H':'4','N':'4','Q':'4','W':'4',
                'K':'5','R':'5',
                'M':'6','S':'6','T':'6','Y':'6' }
    ct_count = {i+j+k:0  for i in '0123456' for j in  '0123456' for k in  '0123456'}
    seq = "".join([ct_category[i] for i in seq.upper() if i in aminos])

    for i in range(len(seq)-2):
        ct_count[seq[i:i+3]] +=1
    values = np.array(list(ct_count.values())) / (len(seq)-2)
    return k,values


def main():
    os.mkdir("./CT") if not os.path.exists("./CT") else print("")

    encode_func = ct

    in_file = sys.argv[1]  if len(sys.argv) > 1 else "../data/training_data/all_pos_and_neg.fasta"
    out_file = sys.argv[2] if len(sys.argv) > 2 else "./CT/all_pos_and_neg_CT.pkl"

    seqs = dict()
    for i in SeqIO.parse(in_file,"fasta"):
        if "|" in i.id:
            k=i.id.split("|")[1]
            if ":" in k:
                k=k.split(":")[0]
        else:
            k=i.id
        v = str(i.seq)
        seqs[k]=v

    #compute
    pool = Pool(12)
    pool_list = []
    for k,v in seqs.items() :
        pool_list.append(pool.apply_async(encode_func,[k,v]))
    pool.close()
    pool.join()

    #extract
    encode_list = [i.get() for i in pool_list]
    encode_dict = {a:np.array(b,np.float32) for a,b in encode_list}

    #save
    with open(out_file,"wb") as f:
        pickle.dump(encode_dict,f)
    #print(encode_dict.keys())

main()
