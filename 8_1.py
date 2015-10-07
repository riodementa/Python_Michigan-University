# Excercise 8_1
def recorta(lista):
    
    # Type1:
    """"
    # Remove first element
    lista.pop(0)
    # Remove last element
    lista.pop()
    """  
    
    # Type2:
    del lista[0]
    
    my_length=len(lista)
    del lista[my_length-1]       
    
    return None   
    
# Testing
my_list=["a","b","v","d"]
recorta(my_list)
print my_list
