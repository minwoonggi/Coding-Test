from collections import deque

N , M = map(int, input().split())
arr = deque([i for i in range(1,N+1)])

num  = list(map(int ,input().split()))
Total_cnt = 0

for i in range(M):
  cnt_1=0
  cnt_2=0
  arr_1 = arr.copy()
  arr_2 = arr.copy()
  while arr_1[0] != num[i]:
    cnt_1 +=1
    t = arr_1.pop()
    arr_1.appendleft(t)
  while arr_2[0] != num[i]:
    cnt_2 +=1
    t = arr_2.popleft()
    arr_2.append(t)
  if(cnt_1>cnt_2):
    Total_cnt+=cnt_2
  else:
    Total_cnt+=cnt_1
  arr_1.popleft()
  arr=arr_1.copy()
  
print(Total_cnt)  