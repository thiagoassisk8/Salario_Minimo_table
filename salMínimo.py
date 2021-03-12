import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

html = urlopen('http://www.fetapergs.org.br/index.php/2015-07-27-16-46-22/tabelas-salario-minimo')


soup = BeautifulSoup(html, "html.parser")
tabela = soup.find("div", {"class":"t3-component"})
todos_trs = tabela.findAll("tr")

dados = []
PrimeiraTabela = []

 
for tr in todos_trs:
    td = tr.find_all('td')
    row = [d.text.strip() for d in td]
    
     
    if row:
     dados.append(row)
      
for i in range(1,26):
   PrimeiraTabela.append(dados[i])


df = pd.DataFrame(PrimeiraTabela,columns=['Ano',"Salário Mínimo", "Salário Referência", "Reajuste Salário Mínimo","Reajuste Beneficio Acima SM",'Teto Máximo de Contribuição','Vigência'])
df.to_csv("Salário Mínimo 2000 a 2021.csv", index=False, encoding='utf8')
print('CSV concluído')


