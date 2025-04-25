#a tree (height of that tree is 1 meter)
s=int(input("Enter test cases how many you want to try"))
numbers=[]
for i in range(s) :
    num=int (input("Enter a number"))
    numbers.append(num)
    
for i in range(s) :
    a=1
    for k in range(numbers[i]) :
        
        if k==0 :
            a=1
        if  k//2!= 0 :
            a=a*2    
        if  k//2== 0:
            a=a+1
    print("Length of utopian tree is ",a)
print("\n")        
            
    