#import sys
#import os
#from selenium.webdriver.common import keys

print 'hello World'
#integer variables
a=10
print a

#String Variables
msg="Hi this is my first program"
print msg
#String Operations

print len(msg)
print msg.capitalize()
print msg.isalpha()
#This converts string into list
words=msg.split()
#list variables which stores array of values
print words
names=['manju','rishi','Ravi','pavan','mom','dad']
values=['12','23','45','65','6','7','7']
#print values
for i in values:
    print i
new_list=words+names
print new_list

#list operations
values.append(78)
print values
#values.extend(34)
values.insert(3, 64)
print values
#values.remove(12)
values.pop()
print values
#values.index(3,)
print values.count(64)
print values
values.sort(cmp=None, key=None, reverse=False)
print values
values.reverse()

print values


#Dictionaries

states={'Karnataka':'KA','Delhi':'DL','Madya pradesh':'MP'}
print states

print states['Karnataka']

for keys in states:
    print   states[keys]
    



    
#for i in words:
    #print i

