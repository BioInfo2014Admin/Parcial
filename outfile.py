import sys

def outfile(n, f):
    
    """The function returns a file with selected name and format.
    
    Via stdout, the function creates a file where printed arguments 
    are saved instead of printing in screen.
    
    Arguments:
    -n- the name of the file
    -f- the file format
    
    Example:
    >>>import sys
    >>>my_seq = ("AAACTGCCA")
    >>>outfile("example.fasta","fasta")
    >>>print(my_seq)"""
    
    if f=="fasta":
        pass
    elif f=="phylip":
        pass
    elif f=="gbk":
        pass
    else:
        raise Exception("Wrong format. Choose accepted format.")
    sys.stdout = open (n, "w")
