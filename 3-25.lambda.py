l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

def sample_func(word):
    return word.capitalize()

change_words(l, sample_func)
"""
Mon
Tue
Wed
Thu
Fri
Sat
Sun
"""

sample_func = lambda word: word.capitalize()
change_words(l, sample_func)
"""
Mon
Tue
Wed
Thu
Fri
Sat
Sun
"""

change_words(l, lambda word: word.capitalize())
"""
Mon
Tue
Wed
Thu
Fri
Sat
Sun
"""
change_words(l, lambda word: word.lower())
"""
mon
tue
wed
thu
fri
sat
sun
"""
