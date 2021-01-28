import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')

soup = bs4.BeautifulSoup(res.text, 'lxml')
computer = soup.select('.thumbimage')[0]

print(computer['src'])

image_link = requests.get("https:" + computer['src'])

with open("Casparov.jpg", 'wb') as f:
    f.write(image_link.content)
