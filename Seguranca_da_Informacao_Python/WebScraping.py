from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br/").content
##Recebendo o conteúdo da requisição http do site...
soup = BeautifulSoup(site, 'html.parser')
##Baixando do site o html dele
#print (soup.prettify())
##Transforma o html em string e exibe ele no terminal

temperatura = soup.find("span", class_="_flex _align-center -gray shimmer-placeholder -text")

print(temperatura.string)