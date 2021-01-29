"""
タプルとリストの違いは
タプル：要素の追加不可　⇨　読み込み用
リスト：要素の追加可
タプルにリストを格納することも可能
"""

t = (1, 2, 3, 4, 1, 2)
print(t)
print(type(t))
"""
(1, 2, 3, 4, 1, 2)
<class 'tuple'>
"""

print(t[0])
print(t[-1])
print(t[2:5:])
print(t.index(1))
print(t.index(1, 1))
print(t.count(1))
"""
1
2
(3, 4, 1)
0
4
2
"""

#print(help(tuple))

t = ([1, 2, 3], [4, 5, 6])
print(t)
print(t[0][0])
"""
([1, 2, 3], [4, 5, 6])
1
"""

#タプルは（）を付けなくても,をつけた時点でタプルの宣言になる
t = 1, 2, 3
print(type(t))
print(t)
t = 1,
print(type(t))
print(t)
"""
<class 'tuple'>
(1, 2, 3)
<class 'tuple'>
(1,)
"""

t = ()
print(type(t))
print(t)
t = (1)
print(t)
print(type(1))
"""
<class 'tuple'>
()
1
<class 'int'>
"""

#タプルは宣言時に足すことができる
new_tuple = (1, 2, 3) + (4, 5, 6)
print(new_tuple)
new_tuple = (1,) + (4, 5, 6)
print(new_tuple)
"""
(1, 2, 3, 4, 5, 6)
(1, 4, 5, 6)
"""