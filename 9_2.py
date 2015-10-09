fhand = open("mbox-short.txt")
my_dict = dict()
for element in fhand:
    try:
        if element.startswith("From"):
            day = element.split()[2]
            if day in my_dict:
                my_dict[day] += 1
            else:
                my_dict[day] = 1
                
    except:
        continue
print my_dict
