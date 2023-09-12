#PSSM

import os
import sys
import pickle
import numpy as np
from Bio import SeqIO
import time

# you need setup the psiblast command path and psiblast search db ....
input_seqs_fname = "../data/training_data/all_pos_and_neg.fasta"         # input fasta 
input_dir = "./pssm/query/"                            # one protein one fasta file!
output_psiblast_dir = "./pssm/psiblast"                # psi-blast process detaill
output_pssm_dir = "./pssm/pssm"                        # psi-blast final output pssm matrix
output_pssm_pickle_path="./pssm/feature_pssm.pkl"
psiblast_db="/home/lcp/proj/db/uniref50/uniref50"      # set your uniref50 psiblast db path
psiblast_command="psiblast"

min_hit_number = 256
done_list = set()

#input fasta file--Represent each sequence as a FASTA file
if not os.path.exists(input_dir):
    os.makedirs(input_dir,exist_ok=True)

seqs = dict()
for i in SeqIO.parse(input_seqs_fname,"fasta"):
    if "|" in i.id:
        k=i.id.split("|")[1]
        if ":" in k:
            k=k.split(":")[0]
    else:
        k=i.id
    v = str(i.seq)
    seqs[k]=v

for prot_id,prot_seq in seqs.items():
    with open(f"{input_dir}/{prot_id}.fasta","w") as f:
        f.write(f">{prot_id}\n{prot_seq}\n")

#When the file size is greater than 10000 (10kb), it is considered a qualified psi-blast.
if not os.path.exists(output_psiblast_dir):
    os.mkdir(output_psiblast_dir)

for file_name in os.listdir(output_psiblast_dir):
    prot_id = file_name.split(".psiblast")[0] 
    cmd = f"head -n 1 psiblast/{file_name}"
    if list(os.popen(cmd))[0][0:8] == 'PSIBLAST':
        hit_number = list(os.popen(f'cat {output_psiblast_dir}/{file_name}|grep \">\"|wc -l'))[0].strip()
        if int(hit_number) > min_hit_number:
            done_list.add(prot_id)
        else:
            print(f"{prot_id} hit number less than {min_hit_number}!")
    else:
        if os.path.getsize(f"{output_psiblast_dir}/{file_name}") > 10000:
            done_list.add(prot_id)
        else:
            print(f"{prot_id} file size less than 10kb!")

#
import subprocess
query_files = os.listdir(input_dir)
for idx,file_name in enumerate(query_files):
    prot_id = file_name.split(".fasta")[0]
    if prot_id not in done_list:
        start = time.time()

        query_file      = f"{input_dir}/{file_name}"
        output_pssm     = f"{output_pssm_dir}/{prot_id}.pssm"
        output_psiblast = f"{output_psiblast_dir}/{prot_id}.psiblast"
        
        cmd=f"""{psiblast_command} \
            -query {query_file} \
            -db {psiblast_db} \
            -out {output_psiblast} \
            -out_ascii_pssm={output_pssm} \
            -evalue 0.001 \
            -save_pssm_after_last_round \
            -num_iterations 3 \
            -num_threads 90 \
            -outfmt=6"""

        print(f"{idx}/{len(query_files)}\n{cmd}")
        try:
            subprocess.check_call([cmd],shell=True) 
        except subprocess.CalledProcessError:
            print("Command execution failed!")
            break
        print(f"{round(time.time()-start,3)} s")

#turn pssm file to a 2D matrix [protein_length x 20].


feature_pssm = dict()
for prot_id in  [_.split(".fasta")[0] for _ in os.listdir(input_dir)]:
    try:
        feature_pssm[prot_id] = np.genfromtxt(f"{output_pssm_dir}/{prot_id}.pssm",skip_header=3,skip_footer=4,dtype=np.float32)[:,2:22]
    except:
        print(f"turn {prot_id} to a matrix failed!")
        break

#save final pssm feature.
with open(output_pssm_pickle_path, "wb") as f:
    pickle.dump(feature_pssm,f)
