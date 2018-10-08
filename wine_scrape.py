from requests import get
from bs4 import BeautifulSoup
from urllib.parse import urljoin

'''
Tool to scrape wine information off websites for input into a pandas dataframe
'''

# First equisite collection page on aldi
url_aldi = 'https://www.aldi.co.uk/exquisite-haut-poitou-sav-blanc/p/086088246528000'
response = get(url_aldi)

html_wine = BeautifulSoup(response.text, 'html.parser')
type(html_wine)

# Scrape exquisite collection urls into a list
base_url = 'https://www.aldi.co.uk/c/wines/exquisite-collection?q=%3Apopular&page=0'
response = get(base_url)
soup = BeautifulSoup(response.content, "lxml")
aldi_exq = []
headlines = soup.find_all(class_="category-item__link js-category-link")
for headline in headlines:
    aldi_exq.append(urljoin(base_url, headline["href"]))
print(aldi_exq)

# Div containing wine titles
wine_titles = html_wine.find_all('div', class_='product-details__component-container')

# Div containing wine info
wine_info = html_wine.find_all(
    'ul', class_='product-attributes__ul list-unstyled')

# Lists to store scraped data
names = []
colours = []
prices = []
notes = []
shops = []

# Extract data from wine titles and print
for title in wine_titles:

    # Wine names
    name = title.h1.text
    names.append(name)
    print(names)

    # Wine prices
    price = title.li.text[5:].strip()
    price_sterling = "£" + price
    print(price_sterling)

for info in wine_info:
    # colour
    colour = info.select('li')[2].text[10:].strip()
    colours.append(colour)
    print(colour)

    # Wine notes
    note = info.select('li')[1].text[6:].strip()
    notes.append(note)
    print(note)
