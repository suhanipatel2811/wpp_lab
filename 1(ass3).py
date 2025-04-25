n= int(input("Enter a number :"))
def digital_root(n) :
    p=0
    while n!=0 :
        s=n%10
        p=p+s
        n=n//10
    if p>9 :
        digital_root(p)
    else :
        print(p)
digital_root(n)
    
        
    