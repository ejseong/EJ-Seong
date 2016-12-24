# deleted some commnets - 12/1

#problem 3

with open("c:\\python\\codetable.txt","r")as ins:

    a=[]
    for line in ins:
        s=line[:-1] #remove \n
        c=s[0]
        r=s[2:].split(',')
        a.append([c,r])
    

d={}
for x in a:
    for y in x[1]:
        z=y.replace('"','').replace(' ','')
        
        d[z]=x[0]





geno= open("c:\\python\\genome (1).txt","r")
newlist=[]
alist=[]



   
#remove \n - 
for x in geno:
    if"\n"in x:
        x=x.replace("\n","")
        alist.append(str(x))
    else:
        alist.append(str(x))



 #remove ''   
alist=''.join(alist)




#split to 3 

i=0
while len(newlist) <= int((len(alist))/3):
    n=3
    newlist.append(alist[i:i+n])
    i=i+n



result=[]


for i in range(len(newlist)):
    if newlist[i] in d.keys():
        result.append(d[newlist[i]])
      


 

newfile=open("c:\\python\\yeast.txt","w")

for x in result:
    newfile.write("{0}\n".format(x))

newfile.close()
ins.close()
geno.close()