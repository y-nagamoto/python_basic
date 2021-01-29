word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])    #2の手前まで
print(word[:2])     #省略可能
print(word[2:5])    #3文字目から5文字目を表示
print(word[2:])     #2番目から最後
print('#######')
word = 'J' + word[1:]
print(word)
print(word[:])      #全て
print(len(word))    #len:文字数
"""
p
y
n
py
py
tho
thon
Jython
Jython
6
"""

