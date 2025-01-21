arr = list(input())

n = 0
idx = 0

while True:
  n+=1
  for chr in str(n):
    if arr[idx] == chr:
      idx+=1
      if(idx >= len(arr)):
        print(n)
        exit()