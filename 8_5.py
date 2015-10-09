fhand = open("mbox-short.txt")
counter=0
for element in fhand:
    if element.startswith("From"):
        counter += 1
        print element.strip().split()[1]
print "Hay",counter,"lineas en el archivo con From como primera palabra"
