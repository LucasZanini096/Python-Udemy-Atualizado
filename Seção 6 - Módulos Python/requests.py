# requests para requisisções HTTP
import requests 

#http:// -> 80 (Porta padrão do http)
#https:// -> 443 (Porta padrão do https)

url = "http://localhost:8080/"
response = requests.get(url)

print(response.status_code)
print(response.headers)
print(response.content) #Traz o conteúdo em bits
print(response.text) #Traz o conteúdo da página em sua linguagem nativa (ex: HTML)
