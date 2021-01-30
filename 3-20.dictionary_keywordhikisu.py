def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

menu(entree='beef', drink='coffee')
"""
{'entree': 'beef', 'drink': 'coffee'}
entree beef
drink coffee
"""

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}
menu(**d)
"""
entree beef
drink ice coffee
dessert ice
"""


#複合渡し
def menu2(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu2('banana', 'apple', 'orange', entree='beef', drink='coffee')
"""
banana
('apple', 'orange')
{'entree': 'beef', 'drink': 'coffee'}
"""
