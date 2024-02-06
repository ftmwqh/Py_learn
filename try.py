from sympy import (symbols,diff,Rational,integrate,lambdify)
import sympy
from math import *
v0,y0,x,g,theta=symbols('v0 y0 x g theta')
y=x*sympy.tan(theta)-1/(2*v0**2)*g*x**2/(sympy.cos(theta)**2)+y0
f=lambdify([v0,y0,theta,g,x],y)
print(f(v0=15,y0=1.0,g=9.8,theta=pi/3,x=0.5))





M,c,p,K,T0,Ty,Tw=symbols('M c p K T0 Ty Tw')
t=M**(2/3)*c*p**(1/3)/(K*pi**2*(4*pi/3)**(2/3))*sympy.log(0.76*(T0-Tw)/(Ty-Tw))
t0=lambdify([M,c,p,K,Ty,T0,Tw],t)

print(t0(M=47,c=3.7,p=1.038,K=5.4*10**(-3),T0=4,Ty=70,Tw=100))
print(t0(M=67,c=3.7,p=1.038,K=5.4*10**(-3),T0=4,Ty=70,Tw=100))

print(18//5)


try:
    c=float('a')
except ValueError:
    print('cant')