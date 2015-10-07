# Exercise 7.3 (Easter Egg)
filename = raw_input("Introduzca el nombre del fichero:   [o pulsa INTRO] ")
count = 0
try:    
    if filename== "na na boo boo":
        print "NA NA BOO BOO PARA TI - ¡Te he pillado!"
    else:
        fhand = open(filename)
        for element in fhand:
            count += 1
        print "Hay", count, "líneas subject en", filename
except:
    print "No se pudo abrir el fichero:", filename
