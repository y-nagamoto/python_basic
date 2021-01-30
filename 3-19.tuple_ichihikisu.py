def say_something(*args):
    print(args)
    
    for arg in args:
        print(arg)

say_something('Hi', 'Mike', 'Nance')
"""
('Hi', 'Mike', 'Nance')
Hi
Mike
Nance
"""


def say_something2(word, *args):
    print('word =', word)
    for arg in args:
        print(arg)

say_something2('Hi', 'Mike', 'Nance')
"""
word = Hi
Mike
Nance
"""

#以下の表現は可能だがあまり用いられない
t = ('Bob', 'Tom')
say_something2('Hi', *t)
"""
word = Hi
Bob
Tom
"""
