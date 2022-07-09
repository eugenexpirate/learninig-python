from prettytable import PrettyTable
import requests
from lxml import etree
import lxml.html

# table = PrettyTable()
# table.add_column("Name", list())
# table.add_column("Type", list())
# print(table)

url = "https://pokemondb.net/pokedex/game/x-y"


api = requests.get(url)
tree = lxml.html.document_fromstring(api.text)

text = tree.text_content()
text_list = list(text.splitlines())

name_list, type_list = [], []

for element in text_list:
    if '#0' in element or '#1' in element or '#2' in element:
        words = element.split()
        l = len(words)
        if l == 3:
            type_list.append(words[2])
        elif l == 5:
            type_list.append(words[2] + " " + words[4])
        elif l == 6:
            type_list.append(words[3] + " " + words[5])
            name_list.append(words[1] + " " + words[2])
            continue
        
        name_list.append(words[1])

print(len(name_list))
print(len(type_list))


table = PrettyTable()
table.add_column("Name", name_list)
table.add_column("Type", type_list)
print(table)

