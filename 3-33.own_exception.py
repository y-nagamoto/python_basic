class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

#check()
"""
  File "/Users/yusakunagamoto/udemy/python/basic/3-33.own_exception.py", line 8, in check
    raise UppercaseError(word)
__main__.UppercaseError: APPLE
"""

try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')
"""
This is my fault. Go next
"""