# Falseと判断されるケース
# False, 0, 0.0, ' ', [], (), {}, set()

is_ok = 1
if is_ok:
    print('OK')
else:
    pritn('NG')
"""
OK
"""

is_ok = 100
if is_ok:
    print('OK')
else:
    print('NG')
"""
OK
"""

is_ok = 0
if is_ok:
    print('OK')
else:
    print('NG')
"""
NG
"""

is_ok = [1, 2, 3, 4]
if is_ok:
    print('OK')
else:
    print('NG')
"""
OK
"""