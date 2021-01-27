import math

print(math.pi)
print(math.e)
value = 4.35
print(math.floor(value))
print(math.ceil(value))
print(round(4.5))
print(round(5.5))
print(math.inf)
print(math.nan)
print(math.log(math.e))
print(math.log(100,10))
print(math.sin(10))
print(math.degrees(math.pi / 2))
print(math.radians(math.pi))

import random

print(random.randint(1,100))
print(random.randint(1,50))
print(random.randint(1,10))
# random.seed(101)
print(random.randint(1,100))
print(random.randint(1,50))
print(random.randint(1,10))

my_list = list(range(1,16))
print(my_list)
print(random.choice(my_list))
print("It has dublicates: ")
print(random.choices(population = my_list, k = 10))

print("It has no dublicates: ")
print(random.sample(population = my_list, k = 10))

random.shuffle(my_list)
print(my_list)
print("Uniform takes any value between a and b including float numbers")
print(random.uniform(0,100))
print(random.gauss(mu = 0, sigma = 1))
