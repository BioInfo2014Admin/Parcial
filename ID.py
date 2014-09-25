def _ID(a):

    """The function saves ids in a list.
    
    Arguments:
    -a- alignment file
    
    Example:
    >>>import os
    >>>import numpy as np
    >>>from Bio import AlignIO
    >>>_ID("example.fasta")"""
        
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
        
    ID = [str(l[j].id) for j in range(0,len(l))]
    return(ID)
