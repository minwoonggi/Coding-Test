
n=int(input())

first_str = list(input())
first_str.sort()
cnt=0
for i in range(n-1):
  str = list(input())
  str.sort()
  if(str==first_str):
    cnt+=1 
  elif (len(str)==len(first_str)):
    for i in range(len(str)):
      correct = 0
      for k in range(65,91):
        str_copy = str.copy()
        str_copy[i]=chr(k)
        str_copy.sort()
        if(str_copy==first_str):
          cnt+=1
          correct=1
      if(correct==1):
        break
  elif (len(str)+1==len(first_str)):
    for k in range(65,92):
      str_copy = str.copy()
      str_copy.append(chr(k))
      str_copy.sort()
      if(str_copy==first_str):
          cnt+=1
          break
  elif(len(str)-1==len(first_str)):
    for k in range(len(str)):
      str_copy = str.copy()
      str_copy.pop(k)
      str_copy.sort()
      if(str_copy==first_str):
        cnt+=1
        break
print(cnt)
      
      
      