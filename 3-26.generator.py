l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)

print("################")

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

for g in greeting():
    print(g)
"""
Good morning
Good afternoon
Good night
################
Good morning
Good afternoon
Good night
"""


g = greeting()
print(next(g))
print("@@@@@@@@")
print(next(g))
print("@@@@@@@@")
print(next(g))
"""
Good morning
@@@@@@@@
Good afternoon
@@@@@@@@
Good night
"""


def counter(num=10):
    for _ in range(num):
        yield 'run'

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

g = greeting()
c = counter()

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))
"""
Good morning
run
run
run
run
run
Good afternoon
run
run
run
run
run
Good night
"""