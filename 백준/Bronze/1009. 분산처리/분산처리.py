N =int(input())
for i in range(N):
  num1, num2 = map(int,input().split())
  k= (num1**(num2%4+4))%10
  if k == 0:
    print(10)
  else:
    print(k)