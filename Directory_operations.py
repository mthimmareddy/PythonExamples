import os
import os.path

#def findfile(path1):
#path1=os.getcwd()
#print path1
#list1=os.listdir(path1)

def findfile(path1):
    print path1
    list1=os.listdir(path1)
    for i in list1:
        print i
        
        if (i =="manju.txt"):
             print 'File found :{} is file'.format(i)
             break   
        
        elif(os.path.isdir(i)):
            path2=path1+"\\"+i
            print path2
            print '{} its a Directory'.format(i)
             #path2=os.getcwd()
             #path2+='i'
             #print path2
            findfile(path2)
        
       # else:
           #  print 'file not found'    
       
findfile(os.getcwd())       
    
        


