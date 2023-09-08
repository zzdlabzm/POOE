mkdir ./tmp_esm_out/
#python extract.py esm1b_t33_650M_UR50S input.fasta ./tmp_esm_out/ --include mean --repr_layers 33 --truncation_seq_length 2000
python generate_ESM.py  esm1b_t33_650M_UR50S  ../../data/training_data/positivedata549.fasta ./output_out/ \
    --include mean  \
    --repr_layers 33  \
    --truncation_seq_length 4000  \
    --save_file  \
    ./positivedata549_esm.pkl
