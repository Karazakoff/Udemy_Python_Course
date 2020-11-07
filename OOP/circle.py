class Circle():
    # Class Object Attribute
    pi = 3.14
    def __init__(self,radius = 1):
        self.radius = radius
        self.area = radius * radius * 2 * Circle.pi
    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(100)
print(my_circle.pi)
print(my_circle.area)
print(my_circle.get_circumference())
