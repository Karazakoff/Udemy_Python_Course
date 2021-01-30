from PIL import Image

words = Image.open("word_matrix.png")

mas = Image.open("mask.png")

print(words.size)

mas = mas.resize((1015, 559), Image.ANTIALIAS)
print(mas.size)
mas.putalpha(150)
words.paste(im = mas, box = (0,0), mask = mas)
words.save('secret_words.png')
