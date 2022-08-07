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

    for i in range(8):
        row = []
        for j in range(8):
            row.append('')
        matrix.append(row)

    matrix[3][1] = Flower(3, 1)
    matrix[5][0] = Flower(5, 0)
    matrix[7][3] = Flower(7, 3)
    matrix[4][5] = Flower(4, 5)
    matrix[1][6] = Flower(1, 6)

    matrix[4][3] = Apples(4, 3)
    matrix[5][6] = Apples(5, 6)

    matrix[3][0] = Grass(3, 0)
    matrix[7][0] = Grass(7, 0)
    matrix[1][1] = Grass(1, 1)
    matrix[5][1] = Grass(5, 1)
    matrix[0][2] = Grass(0, 2)
    matrix[1][3] = Grass(1, 3)
    matrix[0][4] = Grass(0, 4)
    matrix[4][4] = Grass(4, 4)
    matrix[6][4] = Grass(6, 4)
    matrix[0][5] = Grass(0, 5)
    matrix[7][5] = Grass(7, 5)
    matrix[2][6] = Grass(2, 6)
    matrix[1][7] = Grass(1, 7)
    matrix[6][7] = Grass(6, 7)
    """ 
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
            g_count+=1"""

    with open('board.txt', 'w') as file:
        for row in matrix:
            print(row, file=file)

    return matrix






