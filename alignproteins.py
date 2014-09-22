def _alignproteins(NM):
    """This function translates a nucelotide matrix already  aligned
    It goes along the rows and columns and list their elements, transforms them into a Biopython's sequence and eventually translate them to protein
    
    Argument:
    -NM- Nucleotide matrix
    
    Example:
    Alignproteinsmatrix=np.array([["A","C","G","G","A","A"],
                              ["A","C","G","T","C","T"]])
    for i in range(0,len(Alignproteinsmatrix)):
        list_1=Alineproteinsmatrix[i].tolist()
        H=""
        B=Ar.join(list_1)
        Seq1=Bio.Seq.Seq(B)
        return(Seq1.translate())
        
        TE
        TS
        """
    import numpy as np
    for i in range (0,len(NM)):
        list_1=NM[i].tolist()
        H=""
        B=H.join(list_1)
        Seq1=Bio.Seq.Seq(B)
        return(Seq1)
