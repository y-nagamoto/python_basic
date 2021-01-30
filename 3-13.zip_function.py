days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])
"""
Mon apple coffee
Tue banana tea
Wed orange beer
"""

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)
"""
Mon apple coffee
Tue banana tea
Wed orange beer
"""
