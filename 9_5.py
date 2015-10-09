fhand = open("mbox-short.txt")
my_dict = dict()
values=[]
for element in fhand:
    if element.startswith("From:"):
        word =  element.split()[1]
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
            
maxValue = max(my_dict.values())

for element in my_dict:
    if my_dict[element]==maxValue:
        print element, my_dict[element]
