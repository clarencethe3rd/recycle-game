import pygame
import random
from pygame.locals import *
import time 
pygame.init()
plastic_count = 0 
paper_bag = 0
playing = True 
score = 0
clock = pygame.time.Clock()
start_time = time.time()-1
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
        self.image = pygame.transform.scale(self.image,(20,40))
        self.rect = self.image.get_rect()
        
class Non_Recycle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/plasticbag.png")
        self.image = pygame.transform.scale(self.image,(20,40))
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
    plastic_list.add(plastic)
    allsprites.add(plastic)

bin = Bin()
allsprites.add(bin)
while playing == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    timeElapsed= time.time()-start_time
    screen.blit(bg,(0,0))
    text = font.render("time left: "+str(20-int(timeElapsed)),True, "Black")
    screen.blit(text,(30,30))
    if game_over == False:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if bin.rect.y > 0:
                bin.rect.y -= 1.5
        if keys[pygame.K_s]:
            if bin.rect.y < 650:
                bin.rect.y += 1.5
        if keys[pygame.K_d]:
            if bin.rect.x < 850:
                bin.rect.x += 1.5
        if keys[pygame.K_a]:
            if bin.rect.x > 0:
                bin.rect.x -= 1.5   
    allsprites.draw(screen)
    item_hit_list = pygame.sprite.spritecollide(bin,item_list,True)
    plastic_hit_list = pygame.sprite.spritecollide(bin,plastic_list,True)    
    for i in item_hit_list:
        score += 1
        paper_bag += 1
    for i in plastic_hit_list:
        plastic_count += 1
        
    text=font. render ("score "+str(paper_bag-plastic_count), True, (0,0,0))
    screen.blit(text,(305,60))
    if timeElapsed >20:
        
        game_over = True
        screen.fill("white")
        text3=font. render ("final score "+str(paper_bag-plastic_count), True, (0,0,0))
        text1=font. render ("plastic bag collected "+str(plastic_count), True, (0,0,0))
        text2=font. render ("paper bag collected "+str(paper_bag), True, (0,0,0))
        screen.blit(text3,(305,60))
        screen.blit(text1,(305,90))
        screen.blit(text2,(305,120))
    pygame.display.update()
