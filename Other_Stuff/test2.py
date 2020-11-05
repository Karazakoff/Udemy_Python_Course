number = int(input())
for i in range(number):
    s = list(input())
    old_back = [s[-1]]
    index_1 = 0
    print(ord(s[0]), ord(s[1]))
    for i in range(len(s) - 1, 0, -1):
        if ord(s[i]) <= ord(s[i - 1]):
            old_back.append(s[i])
        else:
            index_1 = i - 1
            break
    back = list(reversed(old_back))

    print("back = {}".format(back))
    print("index_1 = {}".format(index_1))
    value = s[index_1]
    print("value = {}".format(value))
    min = 999
    index_2 = 0
    for i in range(len(back)):
        if ord(value) < ord(back[i]):
            print("TRUE")
            if min > ord(back[i]):
                print("TRUE")
                min = ord(back[i])
                index_2 = i
    print("min = {}".format(min))
    print("index_2 = {}".format(index_2))
    s[index_1] = chr(min)
    s[index_2] = value
    print("s[index_1] = {}".format(s[index_1]))
    print("s[index_2] = {}".format(s[index_2]))
    print(s[:index_1 + 1], end="")
    print(sorted(back))
