s=0
p=0
import random
list=[random.randint(0,1) for i in range(100)]
for i in list:
    if(i==0):
        s=s+1
        p=max(s,p)
    else :
        s=0

print(p)
    
