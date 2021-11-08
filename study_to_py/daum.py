
import requests
from bs4 import BeautifulSoup as bs

resp = requests.get('https://daum.net')

html = resp.text

soup = bs(html,'html.parser')

len(soup.select('ul'))

len(soup.select('li'))

result = soup.select('.list_favorsch a')

for item in result:
    print(item.text)
    

