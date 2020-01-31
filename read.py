ask = open("test1.py", "r")

for number in ask.readlines():
    print(number)

ask.close()

List = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10]


]

print(List)
print(List[1][0])

for row in List:
    for col in row:
        print(col)