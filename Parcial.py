# -*- coding: utf-8 -*-

def parcial(seqdir,protalign,outputname,tupla,outputnamealign,codon_table,binary,stops):

    """This function cleans codon alignments by gaps and stop codons removal, allowing
	the user to select zones, generate a protein alignment and select output name and
	format. 

	Input file must be .fasta or .phylip alignment sequences. The function has two
	options to remove stops codons: the first one removes all the sequences 
	with more than one stop codon and the other one removes the position in all the sequences
	where a stop codon is found. By default the function doesn't remove stop codons.
	The funtion can select portions of the secuence, this can be done by introducing
	a 0 and 1 sequence as a plane file text (-binary name.txt). Finally, if the user 
	wants the protein alignment(-protalign), the function will translate the codon alignment
	with the option of choosing a desired codon table or leaving the default one. 
	

	Arguments:
	-seqdir- alignment file 
	-protalign- protein alignment
	-outputname- exit file name
	
	-outputnamealign- protein alignment file name
	-codon_table- genetic code number (http://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi)
	-stops- c or d. "c" removes all the sequences with premature stop codons. "d" removes the position
	of the alignment where stops codons are found.
	 

	>>> parcial("./examples/example.fasta",False,"alineamiento.fasta",None,"alineamientoprot.fasta",1,None,None)
	>>> parcial("./examples/example.fasta",True,"alineamiento.fasta",None,"alineamientoprot.fasta",1,None,None)
	
	>>> parcial("./examples/example.fasta",False,"alineamiento.fasta",None,"alineamientoprot.fasta",1,"./examples/binary.txt",None)
	>>> parcial("./examples/example.fasta",False,"alineamiento.fasta",None,"alineamientoprot.fasta",1,None,"c")
	>>> parcial("./examples/example.fasta",False,"alineamiento.fasta",None,"alineamientoprot.fasta",1,None,"d")"""


#Here we import the modules
    from modules import Infile
    from modules import Selectingbyzones
    from modules import gap_cleaner
    from modules import removestops
    from modules import alignproteins
    from modules import outfile
    from modules import ID
 

    
   
    
    if binary == None or "." in binary:
	pass
    else:
        raise Exception("wrong argument -binary: it should be name.txt , instead it was "+str(binary)) 

    if type(codon_table) == int:
        pass
    else:
        raise Exception("wrong argument -codon_table: it should be 1,2,3,4,5,6,7,8,9,10 or 11, instead it was "+str(codon_table)) 


    if stops == "d" or stops == "c" or stops == None:
        pass
    else:
        raise Exception("wrong argument -stops: it should be c or d, instead it was "+str(stops))   
    ID = ID._ID(seqdir)
    array =Infile._input(seqdir)
#We send it  to the cutting module
    
    interestarray = Selectingbyzones._zoneselector(array,tupla,binary)
    
#We send it to the gap cleaner module
    
    nogapsarray = gap_cleaner._gap_cleaner(interestarray)
#We send it to the sotp codones cleaner module
    final = removestops._remove_stops(nogapsarray,codon_table,ID,stops)
    
#Ir returns the alignment protein, when necessary
    if protalign == True:
        arrayprotalign = alignproteins._Alignproteins(final[0],codon_table)   

#The user transforms it into the desired format and this is sent to a file
    
    outfile._outfile(final[0],outputname,final[1])

    if protalign == True:
    	outfile._outfile(arrayprotalign,outputnamealign,final[1])
               
            
        
        
    
	

if __name__ == "__main__":
    import argparse
#These are the arguments that the program will take in

    parser = argparse.ArgumentParser(description='Here goes the description of the program')
    parser.add_argument('-seqdir',  type=str, help='input name')
    parser.add_argument('-stops',  type=str, help='type of stops codons treatment')
    parser.add_argument('-binarydir',  type=str, help='.txt that contains a 0 and 1 sequence to select zones of interest')
    parser.add_argument('-protalign', action='store_const', const = True, default = False, help='if True will return cleaned protein aligment ')
    parser.add_argument('-outputname', type=str, help='output name', default = "parcial.fasta")
    parser.add_argument('-outputnamealign', type=str, help='output name for the protein aligment', default = "aligment.fasta")
    parser.add_argument('-tupla', type=str, help='tuple list containing the zones of interest')
    parser.add_argument('-codon_table', type=int, help='number of the codon table to use', default = 1)
#This fits the arguments into a variable    
   
    args = parser.parse_args()
    args.tupla = None
#This sends the arguments to the function "parcial" as usable arguments for the function
    parcial(args.seqdir,args.protalign,args.outputname,args.tupla,args.outputnamealign,args.codon_table,args.binarydir,args.stops)
