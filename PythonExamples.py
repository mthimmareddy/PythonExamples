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
21.Given a list,find the avg of list if all the elements present else break
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
32.Reading the csv 
33.Given list of elements find the largest,second largest and smallest element
34.Given matrix,find second largest along all columns
35.Given a list of strings, return the count of the number of strings where the string length is 2 or more and
 the first and last chars of the string are the same.
Note: python does not have a ++ operator, but += works.
36.String sorting
37.Given a list of strings, return a list with the strings in sorted order, except group all the strings that begin with 'x' first.
38.Sorting a list of numbers
39.C. sort_last,Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
40.Given a string s, return a string made of the first 2 and the last 2 chars of the original string, so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
41.Given a string s, return a string where all occurences of its first char have been changed to '*', except do not change the first char itself.
# e.g. 'babble' yields 'ba**le'
42.Given strings a and b, return a single string with a and b separated by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.'mix', pod' -> 'pox mid' 'dog', 'dinner' -> 'dig donner' Assume a and b are length 2 or more.
43.Given 2 sorted list, merge into single sorted list
44.D. Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
45.Consider dividing a string into two halves.If the length is even, the front and back halves are the same length.
If the length is odd, we'll say that the extra char goes in the front half. e.g. 'abcde', the front half is 'abc', the back half 'de'. Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
46.Given a string, find the first appearance of the substring 'not' and 'bad'. If the 'bad' follows the 'not', replace the whole 'not'...'bad' substring
# with 'good'.Return the resulting string.So 'This dinner is not that bad!' yields:This dinner is good!
47.Given a string, if its length is at least 3,add 'ing' to its end.Unless it already ends in 'ing', in which case add 'ly' instead. If the string length is less than 3, leave it unchanged.
Return the resulting string.
48.Remove the duplicates in list
49.Fibonacci series with recursion
50.Usage of lamda,map,zip,all,any and filter,pass
Builtin keywords
-------------------
lamda expressions
Zip 
map
filter
any and all
pass
51.Sorting using quick sort
52.Reverse the list 
53.Merge sort
54.Web Scarping in python
55.CSV reading in python without module and with module
56.Excel reading in python
57.Difference b/w iteritem amd items
58.linearsearch on list

Unit testframework on python #refer sepearate program testframework.py


54.Collections and use
binary search
55.Exceptions is python
56.Collections in python
57.classes and inheritance
58.Direcoty traversersal,cleans the computer,cpu,memory
59.Generators
60.Argparser in python demo



Introduction to data structures
My code school

Intro to algorithms
MIT open course

Practice on HackerEarth.com,hackerRank.com

Python related questions ask interview


