s = "laslfjaisjflakdnfasfsof"

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)
"""
{'l': 3, 'a': 4, 's': 4, 'f': 5, 'j': 2, 'i': 1, 'k': 1, 'd': 1, 'n': 1, 'o': 1}
"""


d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)
"""
{'l': 3, 'a': 4, 's': 4, 'f': 5, 'j': 2, 'i': 1, 'k': 1, 'd': 1, 'n': 1, 'o': 1}
"""


from collections import defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1
print(d)
print(d['f'])
"""
defaultdict(<class 'int'>, {'l': 3, 'a': 4, 's': 4, 'f': 5, 'j': 2, 'i': 1, 'k': 1, 'd': 1, 'n': 1, 'o': 1})
5
"""