# -*- coding: utf-8 -*-
"""
This function cleans a codon alignment , removes gaps, stops codons and allows user to select an output name. 
Input format must be "fasta" or "phylip" alignment sequences. User can also choose to generate a protein alignment. 
The funtion has two options to remove stops codons, the first directly remove all the secuences with premature codons (-stops c) and the other remove all the secuence after the stop codon (-stops -d). By default the funtion dont remove the stop codons.  
The function also selects zones to keep and zones to eliminate. There are two ways for the user to do that. 
The first way is introducing a sequence of "0" and "1" into the input file. 
The second way is introducing a list of tuples as an argument.
-seqdir sequence (eg. ejemplo.fasta)
-protalign 
-outputname name (eg. result.fasta)
-tupla (list of tuples) (eg. [(0,3),(12,33),(933,1032)]
-outputnamealign name (eg. result2.fasta)
-codon_table ID (eg. 1)
-stops (-d or -c) 
(eg. python Parcial.py -seqdir ejemplo.fasta -outputname pruebajodida32.fasta -stops d)

"""

def parcial(dirseq,protalign,outputname,tupla,outputnamealign,codon_table,binary,stops):
#aca generamos los doctest
    """
    >>> parcial("ejemplo.fasta",False,"alineamiento.fasta",None,"alineamientoprot.fasta",1,None,None)
    >>> parcial("ejemplo.fasta",True,"alineamiento.fasta",None,"alineamientoprot.fasta",1,None,None)
    >>> parcial("ejemplo.fasta",False,"alineamiento.fasta",[(0,9),(27,30)],"alineamientoprot.fasta",1,None,None)
    >>> parcial("ejemplo.fasta",False,"alineamiento.fasta",None,"alineamientoprot.fasta",1,"binary.txt",None)
    >>> parcial("ejemplo.fasta",False,"alineamiento.fasta",None,"alineamientoprot.fasta",1,None,"c")
    >>> parcial("ejemplo.fasta",False,"alineamiento.fasta",None,"alineamientoprot.fasta",1,None,"d")
    >>> parcial("ejemplo.fasta",False,"alineamiento.fasta",None,"alineamientoprot.fasta",1,None,"cd")
    Exception: wrong argument -stops: it should be c or d, instead it was cd 
    """
#no me sale hacer un doctest que espere un error

#aca importamos los todos los modulos
    import Infile
    import Selectingbyzones
    import limpiezagaps
    import removestops
    import alignproteins
    import outfile
    import ID
#primero transformamos el input a una matriz
    if stops == "d" or stops == "c" or stops == None:
        pass
    else:
        raise Exception("wrong argument -stops: it should be c or d, instead it was "+str(stops))   
    ID = ID._ID(dirseq)
    array =Infile._input(dirseq)
#enviamos al modulo que lo corta
    
    interestarray = Selectingbyzones._zoneselector(array,tupla,binary)
#enviamos al modulo que limpia gaps
    
    nogapsarray = limpiezagaps._limpiezagaps(interestarray)
#enviamos al modulo que limpia stops
    final = removestops._remove_stops(nogapsarray,codon_table,ID,stops)
#cuando corresponda, generamos el alineamiento de proteinas
    if protalign == True:
        arrayprotalign = alignproteins._alignproteins(final[0],codon_table)

#transformamos al formato deseado por el user y lo enviamos a un archivo.

    outfile._outfile(final[0],outputname,final[1])

    if protalign == True:
    	outfile._outfile(arrayprotalign,outputnamealign)
               
            
        
        
    
	

if __name__ == "__main__":
    import argparse
#estos sos los argumentos que cargara el programa

    parser = argparse.ArgumentParser(description='ACA VA LA DESCRIPCION DEL PROGRAMA')
    parser.add_argument('-seqdir',  type=str, help='input name')
    parser.add_argument('-stops',  type=str, help='type of stops codons treatment')
    parser.add_argument('-binarydir',  type=str, help='.txt que contiene una secuencia de 0 y 1 para seleccionar que zonas son de interes')
    parser.add_argument('-protalign', action='store_const', const = True, default = False, help='if True will return cleaned protein aligment ')
    parser.add_argument('-outputname', type=str, help='output name', default = "parcial.fasta")
    parser.add_argument('-outputnamealign', type=str, help='output name for the protein aligment', default = "aligment.fasta")
    parser.add_argument('-tupla', type=tuple, help='lista de tuplas que contiene las zonas de interes')
    parser.add_argument('-codon_table', type=int, help='number of the codon table to use', default = 1)
#esto carga los argumentos en una variable    
    args = parser.parse_args()
#esto envia los argumentos a la funcion parcial, coimo argumentos para la funcion.    
    parcial(args.seqdir,args.protalign,args.outputname,args.tupla,args.outputnamealign,args.codon_table,args.binarydir,args.stops)
