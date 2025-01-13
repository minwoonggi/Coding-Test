N = int(input())
arr = []
heart = [0,0]
for _ in range(N):
  arr.append(list(input()))
for a in range(N):
  for b in range(N):
    if 0<a<N-1 and 0<b<N-1:
      if arr[a][b]=="*" and arr[a-1][b]=="*" and arr[a+1][b]=="*"and arr[a][b-1]=="*"and arr[a][b+1]=="*":
        heart = [a,b]
heart_column= [column[heart[1]] for column in arr]
heart_column_left= [column[heart[1]-1] for column in arr]
heart_column_right= [column[heart[1]+1] for column in arr]
heart_row = arr[heart[0]]
print(heart[0]+1,heart[1]+1)
print(heart_row[:heart[1]].count("*"),end=" ")
print(heart_row[heart[1]+1:].count("*"),end=" ")
print(heart_column[heart[0]+1:].count("*"),end=" ")
print(heart_column_left[heart[0]+1:].count("*"),end=" ")
print(heart_column_right[heart[0]+1:].count("*"))

