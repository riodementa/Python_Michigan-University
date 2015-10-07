# Exercise 5.1
import numpy as np

max=0
min=0
list_numbers=[]

while True:
    str_number = raw_input("Introduce un numero: ")    
    
    if str_number=="fin":
        break
    
    try:
        number = float(str_number)
        if number>=max:
            max=number
        elif number<=min:
                min=number   
        else:
            continue
                
    except:
        print "Entrada inválida" 
        continue
    
    list_numbers.append(number)

print sum(list_numbers), np.size(list_numbers), np.mean(list_numbers)
