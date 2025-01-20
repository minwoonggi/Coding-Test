while 1:
  str = input()
  if str =="end":
    break
  rule_1 = False
  rule_2 = True
  rule_3 = True
  vowel = "aeiou"
  for chr in vowel:
    if chr in str:
      rule_1 = True
      
  for i in range(1,len(str)):
    if str[i] == str[i-1] and str[i] not in {'e','o'}:
      rule_2 = False
  
  v = 0
  c = 0
  
  for i in range(len(str)):
    if str[i] in vowel:
      v+=1
      c=0
      if(v==3 or c==3):
        rule_3 = False
    else:
      c+=1
      v=0
      if(v==3 or c==3):
        rule_3 = False
  if(rule_1 and rule_2 and rule_3):
    print(f"<{str}> is acceptable.")
  else:
    print(f"<{str}> is not acceptable.")
