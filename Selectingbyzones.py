#Hola, la primer función es necesaria para la segunda, y probablemente les sirva a ustedes.
#
#
def _Recepcion(Inputfasta):
    """
    str--> matrix
    Recibe la dirección del archivo de alineamiento en fasta (Inputfasta) como un string, parsea y toma las secuencias. Con estas genera una matriz donde las columnas corresponden a las columnas de un alineamiento y las filas a cada secuencia.
    
    Parametros
    ---------
    Inputfasta : Debe ser la dirección de un archivo de alineamiento en .fasta, debe ingresarse entre comillas.
    
    """
    from Bio import SeqIO
    import numpy as np
    Archivoparseado = SeqIO.parse(Inputfasta,"fasta")
    Listasecuenciasinput=[record for record in Archivoparseado] #genero listas con secuencias parseadas
    Paraformarmatriz=[[i for i in str(Listasecuenciasinput[j].seq)] for j in range(0,len(Listasecuenciasinput))] #a partir de la lista anterior genero una lista que contiene las secuencias en formato lista: cada nucleótido es un elemento. Me queda algo así: [[A,T,G],[G,T,T],[T,C,A]]
    Arrayalineamiento=np.array(Paraformarmatriz) #la lista de listas anterior la puedo utilizar directamente para formar la matriz que quiero, donde las columnas quedan alineadas.
    return(Arrayalineamiento) #expulsa el array
#
#
def _Selecciondezonas(Inputfasta, Inseleccion=None):
    """
    Construye un array (¿o dataframe?) con las zonas seleccionadas
    
    Parameters
    ----------
    Inputfasta : 
                Debe ser la dirección de un archivo de alineamiento en .fasta, debe ingresarse entre comillas.
    Inseleccion : Lista de tuplas
        Cada tupla de la lista debe poseer con los # de las columnas que franquean los bloques que quiero seleccionar 
        Ejemplo Inseleccion=[
    
    Returns
    -------
    Un array (#o dataframe?)
    """
    import numpy as np
    import pandas as pd
    Arrayalineamiento=_Recepcion(Inputfasta)
    if Inseleccion != None:
        Lista=[]
        Arrayseleccion=np.zeros((len(Arrayalineamiento),0))
        for i in range(0,len(Inseleccion)):
            Arrayseleccion=np.hstack([Arrayseleccion, Arrayalineamiento[:,Inseleccion[i][0]:Inseleccion[i][1]]])
            for j in range(Inseleccion[i][0],Inseleccion[i][1]):
                Lista.append(j)
        #return(Arrayseleccion)
        return(pd.DataFrame(Arrayseleccion,columns=Lista))
    else:
        #return(Arrayalineamiento)
        return(pd.DataFrame(Arrayalineamiento))
#
#
