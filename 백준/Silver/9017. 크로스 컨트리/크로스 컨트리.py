import sys
N = int(input())

for _ in range(N):
  arr = [[0 for _ in range(8)] for _ in range(201)]
  length = int(sys.stdin.readline())
  num = list(map(int, sys.stdin.readline().rstrip().split()))
  for i in range(length):
    arr[num[i]][0]+=1
  cnt=1

  for i in range(length):
    if(arr[num[i]][0]==6):
      arr[num[i]][7]+=1
      arr[num[i]][arr[num[i]][7]]=cnt
      cnt+=1
  min = 100000
  awr = -1

  for i in range(201):
    if arr[i][0]==6:
     if(sum(arr[i][1:5])<min):
       awr=i
       min = sum(arr[i][1:5])
     elif  sum(arr[i][1:5])==min:
       if(arr[i][5]<arr[awr][5]):
          awr=i
  print(awr)


  