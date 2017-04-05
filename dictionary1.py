

list1=[]
listall=[]
dict1={}
d={}


with open("test2.txt", 'r') as f:
 for i in range(0,4):
  header=f.readline().strip()
  keys=[] 
  list1=header.split(" ")
  for i in list1:
   if i:
    keys.append(i)
  listall.append(keys)

# print (listall)

values=[]
for i in range(1,4):
 values.append(listall[i])

#print(values)


d=dict(zip(listall[0],map(list,zip(*values))))
print (d)

list2=[]
for i in range(1,len(listall)):
 dict1=dict(zip(listall[0],listall[i]))
 list2.append(dict1)

print(list2)

