from seqmod.seqIO import *

class Sequence:
    """
        This class reads a fasta file and calculates the length,
        GC content, and AT content of the sequences.
    ...
    Attributes
    ----------
        file (str): path to fasta file
        seqs (dict): dictionary of sequences
        seq_length (dict): dictionary of sequence lengths
        seq_gc_content (dict): dictionary of GC content
        seq_at_content (dict): dictionary of AT content
    """
    def __init__(self, file):
        # docstring
        """
            This class reads a fasta file and calculates the length, 
            GC content, and AT content of the sequences.
        """
        self.file = file
    # destructor
    def __del__(self):
        del self.file
        if "seqs" in dir(self):
            del self.seqs
        if "seq_length" in dir(self):
            del self.seq_length
        if "seq_gc_content" in dir(self):
            del self.seq_gc_content
        if "seq_at_content" in dir(self):
            del self.seq_at_content
        print("Sequence object deleted")
    def get_seqs(self):
        self.seqs = read_fasta(self.file)
        # check if DNA
        if check_nonDNA(self.seqs):
            del self.seqs
            return
        return self.seqs

    def get_seq_length(self):
        """
            This function calculates the length of each sequence in a dictionary of sequences.
        """
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
    def get_seq_info(self):
        info={}
        #list attributes
        if "seqs" not in dir(self):
            self.get_seqs()
        if "seq_length" not in dir(self):
            self.get_seq_length()
        if "seq_gc_content" not in dir(self):
            self.get_gc_content()
        if "seq_at_content" not in dir(self):
            self.get_at_content()
        info["gc_content"]=self.seq_gc_content
        info["at_content"]=self.seq_at_content
        info["length"]=self.seq_length
        return info
