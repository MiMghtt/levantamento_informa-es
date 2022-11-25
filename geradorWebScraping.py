
#pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

#objeto site está recebedo o conteudo da requisição http do site
site = requests.get('https://github.com/MiMghtt?tab=repositories').content
#objeto soup está baixando do site o html
soup = BeautifulSoup(site, 'html.parser')

#prettify transforma o html em string
print(soup.prettify())

print(soup.title.string)

print(soup.find('admin'))

