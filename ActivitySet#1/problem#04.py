

hrs = input("Enter hours? ")
hrs = input("Enter Hours:")
h = float(hrs)
rate=input("enter rate:")
p=float(rate)
  
if h>40:
    x=float(40*p)+float(h-40)*float(1.5*p) 
    print(x)