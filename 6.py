a=int(input("enter a number"))
f=0
while a!=0 :
    
    f=f*10+(a%10)
    a=a//10
print("reverse of this number",f)
    