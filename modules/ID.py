import os
from Bio import AlignIO

def _ID(a):

    r"""The function saves ids in a list.
    
    Arguments:
    -a- alignment file
    
    Example:
    
        >>> with open("alignment.fasta", "w") as alignment_file:
    ...     alignment_file.write(">ENSG0997"+"\n"+"TGA"+"\n"+">ENSG1233"+"\n"+"AAA")  
    >>> import os
    >>> from Bio import AlignIO
    >>> ID = _ID("alignment.fasta")
    >>> ID
    ['ENSG0997','ENSG1233']"""
        
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
