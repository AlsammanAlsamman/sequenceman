from seqclass.sequence import Sequence
from seqmod.seqIO import read_fasta, get_seq_length


fastaFile="exampledata/seqmultiline.fasta"

myseq = Sequence(fastaFile)

# myseq.get_seqs()
# myseq.get_seq_length()
# del myseq
get_seq_length(fastaFile)
# print(myseq.get_seq_length())
# print(myseq.get_gc_content())

# print(myseq.get_seq_length())

# myseqs = read_fasta(fastaFile)
# seqLenght= get_seq_length(myseqs)
# # print(myseqs)
# print(seqLenght)
# # if __name__ == '__main__':
# #     pass