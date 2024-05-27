def tpl_sort(tupl):
    for element in tupl:
        if not isinstance(element,int):
            return tupl            
    return tuple(sorted(tupl))
print(tpl_sort((3,4,0,1,7,12,)))



    
    
        

            

