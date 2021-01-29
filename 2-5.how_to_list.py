seat = []
min = 0
max = 5
first_action = min <= len(seat) < max
print(first_action)
"""
True
"""
seat.append('p')
second_action = min <= len(seat) < max
print(second_action)
"""
True
"""
print(len(seat))
"""
1
"""
seat.append('p')
third_action = min <= len(seat) < max
print(third_action)
"""
Ture
"""
print(len(seat))
"""
2
"""
seat.append('p')
seat.append('p')
fourth_action = min <= len(seat) < max
print(fourth_action)
"""
True
"""
seat.append('p')
fifth_action = min <= len(seat) < max
print(fifth_action)
"""
False
"""
print(len(seat))
"""
5
"""
seat.pop(0)     # 1番目を削除
sixth_action = min <= len(seat) < max
print(sixth_action)
"""
True
"""

