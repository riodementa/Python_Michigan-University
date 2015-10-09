fhand = open("mbox-short.txt")
my_dict = dict()
for element in fhand:
    if element.startswith("From:"):
        position = element.strip().find("@")
        mail =  element[position:].strip()
        if mail in my_dict:
            my_dict[mail] += 1
        else:
            my_dict[mail] = 1

print my_dict
