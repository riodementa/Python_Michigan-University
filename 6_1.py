# Exercise 6.1
import numpy as np

cadena = raw_input("Introduce una cadena: ")   
my_length = len(cadena)

while my_length>0:
    my_length -= 1
    print cadena[my_length]
