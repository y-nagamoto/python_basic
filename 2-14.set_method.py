s = {1, 2, 3, 4, 5}
print(s)
s.add(6)
print(s)
"""
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5, 6}
"""

s.remove(6)
print(s)
s.clear()
print(s)
"""
{1, 2, 3, 4, 5}
set()
"""

a = {}
print(type(a))
print(a)
"""
<class 'dict'>
{}
"""