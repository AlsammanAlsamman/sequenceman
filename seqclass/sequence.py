from seqmod.seqIO import read_fasta , get_seq_length
class Sequence:
    def __init__(self, file):
        self.file = file
    def get_seqs(self):
        self.seqs = read_fasta(self.file)
        return self.seqs
    def get_seq_length(self):
        if self.seqs is None:
            self.get_seqs()
        self.seq_length = get_seq_length(self.seqs)
        return self.seq_length