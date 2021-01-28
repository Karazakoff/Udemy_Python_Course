import requests
import bs4

base_page = "http://books.toscrape.com/catalogue/page-{}.html"

three_star_titles = []

for i in range(1, 3):

    page = requests.get(base_page.format(i))
    soup = bs4.BeautifulSoup(page.text, 'lxml')
    for product in soup.select(".product_pod"):
        if len(product.select('.star-rating.Three')) != 0:
            three_star_titles.append(product.select('a')[1]['title'])
print(three_star_titles)
