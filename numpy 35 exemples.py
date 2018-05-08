import numpy as np

#Ex1
#Print the version of Numpy
print("Print the version of Numpy :")
print(np.__version__)
#>1.14.3

#Ex2
#Create an array of dimension 1 from 0 to 9
print("Create an array of dimension 1 from 0 to 9 :")
arr = np.arange(10)
print(arr)
#>[0 1 2 3 4 5 6 7 8 9]

#Ex3
#Create an array of bool of size 3*3
print("Create a array of bool of size 3*3 :")
#Method 1
print("    Method 1:")
arr = np.full((3, 3), True,dtype = bool)
print(arr)
#>[[ True  True  True]
#  [ True  True  True]
#  [ True  True  True]]
#Method 2
print("    Method 2:")
np.ones((3,3),dtype = bool)
print(arr)
#>[[ True  True  True]
#  [ True  True  True]
#  [ True  True  True]]

#Ex4
#Filtre of an array
print("Filtre of an array :")
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr=arr[arr % 2 == 1]
print(arr)
#>[1 3 5 7 9]

#Ex5
#Change some elements in the array and hold the position
print("Change the elements in the array and hold the position")
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr % 2 == 1] = -1
print(arr)

#Ex6
#Change some elements in the array and return a new one
print("Change some elements in the array and return a new one :")
arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print(out)
#What is «where»
#When the condition is ture, return the first value
#Here is -1, else retrun the second value
#Here is the oringinal value
#like map(lambda f:x if bln else y,List)

#Ex7
#Change the size of array
print("Change the size of array")
arr = np.arange(10)
arr=arr.reshape(2,-1) #-1 means calculate automaticly the dimension, it's a fonction not procedure
print(arr)

#Ex8
#Combine the array in colomn direction
print("Combine the array in colomn direction :")
a = np.arange(10).reshape(2,-1)
b = np.repeat(1,10) #repeat 1 10 times
b = b.reshape(2,-1)
#Method 1
print("    Method 1 :")
print(np.concatenate([a, b], axis=0))#extend an array
#Method 2
print("    Method 2 :")
print(np.vstack([a,b])) #Split array into a list of multiple sub-arrays vertically.
#Method 3
print("    Method 3 :")
print(np.r_[a ,b]) #joint 2 arrays in row direction
#>[[0 1 2 3 4]
#  [5 6 7 8 9]
#  [1 1 1 1 1]
#  [1 1 1 1 1]]

#Ex9
#Combine the array in row direction
a = np.arange(10).reshape(2,-1)
b = np.repeat(1,10).reshape(2,-1)
#Method 1
print("    Method 1 :")
print(np.concatenate([a,b],axis=1))
#Method 2
print("    Method 2 :")
print(np.hstack([a,b]))
#Method 3
print("    Method 3 :")
print(np.c_[a,b])
#>[[0 1 2 3 4 1 1 1 1 1]
#  [5 6 7 8 9 1 1 1 1 1]]

#Ex10
#Create a new array without hard coding
a = np.array([1,2,3])
#Hard coding version
b = np.array([1,1,1,2,2,2,3,3,3,1,2,3,1,2,3,1,2,3])
print("Create a new array without hard coding :")
print("From\n",a)
print("to\n",b,"\n")
#Without hard coding
print(np.r_[np.repeat(a,3),np.tile(a,3)])

#Ex11
#Return the intersection
print("Return the intersection :")
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,8])
print(np.intersect1d(a,b))

#Ex12
#Delete all the elements from b
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
print("Delete all the elements from b :")
print(np.setdiff1d(a,b))

#Ex13
#Get the indexes of the same elements from a and b
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.where(a == b))

#Ex14
a = np.arange(15)
#Method 1
index = np.where((a>=5) & (a<=10))
print(index)
print(a[index])
#Method 2
index = np.where(np.logical_and(a>=5,a<=10))
print(index)
print(a[index])
#Method 3
print(a[(a >= 5) & (a<=10)])

#Ex15
#Return the bigger one between 2 arrrays
a = np.array([5,7,9,8,6,4,5])
b = np.array([6,3,4,8,9,7,1])
maxx = lambda x,y:x if x>=y else y
pair_max = np.vectorize(maxx,otypes = [int])
print(pair_max(a,b))

#Ex16
#Exchange the first column and second column
arr = np.arange(9).reshape(3,3)
print(arr)
print(arr[:,[1,0,2]])

#Ex17
#Exchange the first row and second row
arr = np.arange(9).reshape(3,3)
print(arr[[1,0,2],:])

#Ex18
#Reverse the array by rows
arr = np.arange(9).reshape(3,3)
print(arr[::-1])

#Ex19
#Reverse the array by column
arr = np.arange(9).reshape(3,3)
print(arr[:,::-1])

#Ex20
#Create an array of size 5*3
#Method 1
rand_arr = np.random.randint(low = 5, high = 10, size = (5,3))+np.random.random((5,3))
print(rand_arr)
#Method 2
rand_arr = np.random.uniform(5,10,size=(5,3))
print(rand_arr)

#Ex21
#Print with 3 decimal places
np.set_printoptions(precision = 3)
print(rand_arr[:4])

#Ex22
#Print without scientific notation
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
np.set_printoptions(suppress=True, precision=6)
print(rand_arr)

#Ex23
#Print at most 6 numbers in an array
a = np.arange(15)
np.set_printoptions(threshold=6)
print(a)

#Ex24
#Get iris numbers
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter = ',',dtype="object")
print(iris[:3])

#Ex25
#Make the range of the array from 0 to 1
sepallength = np.genfromtxt(url,delimiter=',',dtype = "float", usecols=[0])
sMax,sMin = sepallength.max(),sepallength.min()
s = (sepallength - sMin)/(sMax - sMin)
#or
s = (sepallength -sMin)/sepallength.ptp()
print(s)

#Ex26

#Return the number of 5% maximal position and minimal position
sepallengh = np.genfromtxt(url,delimiter=',',dtype='float',usecols=[0])
print(np.percentile(sepallength,q=[5,95]))

#Ex27
#Return the default position
iris_2d = np.genfromtxt(url,delimiter=",",dtype='float',usecols=[0,1,2,3])
iris_2d[np.random.randint(150,size=20), np.random.randint(4,size = 20)] = np.nan

print("Number of missing values : \n",np.isnan(iris_2d[:,0]).sum())
print("Position of missing values : \n",np.where(np.isnan(iris_2d[:,0])))

#Ex28
#Return if there is a default value
print(np.isnan(iris_2d).any())

#Ex29
#Replace the defalut value to 0
iris_2d[np.isnan(iris_2d)]=0
print(iris_2d)

#Ex30
#Return the set of all elements
species = np.array([row.tolist()[4]for row in iris])
np.unique(species, return_counts = True)

#Ex31
#Arrange the 2d-array by the first row
print(iris[iris[:,0].argsort()][:5])

#Ex32
#Return the most frequent element in an array
vals, counts = np.unique(iris[:,2],return_counts=True)
print(vals[np.argmax(counts)])

#Ex33
#Return the fisrt value >1 in the 4th row
np.argwhere(iris[:,3].astype(float)>1.0)[0]

#Ex34
#Set the upper bound and lower bound
np.set_printoptions(precision=2)
np.random.seed(100)
a = np.random.uniform(1,50,20)
print(np.clip(a,a_min=10,a_max=30))
print(np.where(a < 10,10,np.where(a>30,30,0)))

#Ex35
#Delete all the defaults
a=np.array([1,2,3,np.nan,5,6,7,np.nan])
print(a[~np.isnan(a)])
