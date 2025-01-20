import math

height, width, a,b = map(int , input().split())

p = math.ceil(height/(a+1))

q = math.ceil(width/(b+1))

print(p*q)


