import sys
import numpy as np
import Bio
from Bio import SeqIO
import os

def _outfile(m, n, ID):
    
    """The function returns the alignments in a file with selected name and format.
    
    First, it converts the alignment matrix to seq element. Via stdout, the function
    creates a file where printed arguments are saved instead of printing in screen.
    
    Arguments:
    -m- alignment matrix 
    -n- the name of the output file
    -ID- a list containing the aligned sequences IDs.
    
    Example:
    >>> my_alignment = np.array([["T","G","A"], ["A","A","A"]])
    >>> my_alignment
    array([['T', 'G', 'A'],
           ['A', 'A', 'A']],
          dtype='|S1')
    >>> ID = ['ENSG0997','ENSG1233']
    >>> import sys
    >>> import numpy as np
    >>> import Bio
    >>> from Bio import SeqIO
    >>> import os
    >>> _outfile(my_alignment,"example.fasta",ID)"""
    
    sys.stdout = open (n, "w")
    
    fileName, fileExtension = os.path.splitext(n)
    
    if fileExtension == ".fasta":
        for i in range(0,len(m)):
            seq_list = m[i].tolist()
            s = ""
            r = s.join(seq_list)
            Seq1 = Bio.Seq.Seq(r)
            print(">"+ID[i]+"\n"+Seq1)
            
    elif fileExtension == ".phylip":
        print(str(len(m))+" "+str(len(m[0])))
        for i in range (0,len(m)):
            seq_list = m[i].tolist()
            s = ""
            r = s.join(seq_list)
            Seq1 = Bio.Seq.Seq(r)
            print(ID[i]+" "+Seq1)
    else:
        raise Exception("Wrong format. Choose accepted format.")
