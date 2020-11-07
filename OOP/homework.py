class Line:

    def __init__(self,coor1,coor2):
        self.x1 = int(coor1[0])
        self.y1 = int(coor1[1])
        self.x2 = int(coor2[0])
        self.y2 = int(coor2[1])
    def distance(self):
        print(((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** 0.5)

    def slope(self):
        print((self.y2 - self.y1) / (self.x2 - self.x1))

class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        self.pi = 3.14

    def volume(self):
        print(self.pi * self.radius ** 2 * self.height)

    def surface_area(self):
        print(2 * self.pi * self.radius * (self.height + self.radius))

# Line
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()
li.slope()

# Cylinder
c = Cylinder(2,3)
c.volume()
c.surface_area()
