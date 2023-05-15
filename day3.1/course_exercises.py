from parsel import Selector
import requests


# Exercício 1:
# Faça uma requisição ao site https://httpbin.org/encoding/utf8 e
# exiba seu conteúdo de forma legível.
#response = requests.get("https://httpbin.org/encoding/utf8")
#print(response.text)

# ---------------------------------------------------------------

# Exercício 2:
# Faça uma requisição ao recurso usuários da API do Github (https://api.github.com/users), 
# exibindo o username e url de todos os usuários retornados.
URL = "https://api.github.com/users"
users = requests.get(URL).json()
for user in users:
    print(f"{user['login']} - https://api.github.com/users/{user['login']}")