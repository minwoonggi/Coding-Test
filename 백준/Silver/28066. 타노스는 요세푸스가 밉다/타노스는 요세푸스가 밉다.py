from collections import deque
import sys
N,K = map(int, sys.stdin.readline().rstrip().split())
arr = deque([i for i in range(1,N+1)])
while N-K>=0:
  N-=K-1
  t = arr.rotate(-1)
  for _ in range(K-1):
    arr.popleft()
print(arr[0])


