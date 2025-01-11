N = int(input())
num = [0 for _ in range(10010)]
num[0]=0
num[1] =1
num[2] =1
cnt=2
if N<=2:
  print(num[N])
else:
  while(cnt<N):
    num[cnt+1] = num[cnt]+num[cnt-1]
    cnt+=1
  print(num[cnt])
    
  