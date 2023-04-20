#!/bin/bash

#example
#bash ./script.sh input.fasta  tmp_dir 0.9

input_seq=$1
tmp_dir=$2 
specificity=$3
prottrans_emb_fname="${2}/prottrans_emb.pkl"

python generate_prottrans.py $input_seq $prottrans_emb_fname $tmp_dir
python model.py $prottrans_emb_fname $tmp_dir $specificity
