# 🚀 Exercício 1: Crie uma função que receba dois números e retorne o maior deles.
def biggerNum(numA, numB):
    if numA > numB:
        return (str(numA) + " is greater than " + str(numB))
    if numB > numA:
        return (str(numB) + " is greater than " + str(numA))
    return 'They are equals'

# print(biggerNum(2, 2))
# print(biggerNum(3, 4))

#🚀 Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.
def listAverage(itemList):
    itemAverage = sum(itemList, 0) / len(itemList)
    return itemAverage

# print(listAverage([2, 3, 5, 1, 10, 25]))

# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1, 
# imprima na tela um quadrado feito de asteriscos de lado de tamanho n. Por exemplo:
def squarePrint(squareSize):
    count = squareSize
    starString = '*' * squareSize
    while (count > 0):
        print(starString)
        count -= 1

squarePrint(5)