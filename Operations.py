# basic Operations

import numpy as np

list=[[1,2],[4,5],[7,8]]
matrix=np.array(list)
print(matrix)

#slicing

print(matrix[0:2,1]) # 0:2 means from staring row to first row excluding 2 # AFETER comma num indicates position of the element

#reshape

matrix=matrix.reshape(2,3)
print(matrix)

#slicing

print(matrix[0:,1])

# maximum value

print(matrix.max())

# minimum value

print(matrix.min())

#sum of the matrix

print(matrix.sum())


print("matrix is")
print("==============================")
print()
print(matrix)
print("addition of individual column")
print(matrix.sum(axis=0)) # addition of individual column

print("addition of individual column")
print(matrix.sum(axis=1)) # addition of individual rows

# square root of each element

print("square root")
print(np.sqrt(matrix))

#standard deviation


print("standard deviation")
print(np.std(matrix))

