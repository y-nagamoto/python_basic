d = {'x': 10, 'y': 20}
# help(d)

print(d.keys())
print(d.values())
"""
dict_keys(['x', 'y'])
dict_values([10, 20])
"""

d2 = {'x': 1000, 'j': 500}
print(d)
print(d2)
d.update(d2)
print(d)
print(d['x'])
print(d.get('x'))
"""
{'x': 10, 'y': 20}
{'x': 1000, 'j': 500}
{'x': 1000, 'y': 20, 'j': 500}
1000
1000
"""

r = d.get('z')
print(r)
print(type(r))
"""
None
<class 'NoneType'>
"""

print(d)
print(d.pop('x'))
print(d)
"""
{'x': 1000, 'y': 20, 'j': 500}
1000
{'y': 20, 'j': 500}
"""

del d['y']
print(d)
"""
{'j': 500}
"""

d.clear()
print(d)
"""
{}
"""

d = {'a': 100, 'b': 200}
print('a' in d)
print('j' in d)
"""
True
False
"""