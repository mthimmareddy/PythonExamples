import re
import os
import sys

Programs = '''
1.To Validate the ip adderess
2.To Validate the mail id
3.To Validate the US  number
4.To Count number of lines in file
5.To count the character in file
6.To count the  words in file
7.To remove trailing spaces in string
8.To remove end and start spaces in string
9.Find the duplicate words in files, using sets.
10.Find all the duclicate characters and replace in string
11.Find all the duplicates in list
12.Find all duplicate characters in file
13.Factorial of number without recursion
14.Find the list of dictionaries and dictionary of list for given text matrix values without any module
15.Find the list of dictionaries and dictionary of list for given text matrix values using re module
16.To find Prime Number or not
17.Demonstarte the classes in python
18.Demonstarte listsa nd strings in Python
19.To find squareroot of number
20.Print the range of numbers 1-100 witout using loops
21.Given a list find the avg of list
22.Find a fibonacci series of number without recursion
23.Find reverse of string
24.File exists
25.To find the transpose of matrix
26.List to set conversion
27.Accessing the csv
28.Reverse of string without using other string
29.To find the maximum element in list and return the value and its index

30.To find file exists in directory or not
31.Ifconfig output with different interface name,ip extraction
32.Generators demo in python

'''


###########################################################################################
###########################################################################################

def generators_square():
    #list1 = []
 def square():
     for x in range(1,100):
        yield(x*x)       #keeps the eleemnt one at time hence performance is much better
        #list1.append(x*x)
    #print(list1)
 numlist1=[x*x for x in range(1,25)] #list comprehension
 numlist2=(x*x for x in range(25,50)) #using Generators

 print(numlist2) #you cant access eleemnts all at time
 #numlist=square()
 #print(numlist1)

 for num in numlist2: #Generators ar accessed this way
    print(num)









#######################################################################################################

def maxvaluelist():
    employment=[23.4,67.0,56.7,23.0,56.8,65.6,76.7,34.4,45.6]
    max_value = 0
    index = 0
    for value in range(len(employment)):
        # print("ths country {0} has {1} employmentrate".format(countries[value],employment[value]))
        if (employment[value] > max_value):
            max_value = employment[value]
            index = value
    print("Maximum employment value is {0} has index : {1} ".format(max_value, index))

#####################################################################################################

def reversestr():

    string1="manju"
    print(string1[::-1])
    ''' 
    i=0
    j=len(string1)-1
    while(i!=j):
        tmp=string1[i]
        string1[i]=string1[j]
        string1[j]=tmp
        i=i+1
        j=j-1
    print(string1)
    '''
##############################################################################################
def listtoset():
    list1=[1,2,3,4,5,6,7,8,9,2,3,4,5]

    s=set(list1)
    print (s)


###############################################################################################

def transposematrix():
    matrix1=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print('Matrix before transpose',matrix1)
    mat2=[]
    for col in range(0,len(matrix1[0])):
        mat1=[]
        for row in range(0,len(matrix1)):
            mat1.append(matrix1[row][col])
        mat2.append(mat1)
    print ('Matrix after transpose',mat2)

    mat4=[[matrix1[row][col] for row in range(0,len(matrix1))] for col in range(0,len(matrix1[0]))]
    print(mat4)
###############################################################################################

def ipcheck():
    # 1.Validate the ip adderess
    input_ip = input('Enter the ip:')
    flag = 0

    pattern = "^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$"
    match = re.match(pattern, input_ip)
    if (match):
        field = input_ip.split(".")
        for i in range(0, len(field)):
            if (int(field[i]) < 256):
                flag +=1
            else:
                flag = 0
    if (flag == 4):
        print("valid ip")
    else:
        print('No match for ip or not a valid ip')


#########################################################################################

def mailcheck():
    # 3.Validate the mail id

    input_mail = input('Enter the mail id to validate:')
    pattern = "[^@]+@[^@]+"
    flag=0
    match=re.match(pattern, input_mail)
    if(match):
         list1=input_mail.split(".")
         print(list1)
         if(3 >= len(list1) > 1) :
             flag=1
         else:
             flag=0
    if(flag==1):
         print("Match found")
    else:
         print ("Not a valid mail id")


