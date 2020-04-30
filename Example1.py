import numpy as np

list=[[1,2,3],[4,5,6],[7,8,9]]
matrix=np.array(list)
print(matrix)

print(matrix.itemsize) #4  int size 4 (if it is float it displays 8)
print(matrix.dtype) # int32 (if it is float it displays float64)
print(matrix.size)  # 9 no of elements
print(matrix.shape) # (3,3) shape of the matrix i:e 3*3 matrix

# output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# 4 //int size
# int32 // datatype
# 9   // no of elements
# (3, 3) // shape of matrix