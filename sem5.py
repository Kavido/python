from math import sqrt


xa = float(input('введите х1 '))
ya = float(input('введите у1 '))
xb = float(input('введите х2 '))
yb = float(input('введите у2 '))
t1 = xa-xb
t2 = ya-yb
c1 = t1*t1
c2 = t2*t2
c = sqrt(c1+c2)
print (c )