#########################################################################################

def telephone():
    print("Validate US telephone number")
    input_num = input('Enter the Telephone Number:')
    pattern = "^(\+)?(1)?(\s|-)?((\d{3})(-|\s)?){2}(\d{4})$"
    match = re.match(pattern, input_num)
    if match:
        print("Found telephone number")
    else:
        print("No match ")


##########################################################################################

def numlines():
    # 4.To Count number of lines in file

    with open("text.txt", 'r') as f:
        print(len(f.readlines()))
        # or
    with open("text.txt", 'r') as f:
        print(sum(1 for _ in f))


##########################################################################################3


def charfile():
    # 5.To count the character in file
    with open("text.txt", 'r') as f:
        count = 0
        for line in f:
            for word in line:
                for ch in word:
                    count = count + 1
    print('Total characters in file', count)


#########################################################################################

def wordsfile():
    # 6.To count the  words in file
    with open("text.txt", 'r') as f:
        count = 0
        text = f.read()
        list2 = []
        list2 = re.findall("\w+", text)

    print('Total words in file', len(list2))


##########################################################################################

def trailing():
    # 7.To remove trailing spaces in string
    string = "This is my world"
    long_string = null
    list1 = string.split("\s")
    for i in list1:
        long_string.append(i)
    print(long_string)


###########################################################################################
def endspace():
    # 8.To remove end and start spaces in string

    string1 = " This is spaces in begining and end  "
    print(string1)
    print(string1.strip())


############################################################################################

def duplicate():
    # 9.Duplicate words in files, using sets.

    count = {}
    line = []
    with open("text.txt", 'r')as f:
        data = f.read()
        line = re.findall("\w+", data)

        for word in line:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1

    for word in count:
        # print (count[word])
        if count[word] > 1:
            print("The word {0} has occured {1} times in file".format(word, count[word]))


###########################################################################################

def dupchar():
    # 10.find duclicate characters and replace in string

    string1 = "ringaringaroses"
    print(string1)
    count = {}
    for ch in string1:
        if ch not in count:
            count[ch] = 1
        else:
            count[ch] += 1
            #   string1[ch]=""

    for word in count:
        if count[word] > 1:
            print("The word {0} has occured {1} times in file".format(word, count[word]))


#########################################################################################33
def fact1():
    # 11.factorial without recoursion

    n = 5
    fact = 1
    while (n > 0):
        if (n == 0) or (n == 1):
            fact *= 1
            break;
        else:
            fact *= n
            n = n - 1
    print("The factorial of number is", fact)


##########################################################################################

def prime():
    # 12.Given list ,prime numbers with generators and witout generators

    list1 = [2, 3, 2,34, 23, 17, 11, 56, 25, 44, 99,7]

    #Using the list comphrensions

    prime1=[x for x in list1 if all(x % y != 0 for y in range(2, x))]
    print("Prime numbers {0}".format(prime1))

    #Withouut using comprehensions
    for i in list1:
        if (i == 3) or i == 5 or i==2:
            print("{0} Prime number".format(i))
            continue
        if (i % 2 == 0 or i % 3 == 0 or i % 5 == 0):
            print("{0} Not prime".format(i))
        else:
            print("{0} is Prime".format(i))


############################################################################################

def fileexists():
    # 13.File exists

    if os.path.isfile("text.txt"):
        print("File Exists")
    else:
        print("Not a file")


#############################################################################################

def reversestring():
    str1 = input('Enter the String')
    str2 = ""
    # j=0
    i = len(str1) - 1
    while (i >= 0):
        str2 += str1[i]
        # print (str2)
        # j=j+1
        i = i - 1
    print("{0} is original,{1} is reverse of string".format(str1, str2))


############################################################################################


