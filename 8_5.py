filename = raw_input("Introduce un nombre de fichero: (o pulsa ENTER):")

try:
    fhand = open(filename)
except:
    print "Filename not found! Test with mbox-short.txt\n"
    fhand = open("mbox-short.txt")

counter=0
for element in fhand:
    if element.startswith("From"):
        counter += 1
        print element.strip().split()[1]
print "\nHay",counter,"lineas en el archivo con From como primera palabra"
