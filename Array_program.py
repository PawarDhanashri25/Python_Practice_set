#Python Program for Find remainder of array multiplication divided by n

import numpy



arr=list(map(int, input().split()))
n=int(input())

m=1
for i in arr:
    m*=i

result=m%n
print(result)


#multiplication of array element

m1=numpy.prod([i for i in arr])
print(m1) 
    
