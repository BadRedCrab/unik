import math
a,b,c=float(input("ax^2+bx+c=0\na=")),float(input("b=")),float(input("c="))
print(f"x = {(-b)/(2*a)}" if (b**2-4*a*c)==0 else f"x1= {(-b+math.sqrt((b**2-4*a*c)))/(2*a)} \nx2= {(-b-math.sqrt((b**2-4*a*c)))/(2*a)}" if (b**2-4*a*c)>0 else "Нет действительных корней")