T=int(input("Enter how many test u want to do:-"))
list = []
p=[]
for i in range(T) :
    name=input("enter a string (try to go in alphabetical order)")
    list.append(name)
    a=len(name)
    p.append(a)

for i in range(T) :
    s=list[i]
    count=0
    for k in range(0,p[i]//2) :
        # for j in range(0,u) :
         #ord is letter to ascii and chr is to from ascii to letter 
            r=ord(s[k])
            e=ord(s[p[i]-k-1])
            # print(r)
            # print(e)
            # if r!=e :
            x=abs(r-e)
            # diff=abs(ord(s[k])-ord(s[p[i]-k-1]))       
            count=count+x
    print(count)
print("\n")
                
            
    
            
