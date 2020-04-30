# using list it's to difficulty to do Basic Arthamatic operations in matrix
# using numpy it's quit easy
# here u can know how convinent is compare to list
import numpy as np

a=np.array([(1,2,3),(3,4,5)])

b=np.array([(1,2,3),(3,4,5)])


print("addition")

print(a+b) #addition

print("substraction")
print(a-b)  #substraction

print("multiplication")
print(a*b) # multiplication of an elements

print("division")
print(a//b) # division


# output:
# addition
# [[ 2  4  6]
#  [ 6  8 10]]
# substraction
# [[0 0 0]
#  [0 0 0]]
# multiplication
# [[ 1  4  9]
#  [ 9 16 25]]
# division
# [[1 1 1]
#  [1 1 1]]
#
# Process finished with exit code 0
