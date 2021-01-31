# グローバル変数を関数内で使用することは可能だが、関数内でその変数に代入することは不可

#グローバル変数
animal = 'cat'

def f():
    # ローカル変数
    animal = 'dog'
    print('local', animal)
    print('local', locals())

f()
print('global', animal)
print('global', globals())
"""
local dog
local {'animal': 'dog'}
global cat
global {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x102393fd0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/Users/yusakunagamoto/udemy/python/basic/3-31.namespace_scope.py', '__cached__': None, 'animal': 'cat', 'f': <function f at 0x10244d430>}
"""


# グローバル変数に対して関数内で値を代入する
def f():
    global animal
    animal = 'neko'
    print('local', animal)

f()
print('global', animal)
"""
local neko
global neko
"""

