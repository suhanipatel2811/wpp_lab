import math
T=int(input("Enter how many test u want to do:-"))
int1=[]
int2=[]

for i in range(T) :
    count=0
    a=int(input("Enter a integer1:- "))
    b=int(input("Enter a integer2:- "))
    int1.append(a)
    int2.append(b)
    for j in range(a,b+1) :
        if(math.sqrt(j).is_integer()) :
            count =count+1
    print(count)