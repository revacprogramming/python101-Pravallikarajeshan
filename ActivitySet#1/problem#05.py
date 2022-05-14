def computepay(h, r):
  if h>40:
    pay=(h*r)+(h-40)*(0.5*10.5)
  
  else:
    pay=h*r
  return pay

hrs=input("enter hours:")
h=float(hrs)
rate=input("enter rate:")
r=float(rate)


z=computepay(h,r)
print("Pay",z)

           
           
           
           
    