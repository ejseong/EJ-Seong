#problem 2

def convert(n,b):
    i=0
    new=""
    while n != 0:
        bi=n%b
        n=n//b
        i=i+1
        bi=str(bi)
        new=bi+new    
    return (new)

#print(convert(10,2))


def transform(number,base,anotherbase):
    number=str(number)
    numberlist=list(map(int,number))
    numberlist=(numberlist[::-1])
    baseTen=0
    for i in range(len(numberlist)):
        baseTen+=numberlist[i]*base**i
    return(convert(baseTen,anotherbase))
    
 
    
 

print(transform(11010,2,3))


def convert1(number,newbase):
    i=0
    b=[]
    while number is not 0:
        b.append(number%newbase)
        number=int(number/newbase)
        i=i+1
    b=(b[::-1])
    b=''.join(map(str,b))
    return int(b)



def transform1(number,base,anotherbase):
    number=str(number)
    numberlist=list(map(int,number))
    numberlist=(numberlist[::-1])
    baseTen=0
    for i in range(len(numberlist)):
        baseTen+=numberlist[i]*base**i
    return(convert1(baseTen,anotherbase))

#print(transform(11010,2,3))
    
    