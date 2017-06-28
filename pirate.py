import pygame
from random import randint
from pygame.sprite import Sprite
from pygame.locals import *


class Pirate(Sprite):
	def __init__(self, cont_size, limitV):
		Sprite.__init__(self)
		self.vel = [randint(-1*limitV, limitV),randint(-1*limitV, limitV)]
		self.cont_size = cont_size
		imagen=randint(0, 4);
		if imagen==0:
			self.image = pygame.image.load("imagenes/pi1.png")
			pos_x = 200
			pos_y = 200
		if imagen==1:
			self.image = pygame.image.load("imagenes/pi2.png")
			pos_x = cont_size[0] - 200
			pos_y = 200
		if imagen==2:
			pos_x = 200
			pos_y = 200
			self.image = pygame.image.load("imagenes/pi3.png")
		if imagen==3:
			pos_x = 200
			pos_y = cont_size[1] - 200
			self.image = pygame.image.load("imagenes/pi4.png")		
		if imagen==4:
			pos_x = cont_size[0] * randint(0, 1) - 200
			pos_y = 200
			self.image = pygame.image.load("imagenes/pi5.png")
		self.rect = self.image.get_rect()
		self.rect.move_ip(pos_x, pos_y)
		
	def update(self):
		self.rect = self.rect.move(self.vel)
		if self.rect.left < 40 or self.rect.right > self.cont_size[0]-40:
			self.vel[0] = -self.vel[0]
		if self.rect.top < 40 or self.rect.bottom > self.cont_size[1]-40:
			self.vel[1] = -self.vel[1]

