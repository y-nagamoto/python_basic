d = {'x': 10, 'y': 20}
print(d)
print(type(d))
"""
{'x': 10, 'y': 20}
<class 'dict'>
"""

print(d['x'])
print(d['y'])
"""
10
20
"""

d['x'] = 100
print(d)
d['x'] = 'xxxx'
print(d)
"""
{'x': 100, 'y': 20}
{'x': 'xxxx', 'y': 20}
"""

d['z'] = 200
print(d)
"""
{'x': 'xxxx', 'y': 20, 'z': 200}
"""

d[1] = 10000
print(d)
"""
{'x': 'xxxx', 'y': 20, 'z': 200, 1: 10000}
"""

dic = dict(a=10, b=20)
print(dic)
"""
{'a': 10, 'b': 20}
"""

dic = dict([('a', 1), ('b', 2)])
print(dic)
"""
{'a': 1, 'b': 2}
"""
