# Dictionaries

filename = "dataset/mbox-short.txt"
p=input("enter file:")
c=open(p)
l=list()
for line in c:
    if not line.startswith("From:"):
        continue
    word=line.split()
    l.append(word[1])
    
counts=dict()
for word in l:
    counts[word]=counts.get(word,0)+1
    
bigcount= None
bigword= None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
        
print (bigword,bigcount)        

    