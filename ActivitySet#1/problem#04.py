#conditinal excecution


hrs = input("Enter hours? ")
hrs = input("Enter Hours:")
h = float(hrs)
rate=input("enter rate:")
p=float(rate)
  
if h>40:
    x=float(40*p)+float(h-40)*float(1.5*p) 
    print(x)

#ppp

score = input("Enter Score: ")
p=float(score)

if (p>=0.9):
    print("A")
elif (p>=0.8):
    print("B")
elif (p>=0.7):
    print("C")
elif (p>=0.6):
    print("D")
elif (p>0.6):
    print("F")
else:
    print("error")
    