T=int(input("Enter how many testcases u want to try"))
list=[]
for i in range(T):
    a=int(input("Enter a number"))
    list.append(a)
for i in range(T):
    if(list[i]%2==0):
        p=list[i]/2
        s=p*p
        print(s)
    else:
        p=(list[i]-1)/2
        x=p+1
        s=x*p
        print(s)
print("\n")
        

    