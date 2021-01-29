x = {'a': 1}
y = x
y['a'] = 1000   #参照渡し
print(x)
print(y)
"""
{'a': 1000}
{'a': 1000}
"""

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)
"""
{'a': 1}
{'a': 1000}
"""
