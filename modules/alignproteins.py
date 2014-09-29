def _Alignproteins(NM,codtable):
    
    """
    This function translates a nucleotide matrix already  aligned.
    It goes along the rows and columns and list their elements, 
    transforms them into a Biopython's sequence and eventually translate them to protein.
    Finally returns an aminoacidic matrix.
    
    Argument:
    -NM- Nucleotide matrix
    -codtable- CodonTable from IUPAC
    
    Example:
    
    >>> import Bio
    >>> from Bio.Data import CodonTable
    >>> from Bio.Seq import Seq
    >>> import numpy as np
    >>> Alignproteinsmatrix=np.array([["A","C","T","G","C","A","C","G","A"], 
                                      ["T","C","A","A","C","G","A","G","G"]])
    >>> _Alignproteins(Alignproteinsmatrix,11)
    array([['T', 'A', 'R'],
           ['S', 'T', 'R']], 
          dtype='|S1')
    """
    import Bio
    from Bio.Seq import Seq
    from Bio.Data import CodonTable
    import numpy as np
    lista2=[]
    for i in range (0,len(NM)):
        lista=[]
        for j in range (0, len(NM[0])-2,3):
            H=""
            B=H.join(NM[i,j:j+3])
            lista.append(Bio.Seq.translate(B,codtable))
        lista2.append(lista)
    return(np.array(lista2))
