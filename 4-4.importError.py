try:
    from lesson_package.talk import utils
except ImportError:
    from lesson_package import utils

s = utils.say_twice('word')
print(s)
"""
word!word!
"""
