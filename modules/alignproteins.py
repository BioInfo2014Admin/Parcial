def _alignproteins(NM, codtable):
    
    """T
    This function translates a nucelotide matrix already  aligned
    It goes along the rows and columns and list their elements, 
    transforms them into a Biopython's sequence and eventually translate them to protein
    
    Argument:
    
    -NM- Nucleotide matrix
    -codtable- CodonTable from IUPAC
    
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
    from Bio.Data import CodonTable 
    import numpy as np
    CodonTable.unambiguous_dna_by_id[codtable]
    for i in range (0,len(NM)):
        list_1=NM[i].tolist()
        H=""
        B=H.join(list_1)
        Seq1=Bio.Seq.Seq(B)
        return(Seq1)
