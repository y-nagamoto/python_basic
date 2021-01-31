def g():
    for i in range(10):
        yield i

g = g()
print(type(g))
print(next(g))
print(next(g))
"""
<class 'generator'>
0
1
"""


g = (i for i in range(10))
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
"""
<class 'generator'>
0
1
2
3
"""
