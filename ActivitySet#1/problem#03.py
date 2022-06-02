def computepay(h,r):
	if h>40:
   		z=(h*r)+(h-40)*(0.5*10.5)
        return z 
    
	else:
   		y=h*r
		return y

h=float(input("enter hours:"))
r=float(input("enter rate:"))
      


z=computepay(h,r)
print("Pay",z)	
       




