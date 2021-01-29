print('a is {}'.format('a'))
print('a is {}'.format('test'))
print('a is {} {} {}'.format(1, 2, 3))
print('a is {0} {1} {2}'.format(1, 2, 3))
print('a is {2} {1} {0}'.format(1, 2, 3))
"""
a is a
a is test
a is 1 2 3
"""

print('My name is {0} {1}'.format('Sherlock', 'Holmes'))
print('My name is {0} {1}. I\'m {1} {0}'.format('Sherlock', 'Holmes'))
print('My name is {name} {family}. I\'m {family} {name}'.format(name='Sherlock', family='Holmes'))
"""
My name is Sherlock Holmes
My name is Sherlock Holmes. I'm Holmes Sherlock
My name is Sherlock Holmes. I'm Holmes Sherlock
"""


#数字と文字列の変換
x = str(1)
print(x)
print(type(x))
"""
1
<class 'str'>
"""