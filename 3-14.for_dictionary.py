d = {'x': 100, 'y': 200}

for v in d:
    print(v)
"""
x
y
"""

for k, v in d.items():
    print(k, ':', v)
print(d.items())
"""
x : 100
y : 200
dict_items([('x', 100), ('y', 200)])
"""
