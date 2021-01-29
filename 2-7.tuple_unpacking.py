num_tuple = (10, 20)
print(num_tuple)
"""
(10, 20)
"""

x, y = num_tuple
print(x, y)
print(type(x))
print(type(y))
"""
(10, 20)
10 20
<class 'int'>
<class 'int'>
"""

x, y = 10, 20
print(x, y)
"""
10 20
"""

min, max = 0, 100
print(min, max)
"""
0 100
"""

#タプルを用いた数字の入れ替え
#通常
i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)
"""
20 10
"""
#タプルのアンパッキングを使用
a = 100
b = 200

a, b = b, a
print(a, b)
"""
200 100
"""

