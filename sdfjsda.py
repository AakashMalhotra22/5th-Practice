from array import *

r = array('i',[1,2,3,4])

print(r.buffer_info())
print(r.typecode)
print(r.reverse())
print(r)

r1 = array(r.typecode, [a*a for a in r])
print(r1)

for i in range(len(r1)):
    print(r1[i])


