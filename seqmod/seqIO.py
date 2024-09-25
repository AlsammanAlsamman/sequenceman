import os
import sys

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
                print(line)
                header=line
                header=header[1:]
                if len(header) < 1:
                    print("Error: empty header")
                    sys.exit(1)
                header=header.split()[0]
                seqs[header] = ""
            else:
                seqs[header] += line.upper()
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
    gc_content = {}
    for header, seq in seqs.items():
        gc_content[header] = (seq.count("G") + seq.count("C"))/len(seq)
    return gc_content

def get_seq_at_content(seqs):
    at_content = {}
    for header, seq in seqs.items():
        at_content[header] = (seq.count("A") + seq.count("T"))/len(seq)
    return at_content
def check_nonDNA(seqs):
    for header, seq in seqs.items():
        for base in seq:
            if base not in ["A", "T", "G", "C"]:
                return True
    return False