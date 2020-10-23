n = int(input())
s = set(map(int, input().split()))
number = int(input())
for i in range(number):
    action = input()
    if action == 'pop':
        s.pop()
    else:
        func, index = action.split()
        if func == 'remove':
            s.remove(int(index))
        elif func == 'discard':
            s.discard(int(index))
print(sum(s))
