
list1=[23,45,56,78,89]
num=[None]*5
#print ("Enter the list numbers")
i=1
sum1=0
for i in range(1,5):
 num[i]=input("Enter num:")
 if not num[i] in list1:
   sum1=sum1+num[i]
   i=i+1
 else:
   break
print ( sum1) 
#print ("Average:{0}"+ sum1) 
