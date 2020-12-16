
# thinks of a number

MaxRangeNumbers = int(input("Lenght?    "))

while guess:

    if len(MaxRangeNumbers) == 2:
        guess = MaxRangeNumbers / 2
        rada = input("Too high, too low, just right:    ")
        if rada == "too low":
            guess +=1
        elif rada == "too high":
            guess += -1
        elif rada == "just right":
            print("number is " + str(guess))
            break
    elif len(MaxRangeNumbers) == 3:
        guess = MaxRangeNumbers / 
        rada = input("Too high, too low, just right:    ")
        if rada == "too low":
            guess +=1
        elif rada == "too high":
            guess += -1
        elif rada == "just right":
            print("number is " + str(guess))
            break

        
    