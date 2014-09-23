"""
This function cleans a codon alignment, removes gaps, stops codons and allows user to select an output name. 
Input format must be “fasta” or “phlips” alignment sequences. User can also choose to generate a protein alignment. 
The function also selects zones to keep and zones to eliminate. There are two ways for the user to do that. 
The first way is introducing a sequence of “0” and “1” into the input file. 
The second way is introducing a list of tuples as an argument.

"""

def parcial(dirseq="",formatseq="fasta",protalign=True,outputformat="fasta",outputname="parcial",tupla="",outputnamealign="aligment",outputformatalign="fasta"):
    """ aca van los ejemplos
    """
    import Infile
    import Selectingbyzones
    import limpiezagaps
    import limpiezastops
    import aligngproteins
    import outfile
#primero transformamos el input a fasta
    array = _input(dirseq)
#enviamos al modulo que lo corta
    interestarray = _zoneselector(array,tupla)
#enviamos al modulo que limpia gaps
    nogapsarray = _limpiezagaps(interestarray)
#enviamos al modulo que limpia stops
    finalarray = _limpiezastops(nogapsarray)
#cuando corresponda, generamos el alineamiento de proteinas
    if protalign == True:
        arrayprotalign = _alinprot(finalarray)
#transformamos al formato deseado por el user y lo enviamos a un archivo.
    _outfile(matrizlimpia,outputname,outputformat)

    if protalign == True:
    	_outfile(arrayprotalign,outputnamealign,outputformatalign)
               
            
        
        
    
	

if __name__ == "__main__":
    import argparse
#estos sos los argumentos que cargara el programa

    parser = argparse.ArgumentParser(description='ACA VA LA DESCRIPCION DEL PROGRAMA')
    parser.add_argument('-seqdir',  type=str, help='input name')
    parser.add_argument('-formatseq', type=str, help='input format',default = "fasta")
    parser.add_argument('-protalign', action='store_const', const = True, default = False, help='if True will return cleaned protein aligment ')
    parser.add_argument('-outputformat', type=str, help='output format',default = "fasta")
    parser.add_argument('-outputformatalign', type=str, help='output format fot the protein aligment',default = "fasta")
    parser.add_argument('-outputname', type=str, help='output name', default = "parcial")
    parser.add_argument('-outputnamealign', type=str, help='output name for the protein aligment', default = "aligment")
    parser.add_argument('-tupla', type=tuple, help='lista de tuplas que contiene las zonas de interes',default="")
#esto carga los argumentos en una variable    
    args = parser.parse_args()
#esto envia los argumentos a la funcion parcial, coimo argumentos para la funcion.    
    parcial(args.seqdir,args.formatseq,args.protalign,args.outputformat,args.outputname,args.tupla,args.outputnamealign,args.outputformatalign)
