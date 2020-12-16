a = [1,1,2,3,5,8,13,21,34,55,89,3]


new_list = [] #creates new list
for variable in a: # for varible in list a 
    if variable < 5: # if variable is smaller than 5
        new_list.append(variable) # add to list varible 
print(new_list)

print([variable for variable in a if variable < 5])# 
