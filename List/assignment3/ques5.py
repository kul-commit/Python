a=[2,4,5,6,7,8,4,6,3,5,32,2,2,3]
result=[]

for i in a:
   if i not in result:
      result.append(i)

high_occur=0
high_occur_element=0

for i in result:
   c= a.count(i)
   print(f"{i} occurs {c}times")  
   if c > high_occur:
      high_occur=c
      high_occur_element=i
     
print(high_occur_element)
   