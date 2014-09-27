def _remove_stops(matrix,codontable_number,ID,stops):
    """

    This function removes sequences with premature stops from nucleotide matrix.
    It walks through the sequences reading codons and if it finds more than 
    one stop codon it adds the row number into a list.
    Finally, it removes the rows that appear in the list.

    Argument:
    -matrix- nucleotide matrix from aligned sequences
    -codontable_number- Codon Table from IUPAC
    -ID- genetic code id from NCBI
    -stops- stop codons 
    Example:

    >>> arr = np.array([["T","G","A","A","A","A","A","A","A","T","G","A"], 
                        ["A","A","A","A","A","A","T","G","A","A","A","A"], 
                        ["A","A","A","A","A","A","T","G","A","A","A","A"],
                        ["T","G","A","A","A","A","T","G","A","A","A","A"]])
    >>> arr
    array([['T', 'G', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'T', 'G', 'A'],
           ['A', 'A', 'A', 'A', 'A', 'A', 'T', 'G', 'A', 'A', 'A', 'A'],
           ['A', 'A', 'A', 'A', 'A', 'A', 'T', 'G', 'A', 'A', 'A', 'A'],
           ['T', 'G', 'A', 'A', 'A', 'A', 'T', 'G', 'A', 'A', 'A', 'A']], 
           dtype='|S1')
    >>> _remove_stops (arr,11,ID,C)
    >>> matrix_without_stops
    matrix_without_stops( ['A', 'A', 'A', 'A', 'A', 'A', 'T', 'G', 'A', 'A', 'A', 'A'],
                          ['A', 'A', 'A', 'A', 'A', 'A', 'T', 'G', 'A', 'A', 'A', 'A']], 
                     dtype='|S1')

      
    """
    import numpy as np
    import Bio.Seq
    from Bio.Data import CodonTable
    ct = CodonTable.unambiguous_dna_by_id[codontable_number]
    seqs_to_delete = []
    counter = 0
    for j in range(0,len(matrix)):
        for i in range(0,len(matrix[0])-3,3):
            codon_1=""
            codon_2 = matrix[j,i:i+3]
            codon = codon_1.join(codon_2)
            if codon in ct.stop_codons:
                counter += 1
            else:
                pass
            if counter > 1:
                seqs_to_delete.append(j)
                counter = 0
            else:
                pass
        counter = 0
    ID.pop(seqs_to_delete)
    matrix_without_stops = np.delete(matrix,seqs_to_delete,0)
    return (matrix_without_stops,ID)
    
def _remove_stops2(matrix,codontable_number, ID, stops):
    """

    This function removes the columns that correspond to stop codons in a  nucleotide matrix.
    It walks through the sequences reading codons and if it finds a stop codon it adds the columns to a list.
    Finally, it removes the columns that appear in the list.

    Argument:
    -matrix- nucleotide matrix from aligned sequences
    -codontable_number- Codon Table from IUPAC
    -ID- genetic code id from NCBI
    -stops- stop codons

    Example:

    >>> import numpy as np
    >>> import Bio.Seq
    >>> from Bio.Data import CodonTable
    >>> arr = np.array([["T","G","A","A","A","A","A","A","A","T","G","A"], 
                        ["A","A","A","A","A","A","T","G","A","A","A","A"], 
                        ["A","A","A","A","A","A","T","G","A","A","A","A"], 
                        ["T","G","A","A","A","A","T","G","A","A","A","A"]])
    >>> arr
    array([['T', 'G', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'T', 'G', 'A'],
           ['A', 'A', 'A', 'A', 'A', 'A', 'T', 'G', 'A', 'A', 'A', 'A'],
           ['A', 'A', 'A', 'A', 'A', 'A', 'T', 'G', 'A', 'A', 'A', 'A'],
           ['T', 'G', 'A', 'A', 'A', 'A', 'T', 'G', 'A', 'A', 'A', 'A']], 
           dtype='|S1')
    >>> _remove_stops2 (arr,11,ID,D)
    >>> matrix_without_stops
    matrix_without_stops([['A', 'A', 'A', 'A', 'A', 'A'],
                          ['A', 'A', 'A', 'A', 'A', 'A']], 
                          dtype='|S1')

      
    """
    import numpy as np
    import Bio.Seq
    from Bio.Data import CodonTable
    ct = CodonTable.unambiguous_dna_by_id[codontable_number]
    seqs_to_delete = []
    for j in range(0,len(matrix)):
        for i in range(0,len(matrix[0]),3):
            codon_1 = ""
            codon_2 = matrix[j,i:i+3]
            codon = codon_1.join(codon_2)
            if codon in ct.stop_codons:
                seqs_to_delete.append(i)
                seqs_to_delete.append(i+1)
                seqs_to_delete.append(i+2)
    matrix_without_stops = np.delete(matrix,seqs_to_delete,1)
    return (matrix_without_stops)
    
    if stops == "C":
        _remove_stops(matrix,codontable_number,ID,stops)
    elif stops == "D":
        _remove_stops2(matrix,codontable_number,ID,stops)
    elif stops == None:
        return (matrix,ID)
