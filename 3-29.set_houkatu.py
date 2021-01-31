s = set()

for i in range(10):
    s.add(i)

print(s)
"""
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
"""


s = {i for i in range(10)}
print(s)
"""
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
"""
