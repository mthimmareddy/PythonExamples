import pandas as pd
import numpy as np


Programs = '''
1.To Declare the pandas series and To basic operations with pandas,checking size and datatypes and to access the elements 
in series.
2.Series addtion operation demo
3.Creating a DataFrame by passing a numpy array, with a datetime index and labeled columns
and Viewing the data of dataframe
4.Selecting the dataframe by loc,iloc
5.Boolean indexing with dataframes
6.Handling the missing data in dataframe
7.apply and applymap on Series and df

8.Groupby in dataframes
9.read_csv into dataframe and read_excel into dataframe
'''


dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=list('ABCD'))


a=np.array([1,2,3,4,5,6,7,8,9])

df1=pd.DataFrame({'data':a,'even':a*2,'add3':a*3,'add4':a*4})

#print(df1)

#########################################################################################################3
##########################################################################################################33
def groupby():
    raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons',
                             'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
                'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd'],
                'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger',
                         'Riani', 'Ali'],
                'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
                'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
    df = pd.DataFrame(raw_data, columns=['regiment', 'company', 'name', 'preTestScore', 'postTestScore'])

    print(df.groupby('name').sum())

    print(df.groupby(['regiment', 'company']).mean())

    print(df.groupby(['regiment', 'company']).size())
    print(df.preTestScore.groupby(df.company).sum())
    #print ("Maximum",df['postTestScore'].groupby(df['categories']).apply(np.max()).unstack())
    print(df.preTestScore.groupby(df.company).describe())
    print(df.preTestScore.groupby(df.company).mean())
    print(df['preTestScore'].groupby([df['regiment'], df['company']]).mean())



#######################################################################################################################333
def csvexceloper():
    df.to_csv('foo.csv')

    df3=pd.read_csv("foo.csv")
    print(df3)
    '''
    #import openpyxl
    df.to_excel('foo.xlsx', sheet_name='Sheet1')

    df4=pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
    print(df4)
    '''

###############################################################################################################

def view_df():
    df = pd.DataFrame(np.random.rand(6, 4), index=[1, 2, 3, 4, 5, 6], columns=list('ABCD'))
    print(df)

    #head will print first 5 lines of df
    print("head will print first 5 lines of df",df.head())
    #tail last 5 rows of df
    print("tail last 5 rows of df",df.tail())
    #Describe shows a quick statistic summary of your data
    print("Describe shows a quick statistic summary of your data",df.describe())
    #Display the index, columns, and the underlying numpy data
    print("Display the index, columns, and the underlying numpy data",df.index)
    print("Display the index, columns, and the underlying numpy data",df.columns)
    #Display numpy data
    print("Display numpy data",df.values)
    #Transposing your data
    print("Transposing your data",df.T)

    #Sorting by an axis
    print("Sorting by an axis",df.sort_index(axis=1,ascending=False))
    #Sorting by values
    print("Sorting by an values",df.sort_values(by='B'))

##################################################################################################################

def selectdf():
    #While standard Python / Numpy expressions for selecting and setting are intuitive and come in handy for
    #interactive work, for production code, we recommend the optimized pandas data access methods, .at, .iat, .loc, .iloc and.ix.

    #Selecting a single column, which yields a Series, equivalent to df.A
    print("Selecting a single column, which yields a Series, equivalent to df.A",df['A'])
    #Selecting via [], which slices the rows.
    print("Selecting via [], which slices the rows.",df[0:3]) #selecting by index
    print("Selecting via [], which slices the rows.",df['2013-01-01':'2013-01-04'])

    print("############################################\nSHOWING BY LABEL\n#################################################\n")

    #Selection by label
    print ("Selection by label",df.loc[dates[0]])


    #Selecting on a multi-axis by label
    print("Selecting on a multi-axis by label",df.loc[:,['A','B']])
    print("Showing label slicing, both endpoints are included",df.loc['2013-01-01':'2013-01-03',['A','B']])
    print("Reduction in the dimensions of the returned object",df.loc['20130102',['A','B']])
    print("For getting a scalar value", df.loc[dates[0],'A'])
    print("For getting fast access to a scalar (equiv to the prior method)",df.at[dates[0],'A'])

    print("############################################\nSHOWING BY POSITION\n#################################################\n")

    print("Select via the position of the passed integers",df.iloc[3])
    print("By integer slices, acting similar to numpy/python",df.iloc[3:5,0:2])
    print("By lists of integer position locations, similar to the numpy/python style",df.iloc[[1,2,4],[0,2]])
    print("For slicing rows explicitly",df.iloc[0:3,:])
    print("For slicing columns explicitly",df.iloc[:,1:3])
    print("For getting a value explicitly",df.iloc[0,1])
    print("For getting fast access to a scalar (equiv to the prior method)",df.iat[0,1])

########################################################################################################################################
def boolean_index():
    print("Using a single column’s values to select data.",df[df.A>0])
    print("A where operation for getting.",df[df>0])
    print("########################\nUsing the isin() method for filtering\n###########################################")
    df2=df.copy()
    df2['E']=['one','two','three','four','five','six']
    print("isin operation",df2[df2['E'].isin(['two','six'])])

