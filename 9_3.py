fhand = open("mbox-short.txt")
my_dict = dict()
for element in fhand:
    if element.startswith("From:"):
        word =  element.split()[1]
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
print my_dict
