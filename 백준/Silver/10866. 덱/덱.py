import sys
from collections import deque
N = int(input())
arr = deque([])

for _ in range(N):
  command = sys.stdin.readline().strip().split()
  if command[0] == "push_front":
    arr.appendleft(command[1])
  elif command[0] == "push_back":
    arr.append(command[1])
  elif command[0] == "pop_front":
    if arr:
      print(arr.popleft())
    else:
      print(-1)
  elif command[0] == "pop_back":
    if arr:
      print(arr.pop())
    else:
      print(-1)
  elif command[0] == "size":
    print(len(arr))
  elif command[0] == "empty":
    if not arr:
      print(1)
    else:
      print(0)
  elif command[0] == "front":
    if arr:
      print(arr[0])
    else:
      print(-1)
  elif command[0] == "back":
    if arr:
      print(arr[-1])
    else:
      print(-1)
    