from PIL import Image

mac = Image.open('example.jpg')

# print(mac.show())

print(mac.format_description)
print(mac.filename)

print(mac.size)

# print(mac.crop((0,0,100,100)).show())

pencils = Image.open('pencils.jpg')

print(pencils.size)
#
# print(pencils.show())

x = 0
y = 0

w = 1950 / 3
h = 1300 / 10

# print(pencils.crop((x,y,w,h)).show())

# Bottom pencils
x = 0
y = 1100

w = 1950 / 3
h = 1300
#
# print(pencils.crop((x,y,w,h)).show())

print(mac.size)

halfway = 1993 / 2

x = halfway - 200
w = halfway + 200

y = 800
h = 1257

# print(mac.crop((x,y,w,h)).show())

computer = mac.crop((x,y,w,h))
mac.paste(im = computer, box = (0,0))
# print(mac.show())
print(mac.resize((3000, 500)))
# print(mac.rotate(90).show())


red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png')

blue.putalpha(255)
blue.show()
