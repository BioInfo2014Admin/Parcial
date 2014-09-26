def _remove_stops2(matrix,codontable_number):
    """

This function removes the columns that correspond to stop codons in a  nucleotide matrix.
It walks through the sequences reading codons and if it finds a stop codon it adds the columns to a list.
Finally, it removes the columns that appear in the list.

Argument:
-matrix- nucleotide matrix from aligned sequences
-codontable_number- genetic code id from NCBI

Example:
Alignedmatrix=np.array([["T","G","A","A","A","A","A","A","A","T","G","A","A","A","A"], ["A","A","A","A","A","A","T","G","A","A","A","A","A","A","A"]])
ct = CodonTable.unambiguous_dna_by_id[codontable_number]
    seqs_to_delete = []
    for j in range(0,len(Alignedmatrix)):
        for i in range(0,len(Alignedmatrix[0]),3):
            codon_1 = ""
            codon_2 = matrix[j,i:i+3]
            codon = codon_1.join(codon_2)
            if codon in ct.stop_codons:
                seqs_to_delete.append(i)
                seqs_to_delete.append(i+1)
                seqs_to_delete.append(i+2)
    matrix_without_stops = np.delete(Alignedmatrix,seqs_to_delete,1)
    return (matrix_without_stops)

array([['A', 'A', 'A', 'A', 'A', 'A'],
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
