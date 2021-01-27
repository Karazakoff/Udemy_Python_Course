import time
def func_one(n):
    return [str(num) for num in range(n)]

def func_two(n):
    return list(map(str, range(n)))

start_time = time.time()
func_one(1_000_000)
end_time = time.time()
code_time = end_time - start_time
print(code_time)
start_time = time.time()
func_two(1_000_000)
end_time = time.time()
code_time = end_time - start_time
print(code_time)

import timeit

stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt, setup, number = 100_000))


stmt2 = '''
func_two(100)
'''

setup2 = '''
def func_two(n):
    return list(map(str, range(n)))
'''

print(timeit.timeit(stmt2, setup2, number = 100_000))
