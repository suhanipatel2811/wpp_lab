p= input("enter a word")
s = "" 
for  i in range(len(p)) :
    if i%2 ==0 :
        s += p[i].lower()
    else :
        s+= p[i].upper()
        
print(s)
        