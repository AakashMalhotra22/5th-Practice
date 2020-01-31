for i in range(10):
    if i%2 != 0:
        continue
    else:
        print(i)

for i in range(4):
    print("#", end = "")
    for r in range(4):
        print("#", end = "")
    print("")


print("             ")
r =1
for i in range(4):
    print("")
    while r<= 4:
        print(r*"#")
        r+=1

r = 4
while r>=1:
    print(r*"#")
    r-=1

r = int(input())
for i in range(2,r-1):
    if r%i == 0:
        print("composite")
        break
else:
    print("prime")

from array import*

r = array('i',[1,2,3,4])

print(r.buffer_info())