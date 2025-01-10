import sys
N = int(input())
arr = []
for _ in range(N):
  command = sys.stdin.readline().strip().split()  
  if command[0] == "push":
    arr.append(command[1])
  elif command[0] == "pop":
    if not arr:
      print(-1)
    else:
      print(arr.pop())
  elif command[0] == "size":
    print(len(arr))
  elif command[0] == "empty":
    if not arr:
      print(1)
    else:
      print(0)
  elif command[0] == "top":
    if not arr:
      print(-1)
    else:
      print(arr[-1])

  