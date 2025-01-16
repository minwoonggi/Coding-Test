n = int(input())

distance = list(map(int,input().split()))
pay = list(map(int,input().split()))

sum= 0
min= pay[0]
for i in range(n-1):
  sum+=min*distance[i]
  if(min > pay[i+1]):
    min = pay[i+1]
print(sum)