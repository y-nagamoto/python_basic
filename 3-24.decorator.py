# デコレーター
# 関数実施に必ず実施する処理を関数として設定
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def add_num(a, b):
    return a + b

f = print_info(add_num)
r = f(10, 20)
print(r)
"""
start
end
30
"""


# 上記ではわかりにくため、デコレーターは＠を利用して書く
def print_info_new(func):
    def warapper_new(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return warapper_new

@print_info_new
def add_num_new(a, b):
    return a + b

r = add_num_new(10, 20)
print(r)
"""
start
end
30
"""


@print_info_new
def sub_num(a, b):
    return a - b

r2 = sub_num(20, 5)
print(r2)
"""
start
end
15
"""


def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)
"""
func: add_num
args: (10, 20)
kwargs: {}
result: 30
30
"""

@print_info_new
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)
"""
start
func: add_num
args: (10, 20)
kwargs: {}
result: 30
end
30
"""

@print_more
@print_info_new
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)
"""
func: warapper_new
args: (10, 20)
kwargs: {}
start
end
result: 30
30
"""