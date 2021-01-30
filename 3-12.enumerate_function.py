# インデックスをつけるには

i = 0
for fruit in ['apple', 'banana', 'orange']:
    print(i, fruit)
    i += 1
"""
0 apple
1 banana
2 orange
"""

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)
"""
0 apple
1 banana
2 orange
"""