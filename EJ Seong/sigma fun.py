
#Problem 1

import math

def sum(start,stop,f,c):
    s=0   
    for i in range(start,stop+1):
        s+=f(i)
    print("{0}={1}".format(s,(c(stop)-c(start-1)))) 


def sumOne(Startnumber,Stopnumber):
    return (sum(Startnumber,Stopnumber,(lambda x: (2*x)+1), (lambda x :(x+1)**2))) 


def sumTwo(Startnumber,Stopnumber):
    return(sum(Startnumber,Stopnumber,(lambda x: x**2),(lambda x: (x*(x+1)*((2*x)+1))/6)))

def sumThree(Startnumber,Stopnumber): #formular is incorrect
    return (sum(Startnumber,Stopnumber,(lambda x: 1/(((x)**3)+x)),(lambda x: ((math.pi)**2)-1)))

def sumFour(Startnumber,Stopnumber):
    return (sum(Startnumber,Stopnumber,(lambda x: 1/((x**2)+(2*x))),(lambda x: 3/4-1/(2*(x+1))-(1/(2*(x+2))))))

sumOne(10,200)

