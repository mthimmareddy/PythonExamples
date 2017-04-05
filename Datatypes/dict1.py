
states={'karnataka':'KA','Madya pradesh':'MP','Kerala':'KE'}

cities={'Bangalore':'BA','unknown':'UN','Telangana':'TE'}

#Way to iterate over dict items
for name in states:
 print ("The state {0}  has this abbrevatiom {1}".format(name,states[name]))


#dict.items() returns the key value pair of tuples
print (states.items())


for abre,name in cities.items():
 print("{0} the state has this city {1}".format(abre,name))

marks=[[1,2,3],[4,5,6],[1,2,4],[2,3,4]]
m1=[1,2,3]

#List comprehensions
m2=[x*x for x in m1]
m3=[x*y for x in m1 for y in marks ]
print(m3)
print (marks)
#print (zip(*marks))
#print (map(list,zip(marks)))

m1=[]

#print (m1)'''

for row in marks:
  m=[]
  for val in row:
    m.append(val)
  m1.append(m) 
  print (m1)
 # print (m)
