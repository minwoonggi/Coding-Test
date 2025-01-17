N = int(input())

for _ in range(N):
  i = int(input())
  arr = list(map(int, input().split()))
  arr.reverse()
  max = arr[0]
  cnt = 0
  for j in range(1,i):
    if(arr[j]>max):
      max = arr[j]
    else:
      cnt+= (max-arr[j])
  print(cnt)