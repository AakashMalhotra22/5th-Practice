from numpy import*
f = array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12]
])

print(f.dtype)
print(f.ndim)
print(f.size)
print(f.shape)

f2 = f.flatten()

print(f2)

m = matrix(f)
print(f)

m1 = matrix("1,2,3; 4,5,6;7,8,9")
print(m1acha)