'''


###########################################################################################
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
                flag += 1
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
        flag = 0
        match = re.match(pattern, input_mail)
        if (match):
            list1 = input_mail.split(".")
            print(list1)
            if (3 >= len(list1) > 1):
                flag = 1
            else:
                flag = 0
        if (flag == 1):
            print("Match found")
        else:
            print("Not a valid mail id")

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

###########################################################################################
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


###########################################################################################################3

def duplist():
    print("To find duplicates in list")
    list1 = [1, 2, 3, 4, 5, 2, 6, 7, 8, 4]
    count = {}
    for num in list1:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    print(count)

    for i in count:
        if (count[i] > 1):
            print("The {0} has occured {1} times".format(i, count[i]))

    # Other way using the bubble sort method
    k = 1
    for i in range(0, len(list1) - 1):
        for j in range(k, len(list1)):

            if (list1[i] == list1[j]):
                print("Duplicate found:", list1[i])
                # continue
        k += 1


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

    # Transpose of listall is mat2
    mat2 = []
    for col in range(0, len(listall[0])):
        mat1 = []
        for row in range(0, len(listall)):
            mat1.append(listall[row][col])
        mat2.append(mat1)
    print('Matrix after transpose', mat2)

    # Dictionay of lists
    for i in range(0, len(keys)):
        d[keys[i]] = mat2[i]
    print(d)

    # list of dictionaries

    list1 = []

    for i in range(0, len(listall)):
        d1 = {}
        for j in range(0, len(listall[0])):
            d1[keys[j]] = listall[i][j]
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
##########################################################################################

def prime():
    # 12.Given list ,prime numbers with generators and witout generators

    list1 = [2, 3, 2, 34, 23, 17, 11, 56, 25, 44, 99, 7]

    # Using the list comphrensions

    prime1 = [x for x in list1 if all(x % y != 0 for y in range(2, x))]
    print("Prime numbers {0}".format(prime1))

    # Withouut using comprehensions
    for i in list1:
        if (i == 3) or i == 5 or i == 2:
            print("{0} Prime number".format(i))
            continue
        if (i % 2 == 0 or i % 3 == 0 or i % 5 == 0):
            print("{0} Not prime".format(i))
        else:
            print("{0} is Prime".format(i))

            # other way of doing
    list2 = []
    for i in range(1, 100):
        flag = 0
        for j in range(2, i):
            if (i % j) == 0:
                flag = 1
                continue
        if (flag == 0):
            list1.append(i)
    print("{0} Prime number list".format(list1))


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
#################################################################################################


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
    list2 = [1, 2, 3, 4, 5]
    count = int(input('Enter the number of items you want in list:'))
    list1 = []
    cnt = 0
    for i in range(0, count):
        i = int(input('Enter the number :'))
        list1.append(i)

    for i in list1:
        for j in list2:
            if i == j:
                cnt = cnt + 1
        if (cnt == 0):
            break

    sum1 = 0
    if (cnt == count):
        for i in list1:
            sum1 = sum1 + i
        print('Average of list items is:', (sum1 / cnt))
    else:
        print("All the given elemnts not present in original list")
 #############################################################################################################

def fib(n):
    x = 0
    y = 1
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    if n > 1:
        print(fib(n - 1), fib(n - 2))
        return (fib(n - 1) + fib(n - 2))
    print('Fibonaci series', fib(4))





############################################################################################

def fileexists():
    # 13.File exists

    if os.path.isfile("text.txt"):
        print("File Exists")
    else:
        print("Not a file")

###############################################################################################

def transposematrix():
    matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print('Matrix before transpose', matrix1)
    mat2 = []
    for col in range(0, len(matrix1[0])):
            mat1 = []
            for row in range(0, len(matrix1)):
                mat1.append(matrix1[row][col])
            mat2.append(mat1)
    print('Matrix after transpose', mat2)

    mat4 = [[matrix1[row][col] for row in range(0, len(matrix1))] for col in range(0, len(matrix1[0]))]
    print(mat4)


##############################################################################################
def listtoset():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

    s = set(list1)
    print(s)



#####################################################################################################################
import unicodecsv


def accesscsv():
    print("CSV reading")
    datacsv = [{'firstnam': 'manju', 'sirname': 'thimmareddy', 'hobby': 'writing', 'age': '29'},
               {'firstnam': 'rishi', 'sirname': 'shereddy', 'hobby': 'dancing', 'age': '3'},
               {'firstnam': 'ravi', 'sirname': 'chandra', 'hobby': 'reading', 'age': '33'}]

    # Accessing without module

    for ele in datacsv:
        for word in ele:
            print(word, ele[word])

#####################################################################################################

def reversestr():
            string1 = "manju"
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

#######################################################################################################

def maxvaluelist():
    employment = [23.4, 67.0, 56.7, 23.0, 56.8, 65.6, 76.7, 34.4, 45.6]
    max_value = 0
    index = 0
    for value in range(len(employment)):
        # print("ths country {0} has {1} employmentrate".format(countries[value],employment[value]))
        if (employment[value] > max_value):
            max_value = employment[value]
            index = value
    print("Maximum employment value is {0} has index : {1} ".format(max_value, index))
###########################################################################################################
import os.path
import os


def findfile():
    # path1=os.getcwd()
    search_file = input('Enter the file name:')

    # path1=input('Enter the path u want to search')
    # find(path1)
    # flag=0

    def find(path1):
        flag = 0
        pathname = path1
        dirlist = os.listdir(path1)
        # print (dirlist)
        for file1 in dirlist:
            if file1 == search_file:
                flag = 1
                break
        for file1 in dirlist:
            if os.path.isdir(file1) and flag == 0:
                find(os.path.join(path1, file1))

        if (flag == 1):
            print("File Found in current directory {0}".format(path1))
        else:
            print("File not Found in current directory {0}".format(path1))

        find('C:\\Users')

####################################################################################################################333
def read_csv(filename):
        list1 = []
        with open(filename, 'r') as f:
            reader = unicodecsv.DictReader(f)
            for row in reader:
                list1.append(row)
                # list1=list(reader)
        print(list1)
#############################################################################################
def generators_square():
        # list1 = []
        def square():
            for x in range(1, 100):
                yield (x * x)  # keeps the eleemnt one at time hence performance is much better
                # list1.append(x*x)
                # print(list1)

        numlist1 = [x * x for x in range(1, 25)]  # list comprehension
        numlist2 = (x * x for x in range(25, 50))  # using Generators
        list2 = list(numlist2)  # convert generators to list
        print(list2)
        print(numlist2)  # you cant access eleemnts all at time
        # numlist=square()
        # print(numlist1)

        for num in numlist2:  # Generators ar accessed this way
            print(num)

        list2 = [x for x in range(1, 100) if all(x % j != 0 for j in range(2, x))]
        print("Prime numbers list from 1-100", list2)

        list2 = [x for x in range(1, 100) if x % 3 == 0]
        print("Multiple of 3", list2)

##################################################################################################
def seclarmatrix():
    list1 = [[8, 2, 3], [3, 4, 5], [6, 7, 8], [56, 67, 78], [23, 34, 12], [1, 11, 23]]

    final = []
    for col in range(0, len(list1[0])):
        tran = []
        for row in range(0, len(list1)):
            tran.append(list1[row][col])
        final.append(tran)
    print(final)

    for i in range(0, len(list1[0])):
        list3 = sorted(final[i])
        print("Second largets in {0} column  is {1}".format(i, list3[len(list3) - 2]))

#######################################################################################################

def stringlen():
        list1 = ['hello', 'anja', 'manjum', 'rishi', 'ravi', 'runr']
        print(sorted(list1))
        cnt = 0
        cnt1 = 0
        for i in list1:
            if len(i) > 2:
                cnt = cnt + 1
                # print(cnt)
                if (i[0] == i[len(i) - 1]):
                    cnt1 = cnt1 + 1
        print(
            "{0} list items have length greater that \"two\" and {1} have first and last character same".format(cnt,
                                                                                                                cnt1))


############################################################################################

def sortstirng():
    s = "Bobble bolly"
    s1 = 'BALL'
    print(s1.lower().upper())
    c = ''.join(sorted(set(s)))  # sorts the string and keeps them distint
    print(c)
    c1 = ''.join(sorted(s))  # sorts and keep duplicates
    print(c1)
    print(''.join(sorted(set(s.lower()))).strip())  # to get rid of begining and end spaces



#############################################################################################

def stringmatch():
    list1 = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
    list2 = []
    list3 = []
    for i in list1:
        if i[0] == 'x' or i[0] == 'X':
            list2.append(i)
        else:
            list3.append(i)
    # print()
    print(list2 + sorted(list3))

################################################################################################


def bubblesort():
    list1 = [15, 14, 3, 2, 1, 8, 9, 1, 4, 6, 19, 21, 13, 14, 16]

    for i in range(0, len(list1) - 1):
        for j in range(i + 1, len(list1)):
            if (list1[i] > list1[j]):
                tmp = list1[j]
                list1[j] = list1[i]
                list1[i] = tmp
    print(list1)

#######################################################################################################################
def tuplesort():
    list1 = [(1, 7), (1, 3), (3, 4, 5), (2, 2), (4, 5, 6), (1, 2, 3), (3, 5, 7)]

    for i in range(0, len(list1) - 1):
        for j in range(i + 1, len(list1)):
            if (list1[i][len(list1[i]) - 1] > list1[j][len(list1[j]) - 1]):
                tmp = list1[j]
                list1[j] = list1[i]
                list1[i] = tmp
    print(list1)


##############################################################################################
def both_ends():
    # +++your code here+++
    s = "manjuisawesome"
    s1 = ''
    if (len(s) <= 2):
        print(' ')
    else:
        s1 = ''.join(s[0])
        s1 += ''.join(s[1])
        s1 += ''.join(s[len(s) - 2])
        s1 += ''.join(s[len(s) - 1])
        print(s1)
        # return s1'''

