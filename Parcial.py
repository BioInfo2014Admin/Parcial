# -*- coding: utf-8 -*-

def parcial(seqdir,protalign,outputname,tupla,outputnamealign,codon_table,binary,stops):

	"""This function cleans codon alignments by gaps and stop codons removal, allowing
	the user to select zones, generate a protein alignment and select output name and
	format. 

	Input file must be .fasta or .phylip alignment sequences. The function has two
	options to remove stops codons, the first one directly remove all the secuences 
	with premature codons and the other remove all the secuence after the first stop
	codon found. By default the funtion doesn't remove stop codons. The function also
	has two ways to selects zones to keep and zones to eliminate . The first one is
	introducing a sequence of "0" and "1" into the input file. The second way is 
	introducing a list of tuples as an argument.

	Arguments:
	-seqdir- alignment file 
	-protalign- protein alignment
	-outputname- exit file name
	-tupla- list of tuples for zone selection
	-outputnamealign- protein alignment file name
	-codon_table- genetic code number (http://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi)
	-stops- c or d. c removes all sequences with premature codons. d removes the nucleotides in
	 all sequences found after the first stop codon.

	>>> parcial("ejemplo.fasta",False,"alineamiento.fasta",None,"alineamientoprot.fasta",1,None,None)
	>>> parcial("ejemplo.fasta",True,"alineamiento.fasta",None,"alineamientoprot.fasta",1,None,None)
	>>> parcial("ejemplo.fasta",False,"alineamiento.fasta",[(0,9),(27,30)],"alineamientoprot.fasta",1,None,None)
	>>> parcial("ejemplo.fasta",False,"alineamiento.fasta",None,"alineamientoprot.fasta",1,"binary.txt",None)
	>>> parcial("ejemplo.fasta",False,"alineamiento.fasta",None,"alineamientoprot.fasta",1,None,"c")
	>>> parcial("ejemplo.fasta",False,"alineamiento.fasta",None,"alineamientoprot.fasta",1,None,"d")"""


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
        raise Exception("Wrong argument -stops: it should be c or d, instead it was "+str(stops))   
    ID = ID._ID(seqdir)
    array =Infile._input(seqdir)
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
