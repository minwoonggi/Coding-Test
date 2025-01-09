A = int(input())
B = int(input())
C = int(input())
MUX = A*B*C
k = [0 for _ in range(10)]
arr = list(map(int , str(MUX)))
for i in arr:
  k[i]+=1
for i in range(10):
  print(k[i])