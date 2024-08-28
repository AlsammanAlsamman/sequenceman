def read_fasta(fastaFile):
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
                header=header[1:]
                header=header.split()[0]
                seqs[header] = ""
            else:
                seqs[header] += line
    return seqs

def get_seq_length(seqs):
    seq_length = {}
    for header, seq in seqs.items():
        seq_length[header] = len(seq)
    return seq_length