import math
import os
from functools import reduce
math.floor(4.12231)

# os Module ----> can do a lot of thinks  

cmd = 'nvim'

# os.system(cmd)

# File I/O


f = open('demo.txt' , 'r')
while True:
    line  = f.readline()
    print(line)
    if not line: 
        break



# Lambda functions

double = lambda x: x*2

print(double(5))


 # map filter reduce ------------------------------------------

def cube(x):
     return x * x * x

l = [1, 2, 4 , 6, 4, 3]


newl = list(map(cube, l))
print(newl)

# Filter 

def filter_func(a):
    return a > 4 

newfl = list(filter(filter_func , l))

print(newfl)


# Reduce 

def mysum(x, y):
    return x + y

sum = reduce(mysum, l)

print(sum)


# is == 
# is --> compare location of object in memory 
# == --> compare value 

a =  3 
b =  3  

print( a is b)
