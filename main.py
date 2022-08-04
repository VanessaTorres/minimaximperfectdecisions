import pygame
import sys
import random
from board import generate_board
from objects import Min,Max,Grass,Apples,Flower

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

board = generate_board()


global player_Min, player_Max
player_Min = Min()
player_Max = Max()


while 1:
    a = random.randint(0,6)
    b = random.randint(0,6)

    if board[a][b]=='':
        board[a][b] = player_Min
        
        break
while 1:
    a = random.randint(0,6)
    b = random.randint(0,6)

    if board[a][b]=='':
        board[a][b] = player_Max
        
        break




# function for drawing our grid
def drawGrid():
    blocksize = 62
    for x in range (0,500,blocksize):
        for y in range (0,500,blocksize):
            rect = pygame.Rect(x,y,blocksize,blocksize)
            pygame.draw.rect(screen,WHITE,rect,1)


objects_sprites = pygame.sprite.Group()

def fillGrid():
    
    global all_sprites
    all_sprites = pygame.sprite.Group()
    rows = len(board)
    cols = len(board[0])
    font = pygame.font.Font.bold
    global max_h, min_h
    for x in range(rows):
        for y in range(rows):
            if board[x][y] != '':
                board[x][y].rect.x = 62*x
                board[x][y].rect.y = 62*y
                all_sprites.add(board[x][y])
                if not isinstance(board[x][y],Max) and not isinstance(board[x][y], Min):
                    objects_sprites.add(board[x][y])



def isvalid_move(x,y):
    if x>=0 and x<=6:
        if y>=0 and y<=6:
            return True
    return False
                
puntuacion = {
    'Grass' : 1,
    'Apples' : 5,
    'Flower': 3
}
    
    
clock = pygame.time.Clock()
fillGrid()
objects_remaining = 21 # not including players
font = pygame.font.SysFont("monospace", 20)

while 1:
    text = font.render(str(f"Max score  -> {player_Max.score}"),True,WHITE)
    
   

    if objects_remaining == 0:
        break
    
    drawGrid()
    
    print(player_Max.rect.x//62,player_Max.rect.y//62)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN:
               player_Max.update("down")
               collided_object = pygame.sprite.spritecollideany(player_Max,objects_sprites)


               if collided_object != None:
                    puntos = puntuacion[type(collided_object).__name__]
                    player_Max.score += puntos
                    
                    collided_object.kill()
                    objects_remaining -= 1
                
              
                
               
            elif event.key == pygame.K_UP:
                player_Max.update("up")

                collided_object = pygame.sprite.spritecollideany(player_Max,objects_sprites)


                if collided_object != None:
                    puntos = puntuacion[type(collided_object).__name__]
                    player_Max.score += puntos
                    
                    collided_object.kill()
                    objects_remaining -= 1
                
                
                
            elif event.key == pygame.K_LEFT:
                player_Max.update("left")

                collided_object = pygame.sprite.spritecollideany(player_Max,objects_sprites)


                if collided_object != None:
                    puntos = puntuacion[type(collided_object).__name__]
                    player_Max.score += puntos
                    
                    collided_object.kill()
                    objects_remaining -= 1
                
               
            elif event.key == pygame.K_RIGHT:
                player_Max.update("right")
                collided_object = pygame.sprite.spritecollideany(player_Max,objects_sprites)


                if collided_object != None:
                    puntos = puntuacion[type(collided_object).__name__]
                    player_Max.score += puntos
                    
                    collided_object.kill()
                    objects_remaining -= 1
                
               
    
    pygame.display.update()
    pygame.display.flip()
    screen.fill(0)
    screen.blit(text,(0,570))
   
    
    all_sprites.draw(screen)
   
    clock.tick(60)