import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Bullet(Sprite):
	def __init__(self, pos, dire):
		Sprite.__init__(self)
		
		if dire==0:
			self.vel = [-2,0]	
		elif dire==1:
			self.vel = [0,-2]
		elif dire==2:
			self.vel = [2,0]		
		elif dire==3:
			self.vel = [0,2]

		self.image = pygame.image.load("imagenes/bullet.png")
		self.rect = self.image.get_rect()
		self.rect.move_ip(pos[0], pos[1])

	def update(self):
		self.rect = self.rect.move(self.vel)
