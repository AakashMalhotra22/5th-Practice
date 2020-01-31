from new import sub

def smart(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

y = smart(sub)

y(2,4)