# Exercise 6.3
def contador(chain,letter):
    counter=0
    
    for element in chain:
        if element == letter:
            print element
            counter += 1
        
    print "Number of letter '",letter,"' in the chain:", counter

contador("This is the chain test for counting a's","a")
