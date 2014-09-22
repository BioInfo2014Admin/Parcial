"""
Parcial

"""

def parcial(dirseq="",formatseq="fasta",protalign=True,outputformat="fasta",outputname="parcial"):
    """ aca van los ejemplos
    """
    import tofasta
    import cortar
    import limpiezagaps
    import limpiezastops
    import alinprot
    import tooutputformat
#primero transformamos el input a fasta
    seq = tofasta(dirseq)
#enviamos al modulo que lo corta
    matriz = cortar(seq)
#enviamos al modulo que limpia gaps
    matrizsingaps = limpiezagaps(matriz)
#enviamos al modulo que limpia stops
    matrizlimpia = limpiezastops(matriz)
#cuando corresponda, generamos el alineamiento de proteinas
    if protalign == True:
        alineamientoproteina = alinprot(matrizlimpia)
#transformamos al formato deseado por el user
    matrizfinal = tooutputformat(matrizlimpia)

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
    args = parser.parse_args()
    print(parcial(args.seqdir,args.formatseq,args.protalign,args.outputformat,args.outputname))
