import numpy as np


Programs = '''
ndarray.ndim
the number of axes (dimensions) of the array. In the Python world, the number of dimensions is referred to as rank.
ndarray.shape
the dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension. For a matrix with 
n rows and m columns, shape will be (n,m). The length of the shape tuple is therefore the rank, or number of dimensions, ndim.
ndarray.size
the total number of elements of the array. This is equal to the product of the elements of shape.
ndarray.dtype
an object describing the type of the elements in the array. One can create or specify dtype’s using standard Python types. 
Additionally NumPy provides types of its own. numpy.int32, numpy.int16, and numpy.float64 are some examples.
ndarray.itemsize
the size in bytes of each element of the array. For example, an array of elements of type float64 has itemsize 8 (=64/8),
 while one of type complex32 has itemsize 4 (=32/8). It is equivalent to ndarray.dtype.itemsize.
ndarray.data
the buffer containing the actual elements of the array. Normally, we won’t need to use this attribute because we will access 
the elements in an array using indexing facilities.


1.Numpy Declarations
2.Basic Operations
3.Builtin functions in numpy
4.Accessing the numpy array
5.Load data from text files in numpy
Data = np.loadtxt(filename,dtype='string',usecols=(1,2),delimiter="\t")

'''

print('Programs')

#############################################################################################
#############################################################################################
employment = np.array([
    55.70000076, 51.40000153, 50.5, 75.69999695,
    58.40000153, 40.09999847, 61.5, 57.09999847,
    60.90000153, 66.59999847, 60.40000153, 68.09999847,
    66.90000153, 53.40000153, 48.59999847, 56.79999924,
    71.59999847, 58.40000153, 70.40000153, 41.20000076
])

ridership = np.array([
    [0, 0, 2, 5, 0],
    [1478, 3877, 3674, 2328, 2539],
    [1613, 4088, 3991, 6461, 2691],
    [1560, 3392, 3826, 4787, 2613],
    [1608, 4802, 3932, 4477, 2705],
    [1576, 3933, 3909, 4979, 2685],
    [95, 229, 255, 496, 201],
    [2, 0, 1, 27, 0],
    [1438, 3785, 3589, 4174, 2215],
    [1342, 4043, 4009, 4665, 3033]
])
###################################################################################################
def loaddata():
    Data = np.loadtxt("text2.txt", delimiter="\t" ,dtype=int ,unpack=True)
    print(Data)

######################################################################################################33
def numpy_dec():
# Subway ridership for 5 stations on 10 different days343q

 a=np.arange(15).reshape(3,5)
 print(a)
 print("Shape:{0},dimention:{1},datatype:{2},itemsize:{3},size:{4},type:{5}",
 print(a.shape,a.ndim,a.dtype.name,a.itemsize,a.size,type(a)))

 b=np.random.rand(3,2) #Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).
 print(b)

a1 = np.arange(6)
a2=np.arange(15).reshape(5,3)
a3=np.arange(24).reshape(2,3,4)

print(a1,a2,a3)

################################################################################################################33
def basic_operations():
#Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result.
 a=np.array([4,5,6,7])
 b=np.arange(4)
 c=a-b
 print(c)
 print(b**2) #square of each elements
 print(10*np.sin(a))
 print(a<3) #return the boolen np array

#Matrix multiplication by dot opearator
 A=np.array([[1,1],[2,3]])
 B=np.array([[1,0],[5,6]])
 C1=A.add(B) #adding the eleement
 C2=np.add(A,B)
 C=A*B   #Elementwise product
 D=A.dot(B) #Matrix product
 E=np.dot(A,B)  #other way of matrix product
 print(np.sqrt(A))
 print(np.exp(A))

#Other basic operations as sum,min,max,mean

 a=np.array([1,2,3,4,5,6,7])
 print(a.sum())#sum of all elements
 print(a.min()) #minimum element
 print(a.max())
 print(a.mean())
 print(a.argmax()) #returns the index of maximum element
 print(a.argmin())

#Other useful builtin fuctions
#all, any, apply_along_axis, argmax, argmin, argsort, average, bincount, ceil, clip, conj, corrcoef, cov, cross, cumprod, cumsum,
# diff, dot, floor, inner, inv, lexsort, max, maximum, mean, median, min, minimum,
#  nonzero, outer, prod, re, round, sort, std, sum, trace, transpose, var, vdot, vectorize, where


##########################################################################################################




#i Dimenstional numpy array
 countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
 ])


# Employment data in 2007 for those 20 countries
 employment = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
 ])
#2Dimentional numpy array
 ridership = np.array([
    [0, 0, 2, 5, 0],
    [1478, 3877, 3674, 2328, 2539],
    [1613, 4088, 3991, 6461, 2691],
    [1560, 3392, 3826, 4787, 2613],
    [1608, 4802, 3932, 4477, 2705],
    [1576, 3933, 3909, 4979, 2685],
    [95, 229, 255, 496, 201],
    [2, 0, 1, 27, 0],
    [1438, 3785, 3589, 4174, 2215],
    [1342, 4043, 4009, 4665, 3033]
 ])

 print(countries)

 print(employment[2])
#####################################################################################################################
def access_numpy():

    #1 Diementional arrays accessed asa lists
    print(employment)
    print(employment[0])

    #Accessing the 2-D numpy array
    print(ridership[:,:])#all rows,all columns
    print(ridership[:,2])#all rows 2 column
    print(ridership[:,1:4])#all rows 1 to 3 columns
    print(ridership[1:3,:])#1 to 2 rows, all columns


#####################################################################################################################3
def numpy_builtin():
    print("{0} station has maximum riders on day1 with {1}".format(ridership[0, :].argmax(), ridership[0, :].max()))
    # print (ridership[0,:].max())

    print(ridership[:, 3].mean())

    # Mean ridership per day for all stations
    # return maximum and minimum ridership per day among all staions
    print(ridership.mean(axis=0))  # to get the mean along columns
    print(ridership.mean(axis=1))  # to get mean along rows
    print(ridership.argmax(axis=1))
    print(ridership.argmax(axis=0))

    print(ridership.mean(axis=0).max())
    print(ridership.mean(axis=0).min())


###################################################################################################3

options = {1:numpy_dec,2:basic_operations,3:numpy_builtin,4:access_numpy,5:loaddata}

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
