
num=4
# input("Enter the number:")

def fact1(num):
 if (num==0) | (num==1):
   return 1
 else:
   return num*(fact1(num-1))

print (fact1(num))
