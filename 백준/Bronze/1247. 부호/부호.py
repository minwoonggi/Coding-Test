for i in range(3):
  N = int(input())
  S= 0
  for j in range(N):
    num = int(input())
    S+=num
  if(S>0):
    print("+")
  elif(S<0):
    print("-")
  else:
    print("0")