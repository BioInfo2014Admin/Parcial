# -*- coding: utf-8 -*-
def _zoneselector(input_array, tuple_selection=None, selection_01=None):
    """
    The function receive an array and a selection of the zones of interest that want to be maintained in
    the output array of this algorithm. The selection can be made via tuple-selection or zero-one selection.
    
    Arguments:
    -input_array-      alignment matrix    
    -list_selection-   list of lists of two elements, which means the two columns in alignment that
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

    >>> _zoneselector(input_array=arr,list_selection=[[0,3]])
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
    Warning, your selection affects the reading frame
    If you want to continue, the program will expand your selection to fit the reading frame
    Do you want to continue?[Y/N]

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
    import numpy as np
    if list_selection==None and selection_01==None:
        return(input_array)
    elif list_selection!=None and selection_01!=None:
        raise Exception("Double zone selection. Choose only one way of zone selection")
    elif list_selection==None and selection_01!=None:
        handle=open(selection_01,"r")
        zero_ones=[i for i in handle.read()]
        handle.close()
        zero_ones.pop()
        if len(zero_ones)!=len(input_array[0]):
            raise Exception("The binary sequence given must have the same lenght of the alignment")
        if zero_ones[0]=="1":
            IN=[0]
        NEW=[]
        for i in range(0,len(zero_ones)-1):
            try:
                r=int(zero_ones[i])
            except:
                raise Exception("'selection_01' file can only contain 0 or 1")
            if r!=0 and r!=1:
                raise Exception("'selection_01' file can only contain 0 or 1")
            if zero_ones[i]+zero_ones[i+1]=="01":
                IN=[]
                IN.append(i+1)
            elif zero_ones[i]+zero_ones[i+1]=="10":
                IN.append(i+1)
                NEW.append(IN)
        if zero_ones[len(zero_ones)-1]=="1":
            IN.append(len(zero_ones))
            NEW.append(IN)
        list_selection=NEW
    selection_array=np.zeros((len(input_array),0))
    flag="good"
    for i in range(0,len(list_selection)):
        R=list_selection[i][1]-list_selection[i][0] 
        if R%3!=0 or list_selection[i][0]%3!=0:
            flag="error"
    if flag=="error":
        print("Warning, your selection affects the reading frame")
        print("If you want to continue, the program will expand your selection to fit the reading frame")
        print("Do you want to continue?[Y/N]")
        ans=""
        while ans!="Y":
            ans=input()
            if ans=="N":
                raise Exception("End")
        for i in range(0,len(list_selection)):
            if list_selection[i][0]%3!=0:
                s1=list_selection[i][0]%3
                list_selection[i][0]=list_selection[i][0]-s1
                #list_selection[i][1]=list_selection[i][1]-s1
            R=list_selection[i][1]-list_selection[i][0]
            if R%3!=0:
                s2=3-list_selection[i][1]%3
                list_selection[i][1]=list_selection[i][1]+s2    
    for i in range(0,len(list_selection)):
        selection_array=np.hstack([selection_array, input_array[:,list_selection[i][0]:list_selection[i][1]]])
    return(selection_array)
