import requests
from bs4 import BeautifulSoup
import csv

url = 'http://www.obt.inpe.br/OBT/assuntos/programas/amazonia/prodes'

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table')

target_table = None

for table in tables:
    previous_element = table.find_previous_sibling()
    while previous_element and previous_element.name != 'h3':
        previous_element = previous_element.find_previous_sibling()
    if previous_element and 'Taxas PRODES Amazônia - 1988 a 2024' in previous_element.get_text():
        target_table = table
        break

if not target_table:
    print("Tabela não encontrada na página.")
    exit()

data = []
rows = target_table.find_all('tr')
for row in rows:
    cols = row.find_all(['td', 'th'])
    cols = [ele.get_text(strip=True) for ele in cols]
    data.append(cols)

with open('taxas_prodes_amazonia_1988_2024.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Arquivo CSV 'taxas_prodes_amazonia_1988_2024.csv' criado com sucesso.")
