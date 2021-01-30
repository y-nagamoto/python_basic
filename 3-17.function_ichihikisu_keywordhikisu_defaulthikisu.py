def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

#位置引数
menu('beef', 'beer', 'ice')
"""
entree =  beef
drink =  beer
dessert =  ice
"""
#キーワード引数
menu(entree='beef', dessert='ice', drink='beer')
"""
entree =  beef
drink =  beer
dessert =  ice
"""
#位置引数＋キーワード引数
menu('beef', dessert='ice', drink='beer')
"""
entree =  beef
drink =  beer
dessert =  ice
"""

#デフォルト引数
def default_menu(entree='beef', drink='wine', dessert='ice'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

default_menu()
"""
entree =  beef
drink =  wine
dessert =  ice
"""
default_menu('chiken', drink='cola')
"""
entree =  chiken
drink =  cola
dessert =  ice
"""
default_menu('chiken', drink='cola', )
"""
entree =  chiken
drink =  cola
dessert =  ice
"""