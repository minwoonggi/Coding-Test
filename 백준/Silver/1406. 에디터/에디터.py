import sys
str1 = list(input())
str2 = []
N = int(input())

for _ in range(N):
  command = list(sys.stdin.readline().strip().split())
  if command[0] == "L" and str1:
    str2.append(str1.pop())
  elif command[0] == "D" and str2:
    str1.append(str2.pop())
  elif command[0] == "P":
    str1.append(command[1])
  elif command[0] =="B" and str1:
    str1.pop()
str2.reverse()

str1.extend(str2)

print("".join(map(str,str1)))