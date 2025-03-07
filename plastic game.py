import pygame
import random
from pygame.locals import *
import time 
pygame.init()
playing = True 
score = 0
clock = pygame.time.Clock()
start_time = time.time()
font=pygame. font.SysFont ("Times New Roman", 36) 
game_over = False
screen = pygame.display.set_mode((900,700))
back = pygame.image.load("assets/enviroment_back.png")
bg = pygame.transform.scale(back,(900,700)) 
class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/bin.png")
        self.image = pygame.transform.scale(self.image,(40,60))
        self.rect = self.image.get_rect()
        
class Recycle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/item1.png")
        self.image = pygame.transform.scale(self.image,(10,20))
        self.rect = self.image.get_rect()
        
class Non_Recycle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/plastic bag.png")
        self.image = pygame.transform.scale(self.image,(10,20))
        self.rect = self.image.get_rect()

item_list = pygame.sprite.Group()
allsprites = pygame.sprite.Group()
plastic_list = pygame.sprite.Group()
for i in range(50):
    item = Recycle()
    item.rect.x = random.randint(50,850)
    item.rect.y = random.randint(50,650)
    item_list.add(item)
    allsprites.add(item)
    
for i in range(20):
    plastic = Non_Recycle()
    plastic.rect.x = random.randint(50,850)
    plastic.rect.y = random.randint(50,650)
    plastic_list.add(item)
    allsprites.add(item)

bin = Bin()
allsprites.add(bin)
while playing == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    timeElapsed= time.time()-start_time
    screen.blit(bg,(0,0))
    text = font.render("time left: "+str(60-int(timeElapsed)),True, "Black")
    screen.blit(text,(30,30))
    
    
    pygame.display.update()