import os
import json
import csv
os.system('clear')

# Faça um programa que receba um nome e imprima o mesmo na vertical em escada invertida. Exemplo: Entrada:

def ladderName():
    name = input('Entre com seu nome: ')
    size = len(name)
    while (size > 0):
        print(name)
        trimmedName = name.strip(name[-1])
        name = trimmedName
        size -= 1

# Dado o seguinte arquivo no formato JSON, leia seu conteúdo e calcule a porcentagem de 
# livros em cada categoria em relação ao número total de livros. O resultado deve 
# ser escrito em um arquivo no formato CSV como o exemplo abaixo.
def booksPercentage():
    booksQuantity = 0
    booksQuantityCategory = { "Python": 0, "Java": 0, "Php": 0}
    with open("books.json") as file:
        content = file.read()
        books = json.loads(content)
    for book in books:
        for category in book["categories"]:
            booksQuantity += 1
            if (booksQuantityCategory.get(category) != None):
                booksQuantityCategory[category] += 1
    booksQuantityCategory["Python"] /= booksQuantity
    booksQuantityCategory["Java"] /= booksQuantity
    booksQuantityCategory["Php"] /= booksQuantity

    entries_list = list(booksQuantityCategory.items())
    with open("booksPercentage.csv", "w", encoding = "utf-8") as file:
        writer = csv.writer(file)
        headers = [
            "Categoria",
            "Porcentagem",
        ]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

        for categoria, porcentagem in entries_list:
            row = {"Categoria": categoria, "Porcentagem": porcentagem}
            writer.writerow(row)

booksPercentage()