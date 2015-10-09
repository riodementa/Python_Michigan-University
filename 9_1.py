fhand = open("words.txt")
my_dict=dict()
for line in fhand:
    for word in line.split():
        my_dict[word]=1

print "Rio" in my_dict
print "or" in my_dict
