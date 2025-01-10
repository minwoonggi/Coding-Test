N = int(input())

def gcd(a,b):
  n= a%b
  if(n==0):
    return b
  else:
    return gcd(b,n)

for _ in range(N):
  A,B = map(int, input().split())
  awr= A*B//gcd(A,B)
  print(awr)
  
  
  