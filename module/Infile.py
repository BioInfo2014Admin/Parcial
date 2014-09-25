import os
import numpy as np
from Bio import AlignIO

def _input(a):

    """The function converts alignments to matrix for further use.
  
    Arguments:
    -a- alignment file
    
    Example:
    >>>import os
    >>>import numpy as np
    >>>from Bio import AlignIO
    >>>_input("example.fasta")"""
        
    fileName, fileExtension = os.path.splitext(a)
    
    if fileExtension == ".phylip":
        try:
            l = list(AlignIO.read(a,"phylip"))
        except (ValueError):
            l = list(AlignIO.read(a,"phylip-relaxed"))
        except:
            pass
    elif fileExtension == ".fasta":
        l = list(AlignIO.read(a,"fasta"))
    else:
        raise Exception("Wrong format. Choose accepted format.")

    p = [[i for i in str(l[j].seq)] for j in range(0,len(l))]
    y = np.array(p)
    return(y)
