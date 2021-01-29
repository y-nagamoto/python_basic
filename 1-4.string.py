"""
文字列内にシングルコートがある場合はダブルコートで囲む
またはバックスラッシュをシングルコートの前につける
"""
print('hello')
print("I don't know")
print('I don\'t know')
print('say "I don\'t know"')
print ("say \"I don't know\"")
"""
hello
I don't know
I don't know
say "I don't know"
say "I don't know"
"""

#改行
print('hello. \nHow are you?')
"""
hello. 
How are you?
"""

#バックスラッシュをそのまま使用する
print(r'C:\name\name')
"""
C:\name\name
"""

#複数行
print("""
line1
line2
line3
""")
"""

line1
line2
line3

"""

#複数行（空行を入れない）
print("##########")
print("""\
line1
line2
line3\
""")
print("##########")
"""
##########
line1
line2
line3
##########
"""

#文字列演算子
print('Hi.' * 3 + 'Mike.')
"""
Hi.Hi.Hi.Mike.
"""

s = ('aaaaaaaaaa'
     'bbbbbbbbbb')
print(s)
ss = 'cccccccccc'\
     'dddddddddd'
print(ss)
"""
aaaaaaaaaabbbbbbbbbb
ccccccccccdddddddddd
"""
