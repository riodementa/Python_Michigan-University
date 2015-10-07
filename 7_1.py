# Exercise 7.1
filename = raw_input("Introduzca el nombre del fichero:   [o pulsa INTRO]")

if filename=="":
    filename = "mbox-short.txt"
    
fhand= open(filename)
for element in fhand:
    a= element.strip().upper()
    print a
