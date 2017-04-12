import re


list1=[]
list2=[]
listall=[]
keys=[]
dict1={}
d={}





with open("test2.txt", 'r') as f:
  for line in f:
     keys=re.findall("\w+",line)
     for item in f:
       listall.append(re.findall("\w+",item))

d=dict(zip(keys,map(list,zip(*listall))))
print (d)

for i in range(0,len(listall)):
 dict1=dict(zip(keys,listall[i]))
 list2.append(dict1)



print(list2)

