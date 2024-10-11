# Add class for DNA sequence
from seqclass.sequence import Sequence
from seqmod.seqIO import *
from seqclass.GenomicConst import GenomicConst
class DNA(Sequence):
    def reverse_complement(self):
        """
            This function calculates the reverse complement of the sequences.
        """
        if "seqs" not in dir(self):
            self.get_seqs()
        return reverse_complement_seq(self.seqs)

    def dna_translate(seq):
        trans_dict = GenomicConst.TripleCodonTable
        for i in range(0, len(seq), 3):
            codon = seq[i:i+3]
            if len(codon) == 3:
                aa+=trans_dict[codon]
        return aa

    def translate(self):
        """
            This function translates the sequences into amino acids.
        """
        self.aa_seqs = {}
        if "seqs" not in dir(self):
            self.get_seqs()
        for header, seq in self.seqs.items():
            self.aa_seqs[header] = DNA.dna_translate(seq)