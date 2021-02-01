from termcolor_package.termcolor import colored

print('test')
print(colored('test', 'red'))
"""
test
test
"""

print(colored('test', 'green'))
"""
test
"""

# ターミナル上は指定の色に変わる

print(help(colored))