N = list(map(int, input()))
if N.count(0)==0:
  print(-1)
else:
  sum=0
  for i in N:
    sum+=i
  if(sum%3!=0):
    print(-1)
  else:
    N.sort(reverse=True)
    for j in N:
      print(j,end="")

  