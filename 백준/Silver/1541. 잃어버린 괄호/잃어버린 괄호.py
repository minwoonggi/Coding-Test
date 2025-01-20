chr = list(input())

is_discount = False
is_num=True
num=''
sum = 0
for i in range(len(chr)):
  if(chr[i]=="-"):
    is_discount = True
  elif(chr[i]=='0' and (i==0 or is_num==False or chr[i-1] in {'+','-'})):
    is_num =False
  elif(chr[i]=='+'):
    num=''
    is_num=True
  else:
    num += chr[i]
    is_num=True
    if(i+1==len(chr) or chr[i+1] in {'+','-'}):
      if(is_discount):
        sum-= (int(num))
      else:
        sum+= (int(num))
      num = ''
print(sum)