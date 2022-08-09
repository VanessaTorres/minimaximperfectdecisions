"""
Gana el juego quién obtenga más puntos
primero miramos si ya no quedan objetos disponibles (estado terminal del juego)
y luego realizamos las comparaciones para los puntajes

"""
from node import Node

def utility_function(objects_remaining,pmin,pmax):
    if not objects_remaining:
        if pmin.score>pmax.score:
            return pmin
        else:
            return pmax
    else:
        return 0

def minimax(position,board,depth,max_player):
    if depth == 0:
        return position.evaluate().position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None

        for move in get_all_moves(position,game):
            pass


    else:
        pass


def get_all_moves(position,game):
    pass 
    # miramos las posiciones circundantes al elemento de interés

def amplitud(position):
        nodes = []
        initial_node = Node(position,None)
        nodes.append(initial_node)
        solucionado = False
        while not solucionado:
            if not nodes:
                raise AttributeError #Fallo
            n = nodes.pop(0)
            bandera = False
        #valida si estamos en un nodo meta y ya pasamos por el otro... de la forma como esta solo funciona con dos metas
            if( n.position == self.goal_position[0] and self.goal_position[1] in n.get_fathers_positions()  ):
                bandera = True
            if( n.position == self.goal_position[1] and self.goal_position[0] in n.get_fathers_positions()  ):
                bandera = True

            if  bandera:
                solucionado = True
                return self.show_route(n.get_fathers())
            else:
                self.expanded_nodes.append(n)
                if (n.can_move_amplitud(self.data, 'right', n.position in self.goal_position  )):
                    nodes.append(n.make_child_node('right'))
                if (n.can_move_amplitud(self.data, 'up' , n.position in self.goal_position)):
                    nodes.append(n.make_child_node('up'))
                if (n.can_move_amplitud(self.data, 'left' , n.position in self.goal_position)):
                    nodes.append(n.make_child_node('left'))
                if (n.can_move_amplitud(self.data, 'down' , n.position in self.goal_position )):
                    nodes.append(n.make_child_node('down'))