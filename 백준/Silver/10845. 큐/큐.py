import sys
class Queue:
  def __init__(self):
    self.arr = []
    
  def push(self, item):
    self.arr.append(item)

  def pop(self):
    if self.arr:
      print(self.arr.pop(0))
    else:
      print(-1)
      
  def size(self):
      print(len(self.arr))
  
  def empty(self):
    if self.arr:
      print(0)
    else:
      print(1)
 
  def front(self):
    if self.arr:
       print(self.arr[0])
    else:
      print(-1)
    
  def back(self):
    if self.arr:
      print(self.arr[-1])
    else:
      print(-1)
  
Q = Queue()
N = int(input())
for _ in range(N):
  command = sys.stdin.readline().strip().split()
  if command[0] == "push":
    Q.push(command[1])
  elif command[0] == "pop":
    Q.pop()
  elif command[0] == "size":
    Q.size()
  elif command[0] == "empty":
    Q.empty()
  elif command[0] == "front":
    Q.front()
  elif command[0] == "back":
    Q.back()  
    