from seqmod.seqIO import read_fasta , get_seq_length

fastaFile="exampledata/seqmultiline.fasta"
myseqs = read_fasta(fastaFile)
seqLenght= get_seq_length(myseqs)
# print(myseqs)
print(seqLenght)
# if __name__ == '__main__':
#     pass