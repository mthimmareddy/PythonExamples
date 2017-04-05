
count=1
def call(count):
 if count !=100:
  print (count)
  count=count+1
  call(count) 
  
call(count)
