# 1 less memory
# 2  very fast
# 3 very convienent all are compare to list

# first 1 proved that is less memory
import numpy as np
import time
import sys

s= range(1000) # it takes all integer values upto 999 from 0
print(sys.getsizeof(5)*len(s)) # print space occupied by list  28000

d=np.arange(1000) # same as about it takes all integer values upto 999

print(d.size*d.itemsize) # print space occupied by numpy array 4000

# 2nd statement for less Time

SIZE=100000

l1=range(SIZE)
l2=range(SIZE)

a=np.arange(SIZE)
b=np.arange(SIZE)

start=time.time()
# print(start)
result=[(x,y) for x,y in zip(l1,l2)]
# print(result)
print((time.time()-start)*1000)  #31.24213218688965



start=time.time()
# print(start)

result=a+b
# print(result)
print((time.time()-start)*1000) #0.0


# by observing output we can conclude that list are take more time compare to numpy array