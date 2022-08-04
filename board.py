import random

from objects import Flower,Grass,Apples,Max,Min

def generate_board():
    """
    Function that generates a matrix which contains a str representation for each game object
    grass -> '0'
    blankspaces -> ''
    apples -> '*'
    flowers -> '-'
    max -> m
    min -> h

    """
    matrix = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append('')
        matrix.append(row)

    f_count = 0
    while f_count < 5:
        a = random.randint(0,6)
        b = random.randint(0,6)
        if matrix[a][b] == '':
            matrix[a][b] = Flower()
            f_count+=1


    a_count=0
    while a_count < 2:
        a = random.randint(0,6)
        b = random.randint(0,6)
        if matrix[a][b] == '':
            matrix[a][b] = Apples()
            a_count+=1


    g_count = 0
    while g_count < 14:
        a = random.randint(0,6)
        b = random.randint(0,6)
        if matrix[a][b] == '':
            matrix[a][b] = Grass()
            g_count+=1



    with open('board.txt','w') as file:
        for row in matrix:
            print(row,file=file)

    return matrix
    
        

