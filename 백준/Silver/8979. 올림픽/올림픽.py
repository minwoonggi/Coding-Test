import sys

N , nation = map(int,input().split()) 

arr = [[0 for _ in range(3)]for _ in range(N+1)]

for _ in range(N):
  num = list(map(int,sys.stdin.readline().rstrip().split()))
  arr[num[0]][0] = num[1]
  arr[num[0]][1] = num[2]
  arr[num[0]][2] = num[3]

cnt=1

for i in range(1,N+1):
  if(arr[nation][0]<arr[i][0]):
    cnt+=1
  elif(arr[nation][0]==arr[i][0]):
      if(arr[nation][1]<arr[i][1]):
        cnt+=1
      elif(arr[nation][1]==arr[i][1]):
        if(arr[nation][2]<arr[i][2]):
          cnt+=1
print(cnt)