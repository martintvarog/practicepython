import random

def guess():
    
    try:
        number_of_guesses = 0
        i = 0
        while i != -1:
            number = int(input("Random number from 1 to 9:  "))    
            random_number = random.randint(1,9)
            if random_number > number:
                print("You've picked too low")
            elif random_number < number:
                print("You've picked too high")
            else:
                print("You've picked exactly right")
            i += 1
            number_of_guesses += 1
            exit = input("For exit write: 'exit' ")
            if exit == "exit":
                print("Number of guesses    " + str(number_of_guesses))
                break
            else:
                continue
    except ValueError:
        print("wrong input")
    

guess()