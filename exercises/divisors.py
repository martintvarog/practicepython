"""Create a program that asks the user for a number and then prints out a 
list of all the divisors of that number. (If you don’t know what a divisor is, 
it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)"""

num = int(input("Please choose a number to divide: "))# enter number

listRange = list(range(1,num+1))# listRange is list with items in range 1 to number + 1

divisorList = []# create list divisor

for number in listRange: #for number in listRange
    if num % number == 0: # if number's module(zbytek) is = to 0
        divisorList.append(number)# add number to the list

print(divisorList)


print([number for number in listRange if num% number == 0])