##################################################################################################

def fix_start():
    # +++your code here+++
    s = "rishiissmart"
    s1 = list(s)  # string has to converted to list for character teplacement
    count = {}
    print(s.count('r'))  # inbuilt function to count charachter occurances in string
    print(s.rstrip())
    print(s.lstrip())
    print(s.strip())

    # tmp=s[0]
    # s1[0]='M'

    for ch in range(0, len(s1)):
        if s1[ch] not in count:
            count[s1[ch]] = 1
        else:
            count[s1[ch]] = count[s1[ch]] + 1
            # print(s[ch])
            s1[ch] = '*'
    s = ''.join(s1)
    print(s)


################################################################################################
def mix_up():
    a = input('Enter string 1')
    b = input('Enter second string')
    s1 = list(a)
    s2 = list(b)
    tmp1 = s1[0]
    tmp2 = s1[1]
    s1[0] = s2[0]
    s1[1] = s2[1]
    s2[0] = tmp1
    s2[1] = tmp2
    a = ''.join(s1)
    print(a)
    b = ''.join(s2)
    # print(b)
    print(a + " " + b)
    # print(a)

#####################################################################################################


def list_merge():
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [4, 5, 6, 7, 8, 9]
    # print(list1.append(list2)) #append complete list inside list
    list1.extend(list2)  # Extend will add eleemnt at end of list,end is  1D list

    print(list1)
    print(sorted(list1))

    # print(sorted(list1+list2))


