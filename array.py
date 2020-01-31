from numpy import *

sdf = array([1,2,3,4,])

print(sdf)

tanu = array([1,2,3,4], float)
print(tanu)

print(tanu.dtype)


aak1 = linspace(0,16,3)
print(aak1)

aak2 = arange(0,16,2)
print(aak2)

aak3 = zeros(2)
print(aak3)

aak4 = ones(4)
print(aak4)

aak5 = logspace(1,40, 5)

print(aak5)
print('%.2f'% aak5[0])