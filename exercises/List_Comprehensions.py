
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100,202,980,981]#entry list

new_list = []#create new_list 
for number in a:# for var in list a loop thru
    if int(number)%2 ==0:# if module of var is equal to 0
        new_list.append(number)# add var numb to list

print(new_list)# pnt list

print([x for x in a if x%2 == 0])


