"""
Gana el juego quién obtenga más puntos
primero miramos si ya no quedan objetos disponibles (estado terminal del juego)
y luego realizamos las comparaciones para los puntajes

"""


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
