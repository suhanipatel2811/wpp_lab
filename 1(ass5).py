a=int(input("Enter a number"))
b=int(input("Enter another number"))
max=0
for i in range(a,b+1) :
    for j in range(i,b+1):
        s=i^j
        if(max<s):
            max=s
print(max)            