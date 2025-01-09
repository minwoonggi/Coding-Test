N =int(input())
Y=0
M=0

numbers = map( int ,input().split())

for i in list(numbers):
  Y += (i//30+1)
  M += (i//60+1)
  
if(Y*10<M*15):
  print(f"Y {Y*10}")
elif(Y*10==M*15):
  print(f"Y M {Y*10}")
else:
  print(f"M {M*15}")
  