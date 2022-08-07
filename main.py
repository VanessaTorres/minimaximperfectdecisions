import pygame
import sys
import time
import random
from board import generate_board
from objects import Min,Max,Grass,Apples,Flower,ValidMovement

pygame.init()


# defining colors
WHITE = (200,200,200)



screen = pygame.display.set_mode([500,700])
clock = pygame.time.Clock()
 
# since our matrix is 8x8, each cell will be 62 pixels of h,w


"""
TODO
>>> Fill the screen with sprites (done)
"""


def validmovements(x, y):
    movements = []
    movements.append((x - 1, y - 2))
    movements.append((x - 1, y + 2))
    movements.append((x + 1, y - 2))
    movements.append((x + 1, y + 2))
    movements.append((x - 2, y - 1))
    movements.append((x - 2, y + 1))
    movements.append((x + 2, y - 1))
    movements.append((x + 2, y + 1))
    return movements

def isvalid_move(x,y):
    if x>=0 and x<=7:
        if y>=0 and y<=7:
            return True
    return False

def can_move(x,y,direction):
    movements = validmovements(x, y)
    position_down = []
    position_up = []
    position_right = []
    position_left = []
    for position in movements:
        if isvalid_move(position[0],position[1]):
            if direction == "down": # Y aumenta 2  & X disminuye o aumenta en 1
                y_down = y + 2
                x_down_1 = x + 1
                x_down_2 = x - 1
                #self.rect.y += 62
                if( (position[0] == x_down_1 or position[0] == x_down_2) and  y_down == position[1]):
                    position_down.append(position)
            elif direction == "up": # Y disminuye 2 & X disminuye o aumenta en 1
                #self.rect.y -= 62
                y_up = y - 2
                x_up_1 = x + 1
                x_up_2 = x - 1
                if ((position[0] == x_up_1 or position[0] == x_up_2) and y_up == position[1]):
                    position_up.append(position)

            elif direction == "right": # x aumenta 2 & Y disminuye o aumenta en 1
                #self.rect.x += 62
                x_right = x + 2
                y_right_1 = y + 1
                y_right_2 = y - 1
                if ( x_right == position[0] and (position[1] == y_right_1 or position[1] == y_right_2)):
                    position_right.append(position)

            elif direction == "left": # x disminuye 2 & Y disminuye o aumenta en 1
                #self.rect.x -= 62
                x_left = x - 2
                y_left_1 = y + 1
                y_left_2 = y - 1
                if (x_left == position[0] and (position[1] == y_left_1 or position[1] == y_left_2)):
                    position_left.append(position)

    if direction == "down":
        return position_down
    elif direction == "up":
        return position_up
    elif direction == "right":
        return position_right
    elif direction == "left":
        return position_left
    #return False

board = generate_board()

global player_Min, player_Max, location
player_Min = Min(1, 2)
player_Max = Max(6, 0)
#location = ValidMovement()

board[6][0] = player_Max
movements_max = validmovements(6, 0)

print(movements_max)
for position in movements_max:
    if isvalid_move(position[0],position[1]) and board[position[0]][position[1]] == "":
        print("Ubicación max"+str(position))
        """board[position[0]][position[1]] = location"""

board[1][2] = player_Min
movements_min = validmovements(1, 2)
print(movements_min)
for position_min in movements_min:
    if isvalid_move(position_min[0], position_min[1]) and board[position_min[0]][position_min[1]] == "":
        print("Ubicación min" + str(position_min))
        """board[position_min[0]][position_min[1]] = location"""


for item in board:
    print(item)

"""while 1:
    a = random.randint(0,6)
    b = random.randint(0,6)

    if board[a][b]=='':
        board[a][b] = player_Min
        break"""
"""while 1:
    break
    a = random.randint(0,6)
    b = random.randint(0,6)

    if board[a][b]=='':
        board[a][b] = player_Max
    break"""


# function for drawing our grid
def drawGrid():
    blocksize = 62
    """for x in range(0, 500, blocksize):
        for y in range(0, 500, blocksize):
            rect = pygame.Rect(x, y, blocksize, blocksize)
            pygame.draw.rect(screen, WHITE, rect, 1)"""
    for y in range(8):
        for x in range(8):
            rect = pygame.Rect(x * (blocksize+1), y * (blocksize+1), blocksize, blocksize)
            pygame.draw.rect(screen, WHITE, rect,1)


objects_sprites = pygame.sprite.Group()

def fillGrid():

    global all_sprites
    blocksize = 62
    all_sprites = pygame.sprite.Group()
    rows = len(board)
    cols = len(board[0])
    font = pygame.font.Font.bold
    global max_h, min_h
    print("Listado de board")
    for x in range(8):
        for y in range(8):
            if board[x][y] != '':
                print(board[x][y])
                board[x][y].rect.x = 62 * x
                board[x][y].rect.y = 62 * y
                all_sprites.add(board[x][y])
                if not isinstance(board[x][y],Max) and not isinstance(board[x][y], Min):
                    objects_sprites.add(board[x][y])
    print("Listado de objetos:")
    for item in objects_sprites:
        print(item)
    print("Listado sprites")
    for item in all_sprites:
        print(item)

