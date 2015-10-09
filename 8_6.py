maxValue=0
minValue=0
while True:
    userChoice = raw_input("Introduce un numero:")
    
    if userChoice == "fin":
        print "Máximo:",maxValue
        print "Mínimo:",minValue
        break
       
    try:
        user_number = float(userChoice)

        if user_number=="fin":
            exit()
        else:
            if user_number > maxValue:
                maxValue = user_number
            elif user_number < minValue:
                minValue = user_number
            else:
                continue
    except:
        print "Wrong number! Try again"
