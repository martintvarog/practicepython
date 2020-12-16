a = 5
b = 0
c = 1

def compace(a,b,c):
    if a > b and a > c:
        print(str(a) + " largest is A")
    elif b > a and b >c:
        print(str(b) +"largest is B")
    elif c > a and c > b:
        print(str(c)+ "largest is C")

compace(a,b,c)

# with max func

maxN = max(a,b,c)

print(maxN)