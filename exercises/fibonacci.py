
# def fib number
def fib(n):
    # numb a
    a = 0
    #numb b
    b = 1
    print(a)
    print(b)
    # for _ in range 2 to n
    for _ in range(2,n):
        #
        c = a + b 
        a = b
        b = c
        print(c)
fib(18)


