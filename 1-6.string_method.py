s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')   #指定の文字列で始まっているか
print(is_start)

print('#############')

print(s.find('Mike'))           #何文字目に指定も文字列があるか
print(s.rfind('Mike'))          #何文字目に指定も文字列があるか(後方の文字)
print(s.count('Mike'))          #指定の文字列が何個入っているか
print(s.capitalize())           #先頭の文字を大文字
print(s.title())                #各単語の先頭を大文字
print(s.upper())                #全て大文字
print(s.lower())                #全て小文字
print(s.replace('Mike', 'Nancy'))              #文字列の置換
"""
True
#############
11
20
2
My name is mike. hi mike.
My Name Is Mike. Hi Mike.
MY NAME IS MIKE. HI MIKE.
my name is mike. hi mike.
My name is Nancy. Hi Nancy.
"""