def squareroot():
    num = int(input('Enter the number :'))
    x = num / 2
    i = 1
    flag = 1
    while (i < x):
        if (i * i == num):
            print("{0} is the square root of {1}".format(i, num))
            flag = 0
            break
        i = i + 1
    if (flag == 1):
        print("{0} is not a perfect square".format(num))


##################################################################################################


def printrangenumbers():
    i = 1

    def recur(i):
        if (i < 100):
            print(i)
            i = i + 1
            recur(i)

    recur(1)


####################################################################################################3


def listavg():
    list1 = [2, 3, 4, 5, 3, 4]
    sum1 = 0
    for i in list1:
        sum1 += i
    avg = sum1 / (len(list1) + 1)
    print("Average of list is:", avg)


##################################################################################################

def fib():
    def fibo(n):
        # n=int(input('Enter the number'))
        if (n == 0):
            return 0
        else:
            x = 0
            y = 1
            for i in range(1, n):
                z = (x + y)
                x = y
                y = z
            return y

    for i in range(10):
        print(fibo(i))


##########################################################################################################3

def classdemo():
    class Animal:
        def __init__(self, breed, color, age):
            self.type = type
            self.color = color
            self.age = age

        def getnames(self):
            print(self.type)

    class Dog(Animal):
        def __init__(self, breed, color, age, owner):
            Animal.__init__(self, breed, color, age)
            self.owner = owner

        def getowner(self):
            print(self.owner)

            # cat=Animal("dog" ,"brown",3)
            # cat.getnames()

    dog = Dog("dog", "brown", 3, "manju")
    dog.getowner()
    print(dog.color)


################################################################################################################

def Datatypesdemo():
    print('hello World')
    # integer variables
    a = 10
    print(a)

    # String Variables
    msg = "Hi this is my first program"
    print(msg)
    # String Operations

    print(len(msg))
    print(msg.capitalize())
    print(msg.isalpha())
    # This converts string into list
    words = msg.split()
    # list variables which stores array of values
    print(words)
    names = ['manju', 'rishi', 'Ravi', 'pavan', 'mom', 'dad']
    values = ['12', '23', '45', '65', '6', '7', '7']
    # print values
    for i in values:
        print(i)
    new_list = words + names
    print(new_list)

    # list operations
    values.append(78)
    print(values)
    # values.extend(34)
    values.insert(3, 64)
    print(values)
    # values.remove(12)
    values.pop()
    print(values)
    # values.index(3,)
    print(values.count(64))
    print(values)
    values.sort(cmp=None, key=None, reverse=False)
    print(values)
    values.reverse()

    print(values)

    # Dictionaries

    states = {'Karnataka': 'KA', 'Delhi': 'DL', 'Madya pradesh': 'MP'}
    print(states)

    print(states['Karnataka'])

    for keys in states:
        print(states[keys])


###########################################################################################################3

def duplist():
    print("To find duplicates in list")
    list1=[1,2,3,4,5,2,6,7,8,4]
    count={}
    for num in list1:
        if num not in count:
            count[num]=1
        else:
            count[num]+=1
    print(count)

    for i in count:
        if (count[i]>1):
            print("The {0} has occured {1} times".format(i,count[i]))

    #Other way using the bubble sort method
    k=1
    for i in range(0,len(list1)-1):
     for j in range(k,len(list1)):

            if (list1[i] == list1[j]):
                print("Duplicate found:", list1[i])
                #continue
     k+=1


###########################################################################################################
import os.path

def findfile():
 search_file=input('Enter the file name:')
 flag=0
 dirlist=os.listdir(os.getcwd())
 print (dirlist)
 for file1 in dirlist:
     if file1==search_file:
         flag=1
         break
     else:
         flag=0
 if (flag==1):
     print("File Found in current directory {0}".format(os.getcwd()))
 else:
   for file1 in dirlist:
     if(os.path.isfile(file1)!=True):
         path2=os.getcwd()+"\file1"
         for file2 in os.listdir(path2):
            if file2==search_file:
                flag1=1
                break
            else:
                flag1=0
 if (flag1 == 1):
  print("File Found in current directory {0}".format(path2))








