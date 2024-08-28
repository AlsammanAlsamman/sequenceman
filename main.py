from seqmod.seqIO import read_fasta

fastaFile="exampledata/seqmultiline.fasta"
myseqs = read_fasta(fastaFile)
print(myseqs)
# if __name__ == '__main__':
#     pass