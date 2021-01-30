def say_something():
    print('hi')
say_something()
print(type(say_something))
"""
hi
<class 'function'>
"""

f = say_something
f()
"""
hi
"""


#返り値あり
def say_something2():
    s = 'hi'
    return s

result = say_something2()
print(result)
"""
hi
"""


#引数あり
def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't"


print(what_is_this('red'))
print(what_is_this('green'))
print(what_is_this('white'))
"""
tomato
green pepper
I don't
"""
