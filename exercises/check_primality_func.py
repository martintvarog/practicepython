
# input number num
num = int(input('Insert a number: '))
# list a = x pro  x v rozmezi 2 až num pokud zbytek pod deleni num /x == 0
a = [x for x in range(2, num) if num % x == 0]


#def is prime   
def is_prime(num):
    # pokud je čislo vetší jak 1
	if num >= 1:
        #pokud je delka listu rovna 0
		if len(a) == 0:
            # je to prvocislo
			print ('prime')
        #jinak    
		else:
            #neni to prvocislo
			print ('NOT prime')
    #jinak        
	else:
        #neni to prvocislo
		print ('NOT prime')

        
# call func is_prime(num)	
is_prime(num)