##############################################################################################################



###########################################################################################################
def listofdict():
    list1 = []
    listall = []
    dict1 = {}
    d = {}

    with open("text2.txt", 'r') as f:
        header = f.readline().strip()
        keys = []
        keys = header.split("\t")
        print(keys)
        for line in f:
            list1 = line.strip().split("\t")
            # print (list1)
            listall.append(list1)

    print(listall)

    #Transpose of listall is mat2
    mat2 = []
    for col in range(0, len(listall[0])):
        mat1 = []
        for row in range(0, len(listall)):
            mat1.append(listall[row][col])
        mat2.append(mat1)
    print('Matrix after transpose', mat2)

#Dictionay of lists
    for i in range(0,len(keys)):
        d[keys[i]]=mat2[i]
    print (d)

#list of dictionaries

    list1=[]

    for i in range(0,len(listall)):
        d1={}
        for j in range(0,len(listall[0])):
          d1[keys[j]]=listall[i][j]
        print(d1)
        list1.append(d1)
    print(list1)

'''
#Using zip,map,and dict
    d = dict(zip(keys, map(list, zip(*listall))))
    print(d)

    list2 = []
    for i in range(0, len(listall)):
        dict1 = dict(zip(keys, listall[i]))
        list2.append(dict1)

    print(list2)
'''
#####################################################################################################################
import unicodecsv
def accesscsv():
  print("CSV reading")
  datacsv=[{'firstnam': 'manju', 'sirname': 'thimmareddy', 'hobby': 'writing', 'age': '29'},
  {'firstnam': 'rishi', 'sirname': 'shereddy', 'hobby': 'dancing', 'age': '3'},
  {'firstnam': 'ravi', 'sirname': 'chandra', 'hobby': 'reading', 'age': '33'}]

#Accessing without module
  
  for ele in datacsv:
      for word in ele:
          print (word,ele[word])


#######################################################################################################################

def read_csv(filename):
  list1=[]
  with open(filename,'r') as f:
      reader=unicodecsv.DictReader(f)
      for row in reader:
        list1.append(row)
      #list1=list(reader)
  print(list1)




#####################################################################################################################

def listofdict1():
    import re

    list1 = []
    list2 = []
    listall = []
    keys = []
    dict1 = {}
    d = {}

    with open("test2.txt", 'r') as f:
        for line in f:
            keys = re.findall("\w+", line)
            for item in f:
                listall.append(re.findall("\w+", item))

    d = dict(zip(keys, map(list, zip(*listall))))
    print(d)

    for i in range(0, len(listall)):
        dict1 = dict(zip(keys, listall[i]))
        list2.append(dict1)

    print(list2)


########################################################################################################################

options = {1: ipcheck, 2: mailcheck, 3: telephone, 4: numlines, 5: charfile, 6: wordsfile, 7: trailing, 8: endspace,
           9: duplicate, 10: dupchar, 11: duplist,13: fact1, 14: listofdict, 15: listofdict1, 16: prime, 17: classdemo,
           18: Datatypesdemo,19: squareroot, 20: printrangenumbers,21: listavg, 22: fib, 23: reversestring, 24: fileexists,
           25:transposematrix,26:listtoset,27:accesscsv,28:reversestr,29:maxvaluelist,30:findfile,32:generators_square}

print(Programs)



key = 'Y'

# ch=int(input('Enter the program Number :'))
while (key == 'Y') or (key == 'y') or (key == 'yes') or key == 'Yes' or key == 'YES':
    print("#####################################################\n")
    ch = int(input('Enter the program Number :'))
    print("\n")
    print("#####################################################\n")
    options[ch]()
    key = input('Do you want to continue : Press Y/Yes/y/yes or N/No/no/n : ')

if key == 'N' or key == 'n' or key == 'no' or key == 'NO' or key == 'No':
    os.system('exit')
