from random import randrange
import random

def common_member(a, b): #func common_member
    a_set = set(a) #converts a[] to set(a)
    b_set = set(b) ##converts b[] to set(b)

    
    print([numbers for numbers  in (a_set&b_set) if (a_set&b_set)])
    
           

   
a = random.sample(range(1,100), 20)
print("A input is:  " + str(a))

b = random.sample(range(1,100), 20)
print("B input is:  " + str(b))

common_member(a, b) 



#print([x for x in a if x%2 == 0])