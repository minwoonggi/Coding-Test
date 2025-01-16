N, length = map(int, input().split())

num = list(map(int, input().split()))


cnt=1
max=sum(num[:length])
now=sum(num[:length])
for i in range(N-length):
  now=now-num[i]+num[i+length]
  if(max< now):
    max=now
    cnt=1
  elif max==now:
    cnt+=1

if max==0:
  print("SAD")
else:
  print(max)
  print(cnt)