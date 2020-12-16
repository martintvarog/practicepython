import random

rand_numbers_list = []
while len(rand_numbers_list) < 4:
    rand_numb = random.randint(1,9)
    rand_numbers_list.append(rand_numb)


number = int(input("Number  "))
user_numb_list = [int(number) for number in str(number)] 

result_list = []


RandN = set(rand_numbers_list) #converts a[] to set(a)
UserN = set(user_numb_list) ##converts b[] to set(b)
  
    
for number in (RandN&UserN): 
    if (RandN&UserN):
        result_list.append(number)
    if len(result_list) >




print(result_list)