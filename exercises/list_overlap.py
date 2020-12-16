# Python program to find the common elements  
# in two lists
# using 'bitwise and' and sets  
def common_member(a, b): #func common_member
    a_set = set(a) #converts a[] to set(a)
    b_set = set(b) ##converts b[] to set(b)
  
    if (a_set & b_set): # if a_set and bitwise b_set
        print(a_set & b_set) #print a_set and bitwise b_set
    else: 
        print("No common elements")  
           
   
a = [1, 1, 2,2,2,2,2,2,2, 3, 5, 8, 13, 21, 34,120,120, 55, 89]
b = [1,120, 2, 3, 4,5,5,5,5,5,5, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_member(a, b) 