#################################################################################################
def conseqdup():
    list1 = [1, 2, 2, 3, 4, 5, 5, 6, 7, 2, 3, 5]
    list2 = []
    for i in range(0, len(list1) - 1):
        j = i + 1
        if (list1[i] == list1[j]):
            continue
        else:
            list2.append(list1[i])
    print(list2)


#####################################################################################################
def front_back():
    # +++your code here+++
    a = input('Enetr the string1 :')
    # b=input('Enter the string2 :')
    afront = ""
    aback = ""
    if (len(a) % 2 == 0):
        lena1 = len(a) / 2
        for i in range(0, int(len(a) / 2)):
            afront += a[i]
        for i in range(int((len(a) / 2)), int(len(a))):
            aback += ''.join(a[i])
    else:
        for i in range(0, int(len(a) / 2) + 1):
            afront += ''.join(a[i])
        for i in range(int(len(a) / 2) + 1, int(len(a))):
            aback += ''.join(a[i])
    print(afront, aback)

    return


###############################################################################################

def not_bad():
    # +++your code here+++
    # refer string.find()
    s = input('Enter the string:')
    s1 = ""
    pat = r"not(\s|\w)+bad"
    re.search(pat, s)
    if (re.search(pat, s)):
        s1 = re.sub(pat, "good", s)
    print(s1)



###################################################################################################

def verbing():
    s = input('Enter the String')
    if (len(s) > 3 and s[len(s) - 3:len(s)] != 'ing'):
        s += ''.join('ing')
        print(s)
    elif (len(s) > 3) and s[len(s) - 3:len(s)] == 'ing':
        s += ''.join('ly')
        print(s)
    elif (len(s) < 3):
        print('String length less than 3 characters')
        # +++your code here+++


###############################################################################################

def rem_dup():
    list1 = [1, 2, 3, 3, 3, 4, 5, 5, 1, 2, 1, 1, 1, 3, 3, 3, 4, 5, 5, 1, 2]
    list2 = []
    count = {}

    for i in range(0, len(list1)):
        if list1[i] not in count:
            count[list1[i]] = 1
            list2.append(list1[i])
        else:
            count[list1[i]] += 1
            # del list1[i]
    print(list2)



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

