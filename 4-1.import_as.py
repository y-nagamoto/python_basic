import lesson_package.utils

r = lesson_package.utils.say_twice('hello')

print(r)
"""
hello!hello!
"""


from lesson_package import utils

print(utils.say_twice("good"))
"""
good!good!
"""


from lesson_package import utils as u

print(u.say_twice("best"))
"""
good!good!
"""


#この書き方は好まれない
from lesson_package.utils import say_twice

print(say_twice("nice"))
"""
nice!nice!
"""

