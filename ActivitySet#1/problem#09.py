# Lists

filename = "dataset/romeo.txt"
p=input("enter the number:")
c=open(p)
l=list()
for line in c:
    words=line.split()
    for word in words:
        if word in l:
            continue
        l.append(word)    
   
print(sorted(l))            

    
        