###################################################################################################
def special_builtin():
        from functools import reduce

        # The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.
        # The pass statement is a null operation; nothing happens when it executes.

        def passdemo():
            pass

        passdemo()
        list1 = [1, 2, 3]
        list2 = [2, 3, 4]
        list3 = [1, 2, 4]
        list4 = [3, 4, 5]

        # lambda is fuction used to create the anynymous fuction without actully creating it,ie it not bound to name
        # at runtime ,it integrated with filter ,map,reduce
        g = lambda x: x * 2

        print("Using the lambda", g(5))

        # The map(aFunction, aSequence) function applies a passed-in function to each item in an
        # iterable object and returns a list containing all the function call results.

        list2 = list(map(lambda x: x ** 2, list1))
        print("List of items with squares using map and lamda", list2)

        def squares(x):
            return (x * x)

        print("List of items with squares using map", list(map(squares, list1)))

        # The built-in filter() function operates on any iterable type (list, tuple, string, etc).
        # It takes a function and an iterable as arguments. filter() will invoke the function on each element of the iterable,
        # and return a new iterable composed of only those elements for which the function returned True.
        print("Filter on true return using Filter", list(filter(lambda x: x % 2 == 0, list1)))

        # Reduce is a really useful function for performing some computation on a list and returning the result integerr.
        # For example, if you wanted to compute the product of a list of integers.
        sum1 = reduce((lambda x, y: x + y), [1, 2, 3, 30])
        print("Sum of list using reduce", sum1)

        product = reduce((lambda x, y: x * y), [1, 2, 3, 30])
        print("Product using the reduce", product)

        # Zip function to traverse 2 list items at time

        list1 = [1, 2, 3]
        list2 = [2, 3, 4]
        for a, b in zip(list1, list2):
            print("items of 2 list", a, b)

        list3 = [list1, list2]
        print(list3)
        print(list(zip(*list3)))  # to transpose the list use zip(*values)

        # print(listb)
        print("sum of lists", reduce(lambda x, y: x + y, list1))

        '''You can roughly think of any and all as series of logical or and and operators, respectively.
        any will return True when atleast one of the elements is Truthy. Read about Truth Value Testing.
        all will return True only when all the elements are Truthy.
        '''
        list2 = [x for x in range(1, 100) if all(x % j != 0 for j in range(2, x))]
        print("Prime numbers list from 1-100", list2)
##############################################################################################3

def quicksort():
        array1 = [12, 4, 5, 6, 7, 3, 1, 15]

        def sort(array):
            less = []
            equal = []
            greater = []

            if len(array) > 1:
                pivot = array[0]
                for x in array:
                    if x < pivot:
                        less.append(x)
                    if x == pivot:
                        equal.append(x)
                    if x > pivot:
                        greater.append(x)

                print(less, equal, greater)
                # Don't forget to return something!
                return sort(less) + equal + sort(greater)  # Just use the + operator to join lists
            # Note that you want equal ^^^^^ not pivot
            else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
                return array

        print(sort(array1))
####################################################################################################
def rev_list():
    array1 = [12, 4, 5, 6, 7, 3, 1, 15]

    print("Reverse of list without any function", array1[::-1])
    print("Reverse of list using builtin reversed", list(reversed(array1)))


