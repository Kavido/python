from math import factorial  
n = int(input('введите число ')) 
list1 = [factorial(x) for x in range(1, n+1) ] 
print ( list1 )