is_empty = None
print(is_empty)
print(type(is_empty))
"""
None
<class 'NoneType'>
"""

# Noneの等しいかの判定にはisを使用する
# isはオブジェクトとして比較する演算子
if is_empty is None:
    print('None!!!')
else:
    print('Not None')
"""
None!!!
"""
if is_empty is not None:
    print('None!!!')
else:
    print('Not None')
"""
Not None
"""

