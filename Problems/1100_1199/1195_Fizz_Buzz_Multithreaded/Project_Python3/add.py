def add(a,b):
    return a+b

def test1(func):
    print(type(func)) # <class 'function'>
    return func(1,2)

result = test1(add)
print(result)

"""Error
result = test1(add(2,4))
print(result)
"""