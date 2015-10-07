# Exercise 7.2
filename = raw_input("Introduzca el nombre del fichero:   [o pulsa INTRO] ")
import numpy as np
if filename=="":
    filename = "mbox-short.txt"

confidences_list=[]

fhand= open(filename)
for element in fhand:
    if element.startswith("X-DSPAM-Confidence:"):
        confidence = float((element.strip()).split()[1])
        confidences_list.append(confidence)
        
print "Valor medio de probabilidad de spam: ", np.mean(confidences_list)
        
