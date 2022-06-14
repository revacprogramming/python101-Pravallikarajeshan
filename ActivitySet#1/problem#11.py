#TUPL
filename = "dataset/mbox-short.txt"
p =input("Enter the file name")
c= open(p)
d=dict()
X=tuple()
for line in c:
    if not line.startswith("From "): 
        continue....
    else:    
        line=line.split()
        line=line[5]
        line=line[0:2]
        d[line]=d.get(line,0)+1

lst=list()        
for value,count in d.items():
    lst.append((value,count))

lst.sort()
for value,count in lst:
    print (value,count)
