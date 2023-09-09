import math
import os
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
