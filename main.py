from seqclass.sequence import Sequence


fastaFile="exampledata/seqmultiline.fasta"

myseq = Sequence(fastaFile)
print(myseq.get_seqs())
print(myseq.get_seq_length())


# print(myseq.get_seq_length())





# myseqs = read_fasta(fastaFile)
# seqLenght= get_seq_length(myseqs)
# # print(myseqs)
# print(seqLenght)
# # if __name__ == '__main__':
# #     pass