import cmath
import math
my_file = open('example.txt')
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.close()

with open('example.txt', mode = 'r') as f:
    print(f.read())
with open('example.txt', mode = 'a') as f:
    f.write("Hello, world")
with open('example.txt', mode = 'r') as f:
    print(f.read())
with open('blablabla.txt', mode = 'w') as f:
    f.write("Something which is not ment to be !!!")

def solve(s):
    new_str = ""
    new_str = new_str + s[0].upper()
    for i in range(1, len(s)):
        if s[i - 1] == " ":
            new_str = new_str + s[i].upper()
        else:
            new_str = new_str + s[i]
    return new_str

print(solve("Hello my name is  1g Yunus"))
print(abs(complex(1-1j)))
print(cmath.phase(complex(1-1j)))
Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = map(int, input().split())
first = []
second = defaultdict(list)
for i in range(n):
    a = input()
    first.append(a)
for i in range(m):
    b = input()
    second[b] = []

for i, j in enumerate(first):
    if j in second.keys():
        second[j].append(index())
    else:
        second[j].append(-1)

for i in second.values():
    print(" ".join(map(str, i)))
