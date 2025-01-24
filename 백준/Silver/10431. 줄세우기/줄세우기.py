import sys

N = int(input())

arr = [[0] for _ in range(N+1)]

for _ in range(N):
  num = list(map(int,sys.stdin.readline().rstrip().split()))
  max= num[1]
  order = []
  order.append(num[1])
  cnt=0
  for i in range(2,21):
    if(num[i]>max):
      order.append(num[i])
      max= num[i]
    else:
      for j in range(len(order)):
        if num[i]<order[j]:
          order.insert(j,num[i])
          cnt+=(len(order)-j-1)
          break
  arr[num[0]][0] = cnt
for i in range(1,N+1):
  print(i,arr[i][0])