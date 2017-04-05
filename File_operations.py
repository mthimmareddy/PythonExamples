'''
Modes 'r+', 'w+' and 'a+' open the file for updating (reading and writing); 
note that 'w+' truncates the file. Append 'b' to the mode to open the file in binary mode 

'''
#__doc__ is inbuilt python keyword to print documentation or comments
print __doc__
f1=open("manju.txt",'w+')
f1.write("Manju is very hard working")
print  f1.mode
f1.close()
f1=open("manju.txt",'r')
print f1.read()
