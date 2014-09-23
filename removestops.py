def _remove_stops(matrix,codontable_number):
    """

Docstring

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
