def _remove_stops(matrix,codontable_number):
    """

This function removes sequences with premature stops from nucleotide matrix.
It walks through the sequences reading codons and if it finds a stop codon before the last three nucleotides it adds the row number into a list.
Finally, it removes the rows that appear in the list.

Argument:
-matrix- nucleotide matrix from aligned sequences
-codontable_number- genetic code id from NCBI

Example:
Alignedmatrix=np.array([["A","A","A","A","A","A","A","A","A","T","G","A"], ["A","A","A","A","A","A","T","G","A","A","A","A"], ["A","A","A","A","A","A","A","A","A","T","G","A"]])
ct = CodonTable.unambiguous_dna_by_id[11]
    seqs_to_delete = []
    for j in range(0,len(Alignedmatrix)):
        for i in range(0,len(Alignedmatrix[0])-3,3):
            codon_1=""
            codon_2 = Alignedmatrix[j,i:i+3]
            codon = codon_1.join(codon_2)
            if codon in ct.stop_codons:
                seqs_to_delete.append(j)
            else:
                pass
    matrix_without_stops = np.delete(Alignedmatrix,seqs_to_delete,0)
    return (matrix_without_stops)

array([['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'T', 'G', 'A'], ["A","A","A","A","A","A","A","A","A","T","G","A"]], 
      dtype='|S1')
      
    """
    import numpy as np
    import Bio.Seq
    from Bio.Data import CodonTable
    ct = CodonTable.unambiguous_dna_by_id[codontable_number]
    seqs_to_delete = []
    for j in range(0,len(matrix)):
        for i in range(0,len(matrix[0])-3,3):
            codon_1=""
            codon_2 = matrix[j,i:i+3]
            codon = codon_1.join(codon_2)
            if codon in ct.stop_codons:
                seqs_to_delete.append(j)
            else:
                pass
    matrix_without_stops = np.delete(matrix,seqs_to_delete,0)
    return (matrix_without_stops)
