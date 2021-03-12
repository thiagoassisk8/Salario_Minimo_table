import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

html = urlopen("http://www.guiatrabalhista.com.br/"
               "guia/salario_minimo.htm")

soup = BeautifulSoup(html, "html.parser")
tabela = soup.find("table", {"class":"MsoNormalTable"})
todos_trs = tabela.findAll("tr")


dados = []
dadosfitrados = []

for numero in range(1,4):  
   trs_filtrados = todos_trs[numero]
   dadosfitrados.append(trs_filtrados)


for tr in dadosfitrados:
    td = tr.find_all('td')
    row = [d.text.strip() for d in td]
    
    if row:
     dados.append(row)
     
df = pd.DataFrame(dados, columns=["Vigência", "Valor Mensal", "Valor Diário","Valor Hora",'Norma Legal'])
df.to_csv("Salário Mínimo ultimos anos.csv", index=False, encoding='utf8')



