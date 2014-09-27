def _gap_cleaner(matrix):
    
    """ This function removes gaps from nucleotide matrix.
    It walks through the sequences reading codons and if it finds a gap it adds the row number into a list.
    Finally, it removes the rows that appear in the list.
    
    Argument:
    -matrix- nucleotide matrix from alignment
    
    
    Example:
    >>> 
    >>> _gap_cleaner (['A' 'C' 'C' 'A' 'G' 'T' 'T' 'G' 'C' 'A' 'T' 'T']
                      ['A' 'C' 'C' '-' '-' '-' 'T' 'G' 'C' 'A' 'A' 'T']
                      ['A' 'C' 'C' 'A' 'G' 'T' '-' '-' '-' 'A' 'A' 'T']
                      ['A' 'C' 'C' 'A' 'G' '-' 'T' 'G' 'C' 'A' 'A' 'T'])
     
    (['A', 'C', 'C', 'A', 'T', 'T'],
     ['A', 'C', 'C', 'A', 'A', 'T'],
     ['A', 'C', 'C', 'A', 'A', 'T'],
     ['A', 'C', 'C', 'A', 'A', 'T'])

    """
    import numpy as np
    gap_list = []
    flag="ok"
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])-2,3):
            if "-" in matrix[i,j:j+3]:
                gap_list.extend([j,j+1,j+2])
                for k in matrix[i,j:j+3]:
                    if k !="-":
                        flag="warning"
    matrix_without_gaps = np.delete(matrix,gap_list,1)
    return (matrix_without_gaps)
                        
