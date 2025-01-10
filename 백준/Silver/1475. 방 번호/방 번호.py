import math
N = input()

arr = list(map(int, N))

count_num = [0 for _ in range(10)]

for i in arr:
  count_num[i] +=1


t= math.ceil((count_num[9]+count_num[6])/2)
count_num[9],count_num[6]=t,t
print(max(count_num))

