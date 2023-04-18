import argparse
import os
from Bio import SeqIO
import torch
import pickle
import numpy as np
import sys

script_path = sys.path[0]
esm_extract_script = os.path.join(script_path,'extract.py')

def print_layer(prefix):
    print(f'{prefix}: {os.environ.get("MKL_THREADING_LAYER")}')

def run_esm_emb_model(seq_file, temp_dir):
    os.makedirs(f"{temp_dir}",exist_ok=True)
    seqs = {i.id:str(i.seq) for i in SeqIO.parse(seq_file,"fasta")}

    with open(os.path.join(temp_dir,"input_for_esm.fasta"),"w") as f:
        for k,v in seqs.items():
            if len(v) > 1000:
                for i in range(len(v) // 1000):
                    sub_v = v[i*1000: (i+1)*1000]
                    sub_k = f"{k}__{i}_{len(sub_v)}"
                    f.write(f">{sub_k}\n{sub_v}\n")
            else:
                f.write(f">{k}\n{v}\n")

    cmd = f"python  {esm_extract_script} esm1b_t33_650M_UR50S " +\
        os.path.join(temp_dir,"input_for_esm.fasta") + " " +\
        os.path.join(temp_dir,"out_esm") + " " +\
        "--include mean "+\
        "--repr_layers 33 "
    print(cmd)#.replace("  "," "))
    os.system(cmd)


def extract_esm_mean_feature(temp_dir, out_file):
    #id_dict to represent long and sort sequences.
    ids_embs = dict()
    for f_name in os.listdir(f"{temp_dir}/out_esm"):
        if "__" in f_name:
            k = f_name.split("__")[0]
            if k not in ids_embs.keys():
                ids_embs[k]=[f_name,]
            else:
                ids_embs[k].append(f_name)
        else:
            ids_embs[f_name.split(".pt")[0]] = [f_name,]

    for k,v in ids_embs.items():
        ids_embs[k] = sorted(ids_embs[k])

    esm_mean = dict()
    for idx,(k, f_names) in enumerate(ids_embs.items()):
        if len(f_names) == 1:
            temp = torch.load(f"{temp_dir}/out_esm/{f_names[0]}")['mean_representations'][33].numpy()
            #print(temp)
            esm_mean[k] = temp
            print(f"{idx} {len(ids_embs)} {k}")
        else:
            temps = [torch.load(f"{temp_dir}/out_esm/{f_name}")['mean_representations'][33].numpy() 
                        for f_name in f_names ]
            #print(temps)
            weights = np.array([f_name.split("__")[1].split(".")[0].split("_")[1] for f_name in f_names],np.float32)
            weights = weights / weights.sum()
            esm_mean[k] = np.array([t*w for t,w in zip(temps,weights)]).sum(0)
            print(f"{idx} {len(ids_embs)} {k}")
        
        #print(k,esm_mean[k])

    with open(out_file,"wb") as f:
        pickle.dump(esm_mean, f)


def main():
    parser = argparse.ArgumentParser(description='Generate EsmMean embeding of proteins')
    parser.add_argument("input",type=str,action="store",help='input  protein sequences for esm-mean feature ')
    parser.add_argument("output",type=str,action="store",help='output file')
    parser.add_argument("tmp_dir",type=str,default="./cache/",help='temp dir')
    args = parser.parse_args()
    run_esm_emb_model(args.input , args.tmp_dir)
    extract_esm_mean_feature(args.tmp_dir, args.output)

main()


