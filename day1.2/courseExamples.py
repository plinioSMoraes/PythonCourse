import os

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