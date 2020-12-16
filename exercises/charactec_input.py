

try:
    name = input("Your name is: ")
    age = input("Your age is:   ")
    num_copies = int(input("Kolik kopií:    "))

    for age_100 in range(num_copies):
        age_100 = int(2020) + (int(100) - int(age))
        print(str(age_100) + "\n")



except ValueError:
    print("špatný vstup")

