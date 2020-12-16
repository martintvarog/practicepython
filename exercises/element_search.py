import random

# def compare
def compare():
    # create list
    my_list = []

    # random numbers in len(10) to list
    while len(my_list) <10:
        add = int(random.randint(0,99)) 
        my_list.append(add)
    #sort from lowest to highest
    my_list.sort()
    # input number
    number = int(random.randint(1,99))
    # loop through list to find if element i in list
    for index in my_list:
        if number in my_list:
            print( str(number) + " is in the list")
            break
        else:
            print(str(number) + " is NOT in the list" + "\nthe list was " + str(my_list))
            break
    # bitwise search    
    number_set = set(str(number))
    list_set = set(str(my_list))
    print([x for x in (number_set&list_set) if (number_set&list_set)])

compare()

