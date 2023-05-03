import os
os.system("clear")

def is_odd(number):
    'Retorna True se um número é ímpar, senão False.'
    return number % 2 != 0

def divide(a_number, other_number):
    "Retorna a divisão de a_number por other_number"
    return a_number / other_number

def get_most_ordered_dish_per_costumer(orders, customer):
    max_amount = 0
    most_ordered = ""
    customer_dishes = {}

    for order in orders:
        if order["customer"] == customer:
            customer_dishes[order["order"]] = (
                customer_dishes.get(order["order"], 0) + 1
            )
            if customer_dishes[order["order"]] >= max_amount:
                max_amount = customer_dishes[order["order"]]
                most_ordered = order["order"]
    return most_ordered


def get_order_frequency_per_costumer(orders, customer, order):
    counter = 0
    for current_order in orders:
        if (
            current_order["customer"] == customer
            and current_order["order"] == order
        ):
            counter += 1
    return counter


# Exercício 1: Escreva um programa que retorne uma lista com os valores numéricos de 1 a N, mas com as seguintes exceções:
# Números divisíveis por 3 deve aparecer como “Fizz” ao invés do número;
# Números divisíveis por 5 devem aparecer como “Buzz” ao invés do número;
# Números divisíveis por 3 e 5 devem aparecer como “FizzBuzz” ao invés do número.
# Exemplo: 3 -> [1, 2, "Fizz"].

def fizzBuzz(num):
    iterator = 1
    fizzBuzzList = []
    while(iterator <= num):
        #if (iterator % 3 == 0 and iterator % 5 == 0):
        #    fizzBuzzList[iterator] = "FizzBuzz" 
        #elif (iterator % 3 == 0):
        #    fizzBuzzList[iterator] = "Fizz" 
        #elif (iterator % 5 == 0):
        #    fizzBuzzList[iterator] = "Buzz" 
        #iterator += 1
        if (iterator % 3 == 0 and iterator % 5 == 0):
            fizzBuzzList.append("FizzBuzz")  
        elif (iterator % 3 == 0):
            fizzBuzzList.append("Fizz")  
        elif (iterator % 5 == 0):
            fizzBuzzList.append("Buzz")  
        else:
            fizzBuzzList.append(iterator)
        iterator += 1
    return fizzBuzzList


# Exercício 2: Em alguns lugares é comum lembrar um número do telefone associando seus 
# dígitos a letras. Dessa maneira, a expressão MY LOVE significa 69 5683. Claro que 
# existem alguns problemas, uma vez que alguns números de telefone não formam uma palavra
# ou uma frase, e os dígitos 1 e 0 não estão associados a nenhuma letra.

# Sua tarefa é ler uma expressão e encontrar o número de telefone correspondente baseado
# na tabela abaixo. Uma expressão é composta por letras maiúsculas (A-Z), hifens (-) e os números 1 e 0.
# Letras  ->  Número
# ABC     ->  2
# DEF     ->  3
# GHI     ->  4
# JKL     ->  5
# MNO     ->  6
# PQRS    ->  7
# TUV     ->  8
# WXYZ    ->  9
# EXEMPLO
# 1-HOME-SWEET-HOME
# MY-MISERABLE-JOB
# 1-4663-79338-4663
# 69-647372253-562

def getPhoneNum(string):
    translate = { 
        "A": "2", "B": "2", "C": "2", 
        "D": "3", "E": "3", "F": "3",
        "G": "4", "H": "4", "I": "4",
        "J": "5", "K": "5", "L": "5",
        "M": "6", "N": "6", "O": "6",
        "P": "7", "Q": "7", "R": "7", "S": "7",
        "T": "8", "U": "8", "V": "8",
        "W": "9", "X": "9", "Y": "9", "Z": "9",
        " ": " ", "-": "-"
    }
    highCaseString = string.upper()
    translatedString = ''
    for char in highCaseString:
        translatedString += translate[char]
    print(translatedString)
getPhoneNum('-OLA-Ei-so-pgdsagdsag')