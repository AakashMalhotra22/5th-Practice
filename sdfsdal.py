from numpy import*

tanu = array([1,2,3,4,5])

r1 = tanu.copy()
r1[0] = 100
print(r1)
print(tanu)
print(id(r1))
print(id(tanu))

