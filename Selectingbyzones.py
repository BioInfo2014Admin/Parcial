# -*- coding: utf-8 -*-
#Hola, la primer función es necesaria para la segunda, y probablemente les sirva a ustedes.
#
#
def _zoneselector(input_array, tuple_selection=None, selection_01=None):
    if tuple_selection!=None and selection_01!=None:
        raise Exception("Double zone selection. Choose only one way of zone selection")
    import numpy as np
    import pandas as pd
    import scipy
    if tuple_selection != None and selection_01==None:
        selection_array=np.zeros((len(input_array),0))
        for i in range(0,len(tuple_selection)):
            R=tuple_selection[i][1]-tuple_selection[i][0] 
            if R%3!=0 or tuple_selection[i][0]%3!=0:
                raise Exception("Warning, your tuple selection affects the reading frame")
#                return("Warning, your tuple selection affects the reading frame"+"\n"+"Continue aniways?[Y/N]")
#                ans=input()
#                if ans==["Y"]:
#                    pass
            selection_array=np.hstack([selection_array, input_array[:,tuple_selection[i][0]:tuple_selection[i][1]]])
        return(selection_array)
    elif tuple_selection==None and selection_01!=None:
        handle=open(selection_01,"r")
        zero_ones=[i for i in handle.read()]
        handle.close
        tr01=[0]
        tr10=[0]
        for i in range(0,len(zero_ones)-1):
            try:
                r=int(zero_ones[i])
            except:
                raise Exception("'selection_01' file can only contain 0 or 1")
            if r!=0 and r!=1:
                raise Exception("'selection_01' file can only contain 0 or 1")
            if zero_ones[i]+zero_ones[i+1]=="01":
                tr01.append(i+1)
            elif zero_ones[i]+zero_ones[i+1]=="10":
                tr10.append(i+1)
        for i in range(0,len(tr01)):
            for j in range(0,len(tr10)):
                if (tr01[i]-tr10[j])%3!=0:
                    raise Exception("Warning, your zero-one selection affects the reading frame")
        columns_to_delete=[]
        for i in range(0, len(zero_ones)):
            auxlist1=[j for j, r in enumerate(zero_ones) if r=="0"]
            columns_to_delete.extend(auxlist1)
        selection_array=scipy.delete(input_array,columns_to_delete,1) ###
        return(selection_array)
    elif tuple_selection==None and selection_01==None:
        return(input_array)
#
#
