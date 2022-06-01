# Files
fname = input("Enter file name: ")
fh =open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("From:"):
        continue
        y=line.find(':')
        
        x=line[y+1:]
      
        z=float(x)
      
        count=count+1
        total=total+z
average=total/count
print("Average spam confidence:",aver