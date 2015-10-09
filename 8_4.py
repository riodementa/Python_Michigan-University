
fhand = open("romeo.txt")
my_list=[]
for linea in fhand:
    palabras = linea.strip().split()
    for palabra in palabras:
        if not palabra in my_list:
            my_list.append(palabra)
my_list.sort()
print my_list   
