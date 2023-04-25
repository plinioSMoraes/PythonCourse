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

os.system('clear')
