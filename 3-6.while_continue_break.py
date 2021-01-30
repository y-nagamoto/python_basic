count = 0
while count < 5:
    print(count)
    count += 1
"""
0
1
2
3
4
"""

count = 0
while True:
    if count >= 5:
        break
    print(count)
    count += 1
"""
0
1
2
3
4
"""

count = 0
while True:
    if count >= 5:
        break

    # countが2の時は以降をスキップして次のループに進む
    if count == 2:
        count += 1
        continue
    
    print(count)
    count += 1
"""
0
1
3
4
"""
