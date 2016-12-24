
#problem 4 

from timeit import default_timer as timer

def Fib(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return (Fib(n-1)+Fib(n-2))
    

for n in range(1,40):
    start=timer()
    print("f({0})={1}took {2} seconds.".format(n,Fib(n),timer()))