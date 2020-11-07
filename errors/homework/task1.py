
try:
    for i in ['a','b','c']:
        print(i ** 2)
except TypeError:
    print("Unsupported operand type(s) for ** or pow(): 'str' and 'int'")
