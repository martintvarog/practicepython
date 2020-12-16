number = input("Input number:   ")

mod = int(number) % 2
multiply_of_4 = int(number) % 4

if mod >0:
	print("u picked odd number")
else:
	print("u picked even number")

if multiply_of_4 >0:
	print("u picked number is NOT multiplied by 4")
else:
	print("u picked number multiplied by 4")
#print(isinstance(x, int))