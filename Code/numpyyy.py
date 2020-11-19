import numpy as np

a=np.array([[1,2,3,4],[5,6,7,8]])
print(a)
# Get dimensions
print(a.ndim)
#Get shape
print(a.shape)
b= np.array([3,4,5,6],dtype='int16')
print(a*b)

print(b.ndim)
print(b.dtype)

print(b.itemsize)
print(b.nbytes)



a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
print(a.shape)

print(a[0,5])
print(a[0,:])
print(a[:,3])
print(a[0,1:7:2])
a[1,:]=22
print(a)



b= np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
print(b[0,1,1])
print(b[:,1,:])



# Initialize all zero matrix

a=np.zeros((2,3))
print(a)

b=np.ones((2,2))
print(b)

# initalize with any random value

b=np.full((2,2),98,dtype='float32')
print(b)
#full_like method
b=np.full_like(b,4)
print(b)



# initialize random decimal numbers
b=np.random.rand(4,2)
print(b)

b= np.random.random_sample(b.shape)
print(b)


b=np.random.randint(-2,20,size=(3,3))
print(b)


# identity matrix

b=np.identity(5)
print(b)

#Repeat an array

a=np.array([1,2,3])
a=np.repeat(a,3)
print(a)



a=np.array([[1,2,3],[4,5,6]])
a=np.array([[1,2,3]])
a=np.repeat(a,4,axis=0)
print(a)


# print
# [[1. 1. 1. 1. 1.]
# [1. 0. 0. 0. 1.]
# [1. 0. 9. 0. 1.]
# [1. 0. 0. 0. 1.]
# [1. 1. 1. 1. 1.]]

a=np.ones((5,5))
b=np.zeros((3,3))
b[1,1]=9
a[1:4,1:4]=b
print(a)


# Coping array 
a=np.array([1,2,3])
#b=a
b=a.copy()
b[0]=100
print(b)
print(a)

#Mathematics

a=np.array([1,2,3,4])
a=a+2
a=a*2

a=np.sin(a)
print(a)

# Linear algebra

a=np.ones((2,4))
print(a)
b=np.full((4,2),2)
print(b)

print(np.matmul(a,b))

# finding determinant
a=np.identity(3)
a=np.linalg.det(a)
print(a)


#Statistic

a= np.array([[1,2,3],[4,5,6]])
a=np.max(a,axis=0)
#a=np.min(a)

a=np.sum(a)
print(a)

#Reorganizing arrays

a=np.array([1,2,3,4])
a=a.reshape((2,2))
print(a)


#Vertical stack
v1= np.array([1,2,3,4])
v2=np.array([5,6,7,8])
a=np.vstack([v2,v1])
print(a)

# horizontal stack

a=np.hstack([v1,v2])
print(a)



import os
# Load data from file
#os.chdir('C:\\USMAN FILES\\Data Science\\Numpy')

a=np.genfromtxt('data.txt', delimiter=",")
print(a)
print(a.astype('int32'))

# Advance indexing & boolean masking

print(np.any(a<20,axis=0))
print("\n")




print(~((a>10) & (a<20) | (a==20)))
print("\n")
print((a>10) & (a<20) | (a==20))
#print values greater check
print(a[a>20])
# index a list in numpy
a=np.array([1,2,3,4,5,6,7,8,9])
print(a[[2,5,7]])


a=np.ones((6,5))

b=np.array([[11,12],[16,17]])

a[2:4,0:2]=b
print(a)
print("\n")

#c=np.identity(4)

c=np.array([2,8,14,20])

a[[0,1,2,3],[1,2,3,4]]=c

#a[0,1]=c[0]
#a[1,2]=c[1]
#a[2,3]=c[2]
#a[3,4]=c[3]

print(a)
print("\n")
d=np.array([4,5,24,25,29,30])
#a[0,3]=d[0]
#a[0,4]=d[1]
#a[4,3]=d[2]
#a[4,4]=d[3]
#a[5,3]=d[4]
#a[5,4]=d[5]
a[[0,0,4,4,5,5],[3,4,3,4,3,4]]=d
print(a)

























