import requests
from pprint import pprint
from bs4 import BeautifulSoup
import lxml

for n in range(1, 51):
    # Visita cada página das palavras mais buscadas e faz uma lista das palavras
    URL = f"https://www.dicio.com.br/palavras-mais-buscadas/{n}/"
    response = requests.get(URL)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    lista = soup.select(".list li a")

    for word in lista:
        # Acessa cada palavra na lista e extrai o seu significado
        href = f"""https://www.dicio.com.br{word.get("href")}"""
        response2 = requests.get(href)
        html2 = response2.text
        soup2 = BeautifulSoup(html2, "html.parser")
        palavra = word.getText().strip()
        significado = soup2.select("p span")[1].getText()

        # Registra a palavra e o seu significado no arquivo csv
        with open('palavras.csv', 'a', encoding='utf-8') as file:
            file.write(f""""{palavra}","{significado}"\n""")