#######################################################################################################################################3
def missingdata():
    print("pandas primarily uses the value np.nan to represent missing data")

    print("#################################\nReindexing allows you to change/add/delete the index on a s"
          "pecified axisThis returns a copy of the data\n########")
    df1=df.reindex(index=dates[0:4],columns=list(df.columns + ['E']))
    df1.loc[dates[0]:dates[2],'E']=1
    print("Dataframe with Nan Values",df1)
    print("To drop any rows that have missing data.",df1.dropna(how='any'))
    print("Filling missing data",df1.fillna(value=5))
    print("To get the boolean mask where values are nan",df1.isnull())


#########################################################################################################################################3

#####################################################################################################################
def series_addtion():
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([20, 30, 40, 50], index=['a', 'b', 'c', 'd'])

    print(s1 + s2)

    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([20, 30, 40, 50], index=['b', 'd', 'a', 'c'])

    print(s1 + s2)

    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([20, 30, 40, 50], index=['c', 'd', 'e', 'f'])

    print(s1 + s2)

    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([20, 30, 40, 50], index=['e', 'f', 'g', 'h'])

    print(s1 + s2)

#################################################################################################################

def dec_Series():

    s=pd.Series([7,2,3,1,5,9],index=list('ABCDEF'))

    print(s)

    s1 = pd.Series([7, 2, 3, 1, 5, 9], index=list('ABCDEF'))

    countries = pd.Series(['Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
                           'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
                           'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
                           'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia'])

    life_expectancy_values = pd.Series([74.7, 75., 83.4, 57.6, 74.6, 75.4, 72.3, 81.5, 80.2,
                                        70.3, 72.1, 76.4, 68.1, 75.2, 69.8, 79.4, 70.8, 62.7,
                                        67.3, 70.6])
    #0,1,2,3 represents the column names

    df = pd.DataFrame({
        0: [11, 2, 30, 40],
        1: [50, 40, 90, 80],
        2: [90, 110, 100, 120],
        3: [130, 140, 150, 160]
    })
#other way od Dictinary

    df1=pd.DataFrame([[1,2,3,4],[3,6,9,12],[4,8,12,16]],index=['row1','row2','row3'],columns=['A','B','C','D'])

    df1.apply(np.sum,axis=0)
    df1.apply(np.sum,axis=1)
    print(df1)

    print(countries)
    print(life_expectancy_values)

   #print shape of series
    print(s.shape)
    print(s[s>3]) #prints the elements greater than 3
    print(s>3) #Generates the boolen series

    #Vectorized operations on series
    print(s.add(2))
    print(s.sub(2))
    print(s.mul(2))
    print(s.div(2))
   #other way of oerations

    print(s+5)
    print(s-5)
    print(s*5)
    print(s/5)

    #Accessing the elements of series

    print(s[0])
    print(s.loc['C'])
    print(s.iloc[0:3]) #print range of values
    print(s[0:4])

##########################################################################################################3

    #apply  method on Series on series
def squares(x):
    return(x*x)

    #print("Squares of Series are {0}".format(s.apply(squares)))
    '''
    df = pd.DataFrame({
        0: [11, 2, 30, 40],
        1: [50, 40, 90, 80],
        2: [90, 110, 100, 120],
        3: [130, 140, 150, 160]
    })

    df1 = pd.DataFrame([[1, 2, 3, 4], [3, 6, 9, 12], [4, 8, 12, 16]], index=['row1', 'row2', 'row3'],
                       columns=['A', 'B', 'C', 'D'])'''
################################################################################################################33
#Apply function on DataFrame acts on every column
def sec_large(s):
    s.sort_values(axis=0,ascending=False,inplace='True')
    return s.iloc[1]
############################################################################################################33
    #sec_large(s1)
def apply_applymap():
    s = pd.Series([7, 2, 3, 1, 5, 9], index=list('ABCDEF'))

    df = pd.DataFrame({
        0: [11, 2, 30, 40],
        1: [50, 40, 90, 80],
        2: [90, 110, 100, 120],
        3: [130, 140, 150, 160]
    })

    print("Squares of Series are {0}".format(s.apply(squares)))

    df1 = pd.DataFrame([[1, 2, 3, 4], [3, 6, 9, 12], [4, 8, 12, 16]], index=['row1', 'row2', 'row3'],
                       columns=['A', 'B', 'C', 'D'])

    df1.apply(np.sum, axis=0)
    df1.apply(np.sum, axis=1)
    print(df1)

    print("Second largest element is {0}".format(df.apply(sec_large,axis=0)))

    #applymap on the dataframe acts on all elements of dataframe

    print("Squares of the dataframe",df.applymap(squares))

##############################################################################################3


options = {1:dec_Series,2:series_addtion,3:view_df,4:selectdf,5:boolean_index,6:missingdata,7:apply_applymap,8:groupby,9:csvexceloper}

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
