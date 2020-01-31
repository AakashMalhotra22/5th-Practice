a = 199


def ram():
    a = 10
    globals()["a"]
    print("inside", a)
    globals()["a"]= 12
    print(globals()["a"])
    print("r", a)


ram()
print(a)