# 1行ずつアルファベット順
import collections
import os
import sys

# 標準ライブラリとサードパーティライブラリの間には空行をもうける
import termcolor_package.termcolor

import lesson_package.talk.animal

# ライブリのパス
print(collections.__file__)
print(termcolor_package.termcolor.__file__)
print(lesson_package.talk.animal.__file__)
"""
/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/collections/__init__.py
/Users/yusakunagamoto/udemy/python/basic/termcolor_package/termcolor.py
/Users/yusakunagamoto/udemy/python/basic/lesson_package/talk/animal.py
"""

print(sys.path)
"""
['/Users/yusakunagamoto/udemy/python/basic', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python38.zip', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/lib-dynload', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/site-packages']
"""