
P = input("Enter file:")
C = open(P)
for line in C:
    line=line.rstrip()
    import re
    line=re.findall(('[0-9]+'),line)
    if len(num)<1:
        continue
    num=int(num)
    line.append(line)
    sum=num
print(sum)..