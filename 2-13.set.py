a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
print(a)
print(type(a))
"""
{1, 2, 3, 4, 5, 6}
<class 'set'>
"""

b = {2, 3, 3, 6, 7}
print(b)
"""
{2, 3, 6, 7}
"""

print(a - b)
print(b - a)
print(a & b)
print(a | b)
print(a ^ b)
"""
{1, 4, 5}
{7}
{2, 3, 6}
{1, 2, 3, 4, 5, 6, 7}
{1, 4, 5, 7}
"""

