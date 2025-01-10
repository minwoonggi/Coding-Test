N = int(input())
T = N
new_num = -1
cnt= 0
while N!=new_num :
  cnt+=1
  num = T
  if(num<10):
    num*10
  sum_num =  num//10+ num%10
  new_num = (num%10*10 + sum_num%10)
  T= new_num
  
print(cnt)
  
  