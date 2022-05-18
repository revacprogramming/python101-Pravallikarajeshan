# Tuples

filename = "dataset/mbox-short.txt"
p=input("enter the file")
c=open(p)
x=tuple()


for line in c:
    if line.startswith ("From:"):
        continue
    word=line.split()
    
    counts=dict()   
    for time in c:
         counts[time]=counts.get(time,0)+1
   
    
time=None
hour=None

for time,hours in counts.items():
    x=sorted(time,hours)
print(x)    