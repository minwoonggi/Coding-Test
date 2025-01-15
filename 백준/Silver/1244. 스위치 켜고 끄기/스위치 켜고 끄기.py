N =  int(input())

def chage(n):
  if n==1:
    return 0
  else:
    return 1

num  = list(map(int, input().split()))
num.insert(0,0)
std_num = int(input())
for _ in range(std_num):
  gender , center = map(int,input().split())
  if gender==1:
    cnt=1
    while cnt*center <=N:
      num[cnt*center] = chage(num[cnt*center])
      cnt+=1
  if gender==2:
    num[center] = chage(num[center])
    left= center-1
    right = center+1
    while left>0 and right<N+1:
      if(num[left]==num[right]):
        reverse= chage(num[left])
        num[left]=reverse
        num[right]=reverse
        left-=1
        right+=1
      else:
        break
cnt=1
for i in num[1:]:
  print(i,end=" ")
  if cnt%20==0:
    print()
  cnt+=1
  