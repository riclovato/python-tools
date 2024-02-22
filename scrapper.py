from bs4 import BeautifulSoup
import requests
#objeto site recebendo o centeudo da requisição http do site
site = requests.get("https://www.climatempo.com.br/").content
#objeto soup baixando do site o html
soup = BeautifulSoup(site, 'html.parser')

print(soup.prettify())

print(soup.title.string)