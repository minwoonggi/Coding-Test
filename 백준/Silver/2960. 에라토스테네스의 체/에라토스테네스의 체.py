N,K = map(int, input().split())

arr = [i for i in range(N+1)]
cnt=0
for i in range(2,N+1):
  if arr[i] !=0:
    cnt+=1
    if(cnt==K):
      print(arr[i])
      break
    for j in range(i+i,N+1,i):
      if(arr[j]!=0):
        cnt+=1
        if(cnt==K):
          print(arr[j])
          break
        arr[j]=0

