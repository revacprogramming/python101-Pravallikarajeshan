# Lists

filename = "dataset/romeo.txt"
p=input("enter the file name:")
c=open(p)
l=list()
for line in c:
    words=line.split()
    for word in words:
        if word in l:
            continue
        if word not in l:
            l.append(word)
            	
                
               
                
        
   
print(sorted(l))            
