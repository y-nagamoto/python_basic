def test_func(x, l=[]):
    l.append(x)
    return l

y = [1, 2, 3]
r = test_func(100, y)
print(r)
"""
[1, 2, 3, 100]
"""

#以下のような処理になるため、デフォルト引数に空のリストを指定するのは推奨されていない
#リストだけではなく参照渡しになるものを指定するのを避けるべき
r = test_func(100)
print(r)
r = test_func(100)
print(r)
"""
[100]
[100, 100]
"""


#解決策はNoneを指定する
def test_func2(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r2 = test_func2(100)
print(r2)
r2 = test_func2(100)
print(r2)
"""
[100]
[100]
"""
