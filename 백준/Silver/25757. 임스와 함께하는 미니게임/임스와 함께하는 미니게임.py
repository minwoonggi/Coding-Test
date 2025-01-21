import sys

a,b = input().split()

name_list = set()

for _ in range(int(a)):
  name_list.add (sys.stdin.readline().rstrip())
cnt = len(name_list)
if b == "Y":
  print(cnt)
elif b =="F":
  print(cnt//2)
else:  
  print(cnt//3)