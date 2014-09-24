# -*- coding: utf-8 -*-
"""
This function cleans a codon alignment, removes gaps, stops codons and allows user to select an output name. 
Input format must be "fasta" or "phylip" alignment sequences. User can also choose to generate a protein alignment. 
The function also selects zones to keep and zones to eliminate. There are two ways for the user to do that. 
The first way is introducing a sequence of "0" and "1" into the input file. 
The second way is introducing a list of tuples as an argument.

"""

def parcial(dirseq="",protalign=True,outputname="parcial.fasta",tupla="",outputnamealign="alignment.fasta",codon_table=1):
    """ aca van los ejemplos
    """
    import Infile
    import Selectingbyzones
    import limpiezagaps
    import removestops
    import alignproteins
    import outfile
    import ID
#primero transformamos el input a una matriz
    ID = ID._ID(dirseq)
    array =Infile._input(dirseq)
#enviamos al modulo que lo corta
    
    interestarray = Selectingbyzones._zoneselector(array,tupla)
#enviamos al modulo que limpia gaps
    
    nogapsarray = limpiezagaps._limpiezagaps(interestarray)
#enviamos al modulo que limpia stops
    finalarray = removestops._remove_stops(nogapsarray,codon_table)
#cuando corresponda, generamos el alineamiento de proteinas
    if protalign == True:
        arrayprotalign = alignproteins._alinprot(finalarray,codon_table)
#transformamos al formato deseado por el user y lo enviamos a un archivo.

    outfile._outfile(finalarray,outputname,ID)

    if protalign == True:
    	outfile._outfile(arrayprotalign,outputnamealign)
               
            
        
        
    
	

if __name__ == "__main__":
    import argparse
#estos sos los argumentos que cargara el programa

    parser = argparse.ArgumentParser(description='ACA VA LA DESCRIPCION DEL PROGRAMA')
    parser.add_argument('-seqdir',  type=str, help='input name')
    parser.add_argument('-protalign', action='store_const', const = True, default = False, help='if True will return cleaned protein aligment ')
    parser.add_argument('-outputname', type=str, help='output name', default = "parcial.fasta")
    parser.add_argument('-outputnamealign', type=str, help='output name for the protein aligment', default = "aligment.fasta")
    parser.add_argument('-tupla', type=tuple, help='lista de tuplas que contiene las zonas de interes')
    parser.add_argument('-codon_table', type=int, help='number of the codon table to use', default = 1)
#esto carga los argumentos en una variable    
    args = parser.parse_args()
#esto envia los argumentos a la funcion parcial, coimo argumentos para la funcion.    
    parcial(args.seqdir,args.protalign,args.outputname,args.tupla,args.outputnamealign,args.codon_table)
