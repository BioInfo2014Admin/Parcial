# -*- coding: utf-8 -*-
def _zoneselector(input_array, tuple_selection=None, selection_01=None):
    """
    The function receive an array and a selection of the zones of interest that want to be maintained in
    the output array of this algorithm. The selection can be made via tuple-selection or zero-one selection.
    
    Arguments:
    -input_array-      alignment matrix    
    -tuple_selection-  list of tuples of two elements, which means the two columns in alignment that
                       flanks the columns of interest
    -selection_01-     string of a .txt file directory which contains a single line of 0s and 1s, the 
                       interest columns are represented with 1s. The binary line should have the same 
                       lenght of the alignment.

    Examples:

    >>> import numpy
    >>> arr=numpy.array([['A','T','G','C','T','T'],['A','T','G','G','T','A']])

    With no expecification given, the program doesn't make any change in the input matrix
 
    >>> _zoneselector(arr)
    array([['A', 'T', 'G', 'C', 'T', 'T'],
           ['A', 'T', 'G', 'G', 'T', 'A']], 
          dtype='|S1')

    Selecting zones using list of tuples. 

    >>> _zoneselector(input_array=arr,tuple_selection=[(0,3)])
    array([['A', 'T', 'G'],
           ['A', 'T', 'G']], 
          dtype='|S1')
    
    Selecting zones using binary selection.

    >>> with open("zeros.txt","w") as arch:
    ...    arch.write("000111")
    >>> _zoneselector(input_array=arr,selection_01="zeros.txt")
    array([['C', 'T', 'T'],
           ['G', 'T', 'A']], 
          dtype='|S1')

    If your selection affects the reading frame, the program will let you know and will ask you whether to continue or not.
    
    .>> _zoneselector(arr,[(0,2)])
    Warning, your tuple selection affects the reading frame
    Continue anyways?[Y/N]

    You can't use both selection methods!

    >>> _zoneselector(input_array=arr,tuple_selection=[(0,3)],selection_01="zeros.txt")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 51, in _zoneselector
    Exception: Double zone selection. Choose only one way of zone selection
    
    Other common errors:

    >>> with open("zeros.txt","w") as arch:
    ...    arch.write("00011")
    >>> _zoneselector(input_array=arr,selection_01="zeros.txt")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 77, in _zoneselector
    Exception: The binary sequence given must have the same lenght of the alignment

    >>> with open("zeros.txt","w") as arch:
    ...     arch.write("000a11")
    >>> _zoneselector(arr,selection_01="zeros.txt")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 85, in _zoneselector
    Exception: 'selection_01' file can only contain 0 or 1

    """
    if tuple_selection!=None and selection_01!=None:
        raise Exception("Double zone selection. Choose only one way of zone selection")
    import numpy as np
    Y="Y"
    N="N"
    if tuple_selection != None and selection_01==None:
        selection_array=np.zeros((len(input_array),0))
        flag="good"
        for i in range(0,len(tuple_selection)):
            R=tuple_selection[i][1]-tuple_selection[i][0] 
            if R%3!=0 or tuple_selection[i][0]%3!=0:
                flag="error"
        if flag=="error":
            print("Warning, your tuple selection affects the reading frame"+"\n"+"Do you want to continue?[Y/N]")
            ans=""
            while ans!="Y":
                ans=input()
                if ans=="N":
                    raise Exception("End")
        for i in range(0,len(tuple_selection)):
            selection_array=np.hstack([selection_array, input_array[:,tuple_selection[i][0]:tuple_selection[i][1]]])
        return(selection_array)
    elif tuple_selection==None and selection_01!=None:
        handle=open(selection_01,"r")
        zero_ones=[i for i in handle.read()]
        handle.close()
        if len(zero_ones)!=len(input_array[0]):
            raise Exception("The binary sequence given must have the same lenght of the alignment")
        tr01=[0]
        tr10=[0]
        flag="good"
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
                    flag="error"
        if flag=="error":
            print("Warning, your tuple zero-one selection affects the reading frame"+"\n"+"Continue anyway?[Y/N]")
            ans=""
            while ans!="Y":
                ans=input()
                if ans=="N":
                    raise Exception("End")           
        columns_to_delete=[]
        for i in range(0, len(zero_ones)):
            auxlist1=[j for j, r in enumerate(zero_ones) if r=="0"]
            columns_to_delete.extend(auxlist1)
        selection_array=np.delete(input_array,columns_to_delete,1) ###
        return(selection_array)
    elif tuple_selection==None and selection_01==None:
        return(input_array)
