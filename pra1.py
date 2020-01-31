n = [1,2,3,4,5,6,7  ]

def count(n):
    odd = 0
    even = 0
    for i in n:
        if i%2== 0:
            even+=1
        else:
            odd+=1
    return "odd = {}, even = {}".format(odd, even)

result = count(n)

print(result)