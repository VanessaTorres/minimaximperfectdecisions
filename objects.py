import pygame

class Flower(pygame.sprite.Sprite):
    points = 3
    def __init__(self,posix,posiy):
        self.x = posix
        self.y = posiy
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("icons/flower.png"),(62,62))      
        self.rect = self.image.get_rect()

    
class Grass(pygame.sprite.Sprite):
    points = 1
    def __init__(self,posix,posiy):
        self.x = posix
        self.y = posiy
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("icons/grass.png"),(62,62))
        self.rect = self.image.get_rect()


class Apples(pygame.sprite.Sprite):
    points = 5
    def __init__(self,posix,posiy):
        self.x = posix
        self.y = posiy
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("icons/apple.png"),(62,62))
        self.rect = self.image.get_rect()


class ValidMovement(pygame.sprite.Sprite):
    points = 1
    def __init__(self,posix,posiy):
        self.x = posix
        self.y = posiy
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("icons/location.png"),(62,62))
        self.rect = self.image.get_rect()


class Min(pygame.sprite.Sprite):
    score = 0

    def __init__(self,posix,posiy):
        self.x = posix
        self.y = posiy
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("icons/min.png"),(62,62))
        self.rect = self.image.get_rect()

    def update(self,direction):
        if direction == "down":
            self.rect.y+=62
        elif direction == "up":
            self.rect.y-=62
        elif direction == "right":
            self.rect.x+=62
        elif direction == "left":
            self.rect.x-=62
        
class Max(pygame.sprite.Sprite):
    score = 0

    def __init__(self,posix,posiy):
        self.x = posix
        self.y = posiy
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("icons/max.png"),(62,62))
        self.rect = self.image.get_rect()


    def update(self,position):

        """self.rect.x = position[0]*62
        self.rect.y = position[1]*62"""

        if(self.x  > position[0]):
            diferencia = self.x - position[0]
            for i in range(diferencia):
                self.rect.x -= 62

        if (self.x < position[0]):
            diferencia = position[0] - self.x
            for i in range(diferencia):
                self.rect.x += 62

        if (self.y > position[1]):
            diferencia = self.y - position[1]
            for i in range(diferencia):
                self.rect.y -= 62

        if (self.y < position[1]):
            diferencia = position[1] - self.y
            for i in range(diferencia):
                self.rect.y += 62

        self.x = position[0]
        self.y = position[1]

        """if direction == "down":
            self.rect.y+=62
        elif direction == "up":
            self.rect.y-=62
        elif direction == "right":
            self.rect.x+=62
        elif direction == "left":
            self.rect.x-=62"""

    def validmovements(self, x, y):
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
  

