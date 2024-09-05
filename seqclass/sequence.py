from seqmod.seqIO import *

class Sequence:
    def __init__(self, file):
        self.file = file
    def get_seqs(self):
        self.seqs = read_fasta(self.file)
        return self.seqs
    def get_seq_info(self):
        #list attributes
        if "seqs" not in dir(self):
            self.get_seqs()
        info={}
        info["gc_content"]=self.get_gc_content()
        info["at_content"]=self.get_at_content()
        info["length"]=self.get_seq_length()
        return info
    def get_seq_length(self):
        if "seqs" not in dir(self):
            self.get_seqs()
        self.seq_length = get_seq_length(self.seqs)
        return self.seq_length
    def get_gc_content(self):
        if "seqs" not in dir(self):
            self.get_seqs()
        self.seq_gc_content = get_seq_gc_content(self.seqs)
        return self.seq_gc_content
    def get_at_content(self):
        if "seqs" not in dir(self):
            self.get_seqs()
        self.seq_at_content = get_seq_at_content(self.seqs)
        return self.seq_at_content