puntuacion = {
    'Grass' : 1,
    'Apples' : 5,
    'Flower': 3
}

clock = pygame.time.Clock()
fillGrid()
objects_remaining = 21 # not including players
font = pygame.font.SysFont("monospace", 20)
players = [player_Max,player_Min]
#El error propuesto
while 1:
    text = font.render(str(f"Max score  -> {player_Max.score}"  f"Min score  -> {player_Min.score}"),True,WHITE)

    if objects_remaining == 0:
        break

    drawGrid()

    ##print(player_Max.rect.x//62, player_Max.rect.y//62)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print("Capturo el evento")
            player = players[0]

            current_x = player.x
            current_y = player.y

            if event.key == pygame.K_DOWN: #aumenta en Y
               movements = can_move(player.x,player.y,"down")
               print("Posición"+str(player.x)+" "+str(player.y))
               print(movements)

               if(len(movements)>0):
                   available_movement =movements[0]

                   if (current_y > available_movement[1]):
                       diferencia = current_y - available_movement[1]
                       for i in range(diferencia):
                           #time.sleep(2)
                           player.rect.y -= 62
                           collided_object = pygame.sprite.spritecollideany(player, objects_sprites)
                           if collided_object != None:
                               puntos = puntuacion[type(collided_object).__name__]
                               player.score += puntos
                               collided_object.kill()
                               objects_remaining -= 1

                   if (current_y < available_movement[1]):
                       diferencia = available_movement[1] - current_y
                       for i in range(diferencia):
                           #time.sleep(2)
                           player.rect.y += 62
                           collided_object = pygame.sprite.spritecollideany(player, objects_sprites)
                           if collided_object != None:
                               puntos = puntuacion[type(collided_object).__name__]
                               player.score += puntos
                               collided_object.kill()
                               objects_remaining -= 1

                   time.sleep(1)

                   if (current_x > available_movement[0]):
                       diferencia = current_x - available_movement[0]
                       for i in range(diferencia):
                           #time.sleep(2)
                           player.rect.x -= 62
                           collided_object = pygame.sprite.spritecollideany(player, objects_sprites)
                           if collided_object != None:
                               puntos = puntuacion[type(collided_object).__name__]
                               player.score += puntos
                               collided_object.kill()
                               objects_remaining -= 1

                   if (current_x < available_movement[0]):
                       diferencia = available_movement[0] - current_x
                       for i in range(diferencia):
                           #time.sleep(2)
                           player.rect.x += 62
                           collided_object = pygame.sprite.spritecollideany(player, objects_sprites)
                           if collided_object != None:
                               puntos = puntuacion[type(collided_object).__name__]
                               player.score += puntos
                               collided_object.kill()
                               objects_remaining -= 1

                   player.x = available_movement[0]
                   player.y = available_movement[1]

            elif event.key == pygame.K_UP:
                movements = can_move(player.x, player.y, "up")
                print("Posición" + str(player.x) + " " + str(player.y))
                print(movements)
                if (len(movements) > 0):
                    available_movement = movements[0]

                    if (current_y > available_movement[1]):
                        diferencia = current_y - available_movement[1]
                        for i in range(diferencia):
                            # time.sleep(2)
                            player.rect.y -= 62
                            collided_object = pygame.sprite.spritecollideany(player, objects_sprites)
                            if collided_object != None:
                                puntos = puntuacion[type(collided_object).__name__]
                                player.score += puntos
                                collided_object.kill()
                                objects_remaining -= 1

                    if (current_y < available_movement[1]):
                        diferencia = available_movement[1] - current_y
                        for i in range(diferencia):
                            # time.sleep(2)
                            player.rect.y += 62
                            collided_object = pygame.sprite.spritecollideany(player, objects_sprites)
                            if collided_object != None:
                                puntos = puntuacion[type(collided_object).__name__]
                                player.score += puntos
                                collided_object.kill()
                                objects_remaining -= 1

                    time.sleep(1)

                    if (current_x > available_movement[0]):
                        diferencia = current_x - available_movement[0]
                        for i in range(diferencia):
                            # time.sleep(2)
                            player.rect.x -= 62
                            collided_object = pygame.sprite.spritecollideany(player, objects_sprites)
                            if collided_object != None:
                                puntos = puntuacion[type(collided_object).__name__]
                                player.score += puntos
                                collided_object.kill()
                                objects_remaining -= 1

                    if (current_x < available_movement[0]):
                        diferencia = available_movement[0] - current_x
                        for i in range(diferencia):
                            # time.sleep(2)
                            player.rect.x += 62
                            collided_object = pygame.sprite.spritecollideany(player, objects_sprites)
                            if collided_object != None:
                                puntos = puntuacion[type(collided_object).__name__]
                                player.score += puntos
                                collided_object.kill()
                                objects_remaining -= 1

                    player.x = available_movement[0]
                    player.y = available_movement[1]

            elif event.key == pygame.K_LEFT:
                movements = can_move(player.x, player.y, "left")
                print("Posición" + str(player.x) + " " + str(player.y))
                print(movements)
                if (len(movements) > 0):
                    available_movement = movements[0]

                    if (current_x > available_movement[0]):
                        diferencia = current_x - available_movement[0]
                        for i in range(diferencia):
                            # time.sleep(2)
                            player.rect.x -= 62
                            collided_object = pygame.sprite.spritecollideany(player, objects_sprites)
                            if collided_object != None:
                                puntos = puntuacion[type(collided_object).__name__]
                                player.score += puntos
                                collided_object.kill()
                                objects_remaining -= 1
                    if (current_x < available_movement[0]):
                        diferencia = available_movement[0] - current_x
                        for i in range(diferencia):
                            # time.sleep(2)
                            player.rect.x += 62
                            collided_object = pygame.sprite.spritecollideany(player, objects_sprites)
                            if collided_object != None:
                                puntos = puntuacion[type(collided_object).__name__]
                                player.score += puntos
                                collided_object.kill()
                                objects_remaining -= 1
                        time.sleep(1)

                    if (current_y > available_movement[1]):
                        diferencia = current_y - available_movement[1]
                        for i in range(diferencia):
                            # time.sleep(2)
                            player.rect.y -= 62
                            collided_object = pygame.sprite.spritecollideany(player, objects_sprites)
                            if collided_object != None:
                                puntos = puntuacion[type(collided_object).__name__]
                                player.score += puntos
                                collided_object.kill()
                                objects_remaining -= 1
                    if (current_y < available_movement[1]):
                        diferencia = available_movement[1] - current_y
                        for i in range(diferencia):
                            # time.sleep(2)
                            player.rect.y += 62
                            collided_object = pygame.sprite.spritecollideany(player, objects_sprites)
                            if collided_object != None:
                                puntos = puntuacion[type(collided_object).__name__]
                                player.score += puntos
                                collided_object.kill()
                                objects_remaining -= 1

                    player.x = available_movement[0]
                    player.y = available_movement[1]

            elif event.key == pygame.K_RIGHT:
                movements = can_move(player.x, player.y, "right")
                print("Posición" + str(player.x) + " " + str(player.y))
                print(movements)
                if (len(movements) > 0):
                    available_movement = movements[0]

                    if (current_x > available_movement[0]):
                        diferencia = current_x - available_movement[0]
                        for i in range(diferencia):
                            # time.sleep(2)
                            player.rect.x -= 62
                            collided_object = pygame.sprite.spritecollideany(player, objects_sprites)
                            if collided_object != None:
                                puntos = puntuacion[type(collided_object).__name__]
                                player.score += puntos
                                collided_object.kill()
                                objects_remaining -= 1
                    if (current_x < available_movement[0]):
                        diferencia = available_movement[0] - current_x
                        for i in range(diferencia):
                            # time.sleep(2)
                            player.rect.x += 62
                            collided_object = pygame.sprite.spritecollideany(player, objects_sprites)
                            if collided_object != None:
                                puntos = puntuacion[type(collided_object).__name__]
                                player.score += puntos
                                collided_object.kill()
                                objects_remaining -= 1
                        time.sleep(1)

                    if (current_y > available_movement[1]):
                        diferencia = current_y - available_movement[1]
                        for i in range(diferencia):
                            # time.sleep(2)
                            player.rect.y -= 62
                            collided_object = pygame.sprite.spritecollideany(player, objects_sprites)
                            if collided_object != None:
                                puntos = puntuacion[type(collided_object).__name__]
                                player.score += puntos
                                collided_object.kill()
                                objects_remaining -= 1
                    if (current_y < available_movement[1]):
                        diferencia = available_movement[1] - current_y
                        for i in range(diferencia):
                            # time.sleep(2)
                            player.rect.y += 62
                            collided_object = pygame.sprite.spritecollideany(player, objects_sprites)
                            if collided_object != None:
                                puntos = puntuacion[type(collided_object).__name__]
                                player.score += puntos
                                collided_object.kill()
                                objects_remaining -= 1

                    player.x = available_movement[0]
                    player.y = available_movement[1]

            elemt = players.pop(0)
            players.append(elemt)


    pygame.display.update()
    pygame.display.flip()
    screen.fill(0)
    screen.blit(text,(0,570))

    all_sprites.draw(screen)

    clock.tick(60)