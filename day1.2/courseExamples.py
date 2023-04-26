import os
import json  # json é um modulo que vem embutido, porém precisamos importá-lo
import csv # csv é um modulo que vem embutido, porem precisamos importa-lo

os.system('clear') # Limpa a tela pa nois

# Faça um programa que solicite o nome de uma pessoa usuária e imprima-o na vertical. Exemplo:
def columnName():
    os.system('clear')
    name = input('Digite seu nome: ')
    for char in name:
        print(char)
#----------------------------------------------------------------------------------------------------

# Escreva um programa que receba vários números naturais e calcule a soma desses valores.
def infiniteSum():
    os.system('clear')
    print('Para sair digite SAIR')
    numArr = input('Digite quantos numeros desejar: ').split()
    sum = 0
    for num in numArr:
        sum += int(num)
    print(sum)

#----------------------------------------------------------------------------------------------------

# Dado um arquivo contendo estudantes e suas respectivas notas, escreva um programa que:
# lê todas essas informações;
# aplique um filtro, mantendo somente as pessoas que estão reprovadas;
# escreva seus nomes em outro arquivo.
# Considere que a nota miníma para aprovação é 6.
def filterStudents():
    os.system('clear')
    gradeToPass = 6
    filteredStud = {}
    file = open('students.txt', mode="r")
    studentList = file.read().split('\n')
    for student in studentList:
        studentInfo = student.split(' ')
        studentName = studentInfo[0]
        studentGrade = studentInfo[1] # Pega a nota do array
        if (int(studentGrade) >= gradeToPass):
            filteredStud[studentName] = studentGrade
    print((filteredStud))


# Exemplo de como trabalhar com arquivos json e csv no python
def howToUseJSON():
    with open("pokemons.json") as file:
        content = file.read()  # leitura do arquivo
        pokemons = json.loads(content)["results"]  # o conteúdo é transformado em estrutura python equivalente, dicionário neste caso.
        # acessamos a chave results que é onde contém nossa lista de pokemons
    print(pokemons[0])  # imprime o primeiro pokemon da lista

def howToUseCSV():
    with open("graduacao_unb.csv", encoding = "utf-8") as file:
        graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')
        # Usando o conceito de desempacotamento
        header, *data = graduacao_reader

    print(data)

