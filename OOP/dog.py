class Dog():
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'
    def __init__(self, breed, name, color, spots, age):
        # Accepting parameters
        # Assigning to self to use in advance
        self.breed  = breed
        self.name = name
        self.color = color
        self.spots = spots
        self.age = age
    # Function voice prints just a line of string
    def voice(self, number):
        print("Huff! Huff! My name is {} and the number is {}".format(self.name, number))


my_dog = Dog(breed = "Huskie", name = "Sammy", color = "Brown", spots = False, age = 3)
print(" Breed = {}\n Name = {}\n Color = {}\n Does dog have spots = {}\n The age of dog = {}\n".format(my_dog.breed, my_dog.name, my_dog.color, my_dog.spots, my_dog.age))
my_dog.voice(10)
print(my_dog.species)
