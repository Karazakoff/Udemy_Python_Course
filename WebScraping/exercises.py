import requests
import bs4

page = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(page.text, 'lxml')
authors = set()
for author in soup.select('.author'):
    authors.add(author.text)
print(authors)

quotes = []

for quote in soup.select('.text'):
    quotes.append(quote.text)
[print(quote) for quote in quotes]

top_tags = []

for tag in soup.select('.tag-item .tag'):
    top_tags.append(tag.text)

[print(f"{i + 1} --> {j}") for i, j in enumerate(top_tags)]
