class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says WOOF"

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says MEOW"

jab = Dog('Jab')
felix = Cat('Felix')
print(jab.speak())
print(felix.speak())

for pet in [jab, felix]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(jab)
pet_speak(felix)


class Animal():
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):

    def speak(self):
        return self.name + " says WOOF"

class Cat(Animal):

    def speak(self):
        return self.name + " says MEOW"


george = Dog('George')
fibo = Cat('Fibo')
print(george.speak())
print(fibo.speak())
