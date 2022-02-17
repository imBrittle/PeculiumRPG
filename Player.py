import random
import time
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, name, max_hp, damage, scroll):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage
        self.start_scroll = scroll
        self.scroll = scroll
        self.isAlive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0 # 0:Idle, 1:Moving, 2:Climbing, 3:Attack, 4:Hurt, 5:Dead
        self.update_time = pygame.time.get_ticks()
        self.position = (x, y)

        # Movement
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0 # Move X Axis
        self.movey = 0 # Move Y Axis
        self.frame = 0 # Frame Count

    def control(self,x,y):
        self.movex += x
        self.movey += y

    def update(self):
        self.rect.x += self.movex
        self.rect.y += self.movey

