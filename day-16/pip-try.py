from bs4 import BeautifulSoup
from prettytable import PrettyTable
import requests
from lxml import etree
import lxml.html

# table = PrettyTable()
# table.add_column("Name", list())  
# table.add_column("Type", list())
# print(table)

url = "https://pokemondb.net/pokedex/game/x-y"


# api = requests.get(url)
# tree = lxml.html.document_fromstring(api.text)

# text = tree.text_content()
# text_list = list(text.splitlines())

name_list, type_list, link_list = [], [], []

api = requests.get(url)
content = api.text

soup = BeautifulSoup(content, 'lxml')

location_box = soup.find('div', class_="infocard-list infocard-list-pkmn-lg")
infocards = location_box.find_all('div', class_ = "infocard")
for card in infocards:
    name_list.append(card.find('a', class_='ent-name').get_text())
    type_text = ""
    types = card.find_all('small')[1].find_all('a')
    for type in types:
        type_text += type.get_text() + " "
    type_list.append(type_text.strip())
    link_list.append("https://pokemondb.net" + card.find('a', href=True)['href'])

table = PrettyTable()
table.add_column("Name", name_list)
table.add_column("Type", type_list)
table.add_column("Link", link_list)
print(table)

