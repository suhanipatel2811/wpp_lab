list = [0,1]

for i in range(2,100) :
    list.append(list[i-1]+list[i-2])
a=int(input("Enter how many number you want to type:-"))
numbers = []
for i in range(a) :
    num=int(input("enter a number"))
    numbers.append(num)
for i in range(a) :  
    if numbers[i] in list :
        print(f"{numbers[i]} is a fibonacci number")
    else :
        print(f"{numbers[i]} is not a fibonacci number")    