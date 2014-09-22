"""
Parcial

"""

def parcial(dirseq="",formatseq="fasta",protalign=True,outputformat="fasta",outputname="parcial",tupla=""):
    """ aca van los ejemplos
    """
    import tofasta
    import Selectingbyzones
    import limpiezagaps
    import limpiezastops
    import alinprot
    import outfile
#primero transformamos el input a fasta
    seq = _tofasta(dirseq)
#enviamos al modulo que lo corta
    matriz = _zoneselector(seq,tupla)
#enviamos al modulo que limpia gaps
    matrizsingaps = _limpiezagaps(matriz)
#enviamos al modulo que limpia stops
    matrizlimpia = _limpiezastops(matriz)
#cuando corresponda, generamos el alineamiento de proteinas
    if protalign == True:
        alineamientoproteina = _alinprot(matrizlimpia)
#transformamos al formato deseado por el user
    matrizfinal = _outfile(matrizlimpia,outputname,outputformat)

    with open(str(outputname), "w") as archivofinal:
        archivofinal.write(matrizfinal)
    if protalign == True:
        with open(str(outprotalign),"w") as palfinal:
            palfinal.write(alineamientoproteina)            
            
        
        
    
	

if __name__ == "__main__":
    import argparse
#estos sos los argumentos que cargara el programa
#falta sacarle el print aca nada mas.
    parser = argparse.ArgumentParser(description='ACA VA LA DESCRIPCION DEL PROGRAMA')
    parser.add_argument('-seqdir',  type=str, help='input name')
    parser.add_argument('-formatseq', type=str, help='input format',default = "fasta")
    parser.add_argument('-protalign', action='store_const', const = True, default = False, help='if True will return cleaned protein aligment ')
    parser.add_argument('-outputformat', type=str, help='output format',default = "fasta")
    parser.add_argument('-outputname', type=str, help='output name', default = "parcial")
    parser.add_argument('-tupla', type=tuple, help='lista de tuplas que contiene las zonas de interes',default="")
    args = parser.parse_args()
    print(parcial(args.seqdir,args.formatseq,args.protalign,args.outputformat,args.outputname,args.tupla))