###############################################################################################
def msort(x):
    result = []
    if len(x) < 20:
        return sorted(x)
    mid = int(len(x) / 2)
    y = msort(x[:mid])
    z = msort(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    print("Sorted array using merge sort", result)



#############################################################################################################3
def webscrape():
    from bs4 import BeautifulSoup as soup
    from urllib.request import urlopen

    url = "https://www.amazon.com/b/ref=s9_acss_bw_tt_x_sgui_shoul_w?node=16313235011&lo=fashion&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=T6GD9F4805AHQVWZXP88&pf_rd_t=101&pf_rd_p=d847fc3d-f4c2-402b-b544-738f8def323e&pf_rd_i=1045024"

    uclient = urlopen(url)
    page_html = uclient.read()

    uclient.close()
    # soup is created, all the html content is stored in the soup
    page_soup = soup(page_html, "html.parser")

    # We can now print out the HTML content of the page, formatted nicely, using the prettify method on the BeautifulSoup object:
    print(page_soup.prettify())

    # print(page_soup.div)
    container = page_soup.findAll('div', attrs={'class': "name"})
    print(container[0])


################################################################################################################
def csvread():
    print("################Without using modules########################3")
    keys = []

    with open("test.csv", 'r') as f:
        keys = f.readline().strip().split(',')
        print(keys)
        for line in f:
            print(line.strip().split(','))


    import csv
    print("################Using csv modules########################3")
    with open("test.csv", 'r', newline='') as f:
     read = csv.reader(f)
     header = next(read)  # extract the header in csv

     for line in read:
        print(line)

###################################################################################3############3
def dicitems():
         dict1 = {'one': 1, 'two': 2, 'three': 3}

         for k, v in dict1.items():
             print("key and vales are", k, v)

         for k in dict1.keys():
             print("keys are", k)

         for v in dict1.values():
             print("Values are:", v)

         '''
         As you are in python3 , use dict.items() instead of dict.iteritems()
         iteritems() was removed in python3, so you can't use this method anymore.
         Take a look at Python Wiki (Link)
         In Built-in Changes part, it is stated that
         Removed dict.iteritems(), dict.iterkeys(), and dict.itervalues().
         Instead: use dict.items(), dict.keys(), and dict.values() respectively.
         '''

         # for k,v in dict1.iteritems(): throws an error as its removed in python 3


################################################################################################################3
def linearsearch():
  list1=[2,3,4,5,6,7,81,2,3,41]

  num=int(input('enter the number to be searched:'))

  for i in range(0,len(list1)):
      if(num==i):
          flag=1
          #print("Found")
          break
      else:
          flag=0
  if(flag==1):
      print("Found")
  else:
      print("Not found")

#################################################################################################	  
def argparserdemo():

   parser=argparse.ArgumentParser()
      
    
    parser.add_argument("Search_criteria",help="Specify the what based Search")
    parser.add_argument("pattern",help="search pattern")
    parser.add_argument("-o","--out",help="search option specific")
    args=parser.parse_args()
    
    print(args.Search_criteria)
    print(args.pattern)
     
    if int(args.Search_criteria)==1:
        result=searchbasedonfilename(args.pattern,sys.argv[3])
    elif int(args.Search_criteria)==2:
        result=searchbasedonfilecontent(args.pattern)
    elif int(args.Search_criteria)==3:
        result=searchbasedondate(args.pattern)
    elif int(args.Search_criteria)==4:
        result=searchbasedonsize(args.pattern)
    elif int(args.Search_criteria)==5:
        result=searchbasedontypeoffile(args.pattern)
    else:
        print("Search criteria range from 1-5")
		
####################################################################################################33






########################################################################################################################

options = {1: ipcheck, 2: mailcheck, 3: telephone, 4: numlines, 5: charfile, 6: wordsfile, 7: trailing, 8: endspace,
           9: duplicate, 10: dupchar, 11: duplist, 13: fact1, 14: listofdict, 15: listofdict1, 16: prime, 17: classdemo,
           18: Datatypesdemo, 19: squareroot, 20: printrangenumbers, 21: listavg, 22: fib, 23: reversestring,
           24: fileexists,25: transposematrix, 26: listtoset, 27: accesscsv, 28: reversestr, 29: maxvaluelist, 30: findfile,31:read_csv,
           32: generators_square,34: seclarmatrix, 35: stringlen, 36: sortstirng, 37: stringmatch, 38: bubblesort, 39: tuplesort,
           40: both_ends, 41: fix_start,42: mix_up, 43: list_merge, 44: conseqdup, 45: front_back, 46: not_bad, 47: verbing, 48: rem_dup,
           49: fib,50: special_builtin,51: quicksort, 52: rev_list,53:msort,54:webscrape,55:csvread,57:dicitems,58:linearsearch,60:argparserdemo
           }

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
