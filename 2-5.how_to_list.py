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
"""