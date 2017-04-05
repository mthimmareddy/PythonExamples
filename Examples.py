#1.Validate the ip adderess

def ipcheck():
 
 import re

 pattern="[0-255]\.[0-255]\.[0-255]\.[0-255]"
 if re.match(pattern, "10.55.55.20"):
  print ("Match found")
 else:
  print ("Not Found")




#2.Validate the mail id
def mailcheck():

 import re
 pattern="(\w)+\@(\w)+\.(\w)"

 if re.match(pattern,"manju@gmail.com"):
  print ("match found")
 else:
  print ("not found")


def telephone():

#3.TO validate the telephone number

 import re
 
 pat1=r"(((\+)?1)?((\s)+)?(\(?(\d){3})\)?((-|\s)?)(\(?(\d){3})\)?((-|\s)?)(\d){4})"

 pat=r"\+12623665056"

 match=re.match(pat1,"+12623665056")
 if match:
  print (match.groups())

 match=re.match(pat1,"+1 262 366 5056")
 if match:
  print ("found 1")


 match=re.match(pat1,"+1 (262)(366) 5056")
 if match:
  print ("found 2")

 match=re.match(pat1,"+1 262-366-5056")
 if match:
  print ("found 3")

def numlines():
#4.To Count number of lines in file

 with open("text.txt",'r') as f:
    print (len(f.readlines()))

 with open("file",'r') as f:
     print (sum(1 for _ in f))


 count=0
 with open("file1",'r') as f:
  for line in f:
        count =count+1
 print ("Total number of  words in file {0}".format(count))



def charfile():
 #5.To count the character in file
 count=0
 with open("file1",'r') as f:
  for line in f:
    for word in line:
        for ch in word:
           if ch !="\n":
            count =count+1
 print ("Total number of charachters in file {0}".format(count))



def wordsfile():
 #6.To count the  words in file

 import re
 pattern=r"(\w+)?|;|,"
 count=0
 list1=[]
 list2=[]
 with open("file1",'r') as f:
   line=f.read()
   print (line)
   list1=re.findall(pattern,line)
   #list3=line.split("\\s|\\n")
  
   for i in list1:
    if i:
      list2.append(i)
 print (list2)
 print ("Total number of words in file {0}".format(len(list2)))


  # if match:
   # print ("Match found",match.groups(1))

def trailing():
 #7.To remove trailing spaces in string
 string="This is my hi:hello,world"
 long_string=""
 list1=string.split(" ")
 for i in list1:
  long_string += i

 print (long_string)

def endspace():
 #8.To remove end and start spaces in string
 import re
 string1="  This is my world  "

 print (string1.strip())

#pattern=r"^\s+(\w)+\s$"
#new_pattern=r"(\w)+"
#new_string=re.sub(pattern,new_pattern,string1)
#print (new_string)


def duplicate():

#9.Duplicate words and count number of times of occurance in files .
 import re
 count={}
 with open("test",'r')as f:
  text=f.read()
  pattern=r"\w+|,|;"
  list1=re.findall(pattern,text)
  print (list1)
  for word in list1:
   if re.match(r"\w+",word):  
    if word not in count:
        count[word]=1
    else:
        count[word]+=1

 for word in count:
  print ("The word {0} has occured {1} times in file".format(word,count[word]))

      
def dupchar():      
 #10.Find duclicate characters and replace in string
 import re
 string1="ringaringaroses"
 list1=[]
 count={}

 for i in string1:
  list1.append(i)
 for ch in list1:
     if ch not in count:
        count[ch]=1
     else:
        count[ch]+=1
        

 for word in count:
  print ("The word {0} has occured {1} times in file".format(word,count[word]))


def duplist():
#11.Find the duplicate number is list
 list1=[1,2,3,3,5,3,4]
 flag=0
 for i in range(len(list1)-1):
   for j in range(1,len(list1)):
     if list1[i]==list1[j]:
       flag=1
     else:
       flag=0
   if(flag):
    print (list1[i],"is a duplicate") 
   else:
    print ("Not duplicate")

def dupcharfile():
 #11.Find duplicate characters in files
 import re
 count={}
 with open("test",'r')as f:
  text=f.read()
  pattern=r"\w+|,|;"
  list1=re.findall(pattern,text)
  print (list1)
  for word in list1: 
    for ch in word:
     if ch not in count:
        count[ch]=1
     else:
        count[ch]+=1

 for word in count:
  print ("The word {0} has occured {1} times in file".format(word,count[word]))

def fact():
#12.To find the factorial without recoursion

 n=4
 fact=1
 for i in range(1,n+1):
  if i==1 or i==0 :
   fact*=1
  else:
   fact=fact*i

 print("Factorial of number is :{0}".format(fact))



def listofdict():
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

 # print(values)


 d=dict(zip(listall[0],map(list,zip(*values))))
 print (d)

 list2=[]
 for i in range(1,len(listall)):
  dict1=dict(zip(listall[0],listall[i]))
  list2.append(dict1)

 print(list2)

def listofdict1():
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


options={1:ipcheck,2:mailcheck,3:telephone,4:numlines,5:charfile,6:wordsfile,7:trailing,8:endspace,9:duplicate,10:dupchar,11:duplist,12:dupcharfile,13:fact,14:listofdict,15:listofdict1}
for ch in range(1,16):
 options[ch]()

options[7]()

