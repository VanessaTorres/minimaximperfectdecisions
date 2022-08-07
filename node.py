class Node:
    def __str__(self):
        return "{0},{1}".format(self.x, self.y)
    
    def __repr__(self) -> str:
        return f'({self.position[0]},{self.position[1]})'

    def __init__(self, position,father,profundidad=0,move=''):
        self.position = position
        self.father = father
        self.profundidad = profundidad
        self.direccion = move