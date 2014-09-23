import sys
import numpy as np
from Bio import SeqIO
import Bio

def _outfile(m, n, f):
    
    """The function returns the alignments in a file with selected name and format.
    
    First, it converts the alignment matrix to seq element. Via stdout, the function
    creates a file where printed arguments are saved instead of printing in screen.
    
    Arguments:
    -m- alignment matrix 
    -n- the name of the file
    -f- the file format
    
    Example:
    >>>import sys
    >>>import numpy as np
    >>>import Bio
    >>>from Bio import SeqIO
    >>>outfile(matrix,"example.fasta","fasta")"""
    
    sys.stdout = open (n, "w")
    
    if f=="fasta":
        for i in range(0,len(m)):
            seq_list = m[i].tolist()
            S = ""
            R = S.join(seq_list)
            Seq1 = Bio.Seq.Seq(R)
            print(">"+ID[i]+"\n"+Seq1)
            
    elif f=="phylip":
        print(str(len(m))+" "+str(len(m[0])))
        for i in range (0,len(m)):
            seq_list = m[i].tolist()
            S = ""
            R = S.join(seq_list)
            Seq1 = Bio.Seq.Seq(R)
            print(ID[i]+" "+Seq1)
    else:
        raise Exception("Wrong format. Choose accepted format.")
