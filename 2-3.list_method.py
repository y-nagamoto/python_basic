r = [1, 2, 3, 4, 5, 1, 2, 3]


print(r.index(3))
print(r.index(3, 3))
print(r.count(3))
"""
2
7
2
"""

if 5 in r:
    print('exist')
"""
exist
"""

r.sort()
print(r)
"""
[1, 1, 2, 2, 3, 3, 4, 5]
"""

r.sort(reverse=True)
print(r)
"""
[5, 4, 3, 3, 2, 2, 1, 1]
"""

r.reverse()
print(r)
"""
[1, 1, 2, 2, 3, 3, 4, 5]
"""


s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)
"""
['My', 'name', 'is', 'Mike']
"""

x = ' '.join(to_split)
print(x)
"""
My name is Mike
"""

y = ' ####'.join(to_split)
print(y)
"""
My ####name ####is ####Mike
"""

print(help(list))   #listのヘルプを表示q


