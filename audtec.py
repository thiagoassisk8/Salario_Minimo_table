import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

html = urlopen("https://audtecgestao.com.br/"
               "capa.asp?infoid=1336")

soup = BeautifulSoup(html, "html.parser")
tabela = soup.find("div", {"class":"pagina"})
todos_trs = tabela.findAll("tr")

periodo_desejado = []
dados = []

for numero in range(104,len(todos_trs)):  
   trs_filtrados = todos_trs[numero]
   periodo_desejado.append(trs_filtrados)

for tr in periodo_desejado:
    td = tr.find_all('td')
    row = [d.text.strip() for d in td]
    
    if row:
     dados.append(row)
     
df = pd.DataFrame(dados, columns=["Vigência", "Dispositivo legal", "Valor"])
df.to_csv("Salário Mínimo.csv", index=False, encoding='utf8')



