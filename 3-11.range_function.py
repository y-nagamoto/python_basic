num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in num_list:
    print(i)
"""
0
1
2
3
4
5
6
7
8
9
"""

for i in range(10):
    print(i)
"""
0
1
2
3
4
5
6
7
8
9
"""

# 5から10までの範囲
for i in range(5, 10):
    print(i)
"""
5
6
7
8
9
"""

# 2から10まで3つとばし
for i in range(2, 10, 3):
    print(i)
"""
2
5
8
"""


for i in range(5):
    print('hello')
"""
hello
hello
hello
hello
hello
"""

# インデックスをつける
for i in range(5):
    print(i, 'hello')
"""
0 hello
1 hello
2 hello
3 hello
4 hello
"""

# for分内で条件式の変数を使用しないと明示的に表す
for _ in range(5):
    print('bye')
"""
bye
bye
bye
bye
bye
"""