import math
length = int(input())
n = int(input())
light = list(map(int , input().split()))
arr = []
for i in range(n-1):
  arr.append(math.ceil((light[i+1]-light[i])/2))
arr.append(length-light[n-1])
arr.append(light[0])
print(max(arr))