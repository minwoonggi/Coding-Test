N, new_scroe, P = map(int, input().split())
if(N > 0):
  arr = list(map(int, input().split()))
else:
  arr=[]
arr.append(new_scroe)
arr.sort(reverse=True)
if (len(arr)-arr[::-1].index(new_scroe))>P :
  print(-1)
else:
  print(arr.index(new_scroe)+1)