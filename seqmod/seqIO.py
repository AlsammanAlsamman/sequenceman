import os
import sys
import re
def read_fasta(fastaFile):
    # check if file exists
    if not os.path.exists(fastaFile):
        print(f"Error: {fastaFile} does not exist")
        return
    seqs = {} # key: header, value: sequence
    with open(fastaFile) as f:
        header=None
        for line in f:
            # remove whitespace
            line=line.strip()
            # skip empty lines
            if len(line)==0:
                continue
            # check for header
            if ">"  == line[0]:
                header=line
                header=header[1:] #remove the >
                if len(header) < 1:
                    print("Error: empty header")
                    sys.exit(1)
                header=header.split()[0]
                seqs[header] = "" # seq1
            else:
                seqs[header] += line.upper() ## CTAGACGACTAC
    return seqs

def get_seq_length(seqs):
    """
        This function calculates the length of each sequence in a dictionary of sequences.
        Parameters:
            seqs (dict): dictionary of sequences
    """
    seq_length = {}
    for header, seq in seqs.items():
        seq_length[header] = len(seq)
    return seq_length

def get_seq_gc_content(seqs):
    """
        This function calculates the GC content of each sequence in a dictionary of sequences.
        Parameters:
            seqs (dict): dictionary of sequences
    """
    gc_content = {}
    for header, seq in seqs.items():
        gc_content[header] = (seq.count("G") + seq.count("C"))/len(seq)
    return gc_content

def get_seq_at_content(seqs):
    at_content = {}
    for header, seq in seqs.items():
        at_content[header] = (seq.count("A") + seq.count("T"))/len(seq)
    return at_content

# optimzed
def check_nonDNA(seqs):
    for header, seq in seqs.items():
       for base in seq:
              if base not in "ACGT":
                print(f"Error: {header} has non-DNA base {base}")
                return True
    return False

def reverse_seq(seqs):
    """ This function reverses the sequences in a dictionary of sequences.
        Parameters:
            seqs (dict): dictionary of sequences
    """
    reverse_seqs = {}
    for header, seq in seqs.items():
        reverse_seqs[header] = seq[::-1]
    return reverse_seqs

def complement_seq(seqs):
    """ This function complements the sequences in a dictionary of sequences.
        Parameters:
            seqs (dict): dictionary of sequences
    """
    complement_seqs = {}
    for header, seq in seqs.items():
        # make translation table
        translation_table = str.maketrans("ACGT", "TGCA")
        # translate sequence
        seq = seq.translate(translation_table)
        complement_seqs[header] = seq
    return complement_seqs

#encapsulation
def reverse_complement_seq(seqs):
    """ This function reverse complements the sequences in a dictionary of sequences.
        Parameters:
            seqs (dict): dictionary of sequences
    """
    return complement_seq(reverse_seq(seqs))