# 🚀 Exercício 1: Crie uma função que receba dois números e retorne o maior deles.
def biggerNum(numA, numB):
    if numA > numB:
        return (str(numA) + " is greater than " + str(numB))
    if numB > numA:
        return (str(numB) + " is greater than " + str(numA))
    return 'They are equals'

# print(biggerNum(2, 2))
# print(biggerNum(3, 4))

#----------------------------------------------------------------------------------------

#🚀 Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.
def listAverage(itemList):
    itemAverage = sum(itemList, 0) / len(itemList)
    return itemAverage

# print(listAverage([2, 3, 5, 1, 10, 25]))

#----------------------------------------------------------------------------------------

# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1, 
# imprima na tela um quadrado feito de asteriscos de lado de tamanho n. Por exemplo:
def squarePrint(squareSize):
    count = squareSize
    starString = '*' * squareSize
    while (count > 0):
        print(starString)
        count -= 1

# squarePrint(5)
#----------------------------------------------------------------------------------------

#🚀 Exercício 4: Crie uma função que receba uma lista de nomes e retorne o
# nome com a maior quantidade de caracteres. Por exemplo, para 
# ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"], o retorno deve ser "Fernanda".

def biggerName(namesList):
    biggestName = ''
    for name in namesList:
        if len(name) > len(biggestName):
            biggestName = name
    return biggestName

# print(biggerName(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]))
#----------------------------------------------------------------------------------------

# Exercício 5: Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Crie uma função que retorne
#  dois valores em uma tupla contendo a quantidade de 
# latas de tinta a serem compradas e o preço total a partir do tamanho de uma parede (em m²).

def totalPaintWallPrice(squareMeters):
    squareMeterPerLiter = 3
    literPerCan = 18
    pricePerCan = 80.00
    squareMeterPerCan = literPerCan * squareMeterPerLiter
    totalOfCans = squareMeters / squareMeterPerCan
    totalPrice = totalOfCans * pricePerCan
    return [totalOfCans, totalPrice]

#print(totalPaintWallPrice(130))
#----------------------------------------------------------------------------------------

# Exercício 6: Crie uma função que receba os três lado de um triângulo e 
# informe qual o tipo de triângulo formado ou "não é triangulo", caso não seja possível formar um triângulo.


def isTriangle(sideA, sideB, sideC):
    if (sideA == sideB and sideB == sideC):
        return 'Triangulo Equilatero'
    if (sideA == sideB or sideB == sideC or sideC == sideA):
        return 'Triangulo Isósceles'
    if (sideA != sideB and sideB != sideC and sideA != sideC):
        return 'Triangulo Escaleno'
    return 'Nao é um triangulo'

# print(isTriangle(3,2,1))
#----------------------------------------------------------------------------------------
