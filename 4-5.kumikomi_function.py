ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

print(sorted(ranking))
"""
['A', 'B', 'C']
"""

print(sorted(ranking, key=ranking.get))
"""
['B', 'C', 'A']
"""

print(sorted(ranking, key=ranking.get, reverse=True))
"""
['A', 'C', 'B']
"""
