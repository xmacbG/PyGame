import sys, pygame
from pygame.locals import *
from pygame.sprite import Sprite
from bullet import Bullet

class Ship(Sprite):
	def __init__(self, cont_size):
		Sprite.__init__(self)
		self.puntos = 0
		self.vida = 100
		self.cont_size = cont_size
		self.image = pygame.image.load("imagenes/ship.png")
		self.rect = self.image.get_rect()
		self.rect.move_ip(cont_size[0]-200, cont_size[1]-200)
		self.bullets = []
		self.limitBulets=4;

	def update(self):
		teclas = pygame.key.get_pressed()
		if teclas[K_LEFT] and self.rect.left > 10:
			self.rect.x -= 10
		elif teclas[K_RIGHT] and self.rect.right < self.cont_size[0]-10:
			self.rect.x += 10
		elif teclas[K_UP] and self.rect.top > 10:
			self.rect.y -= 10
		elif teclas[K_DOWN] and self.rect.bottom < self.cont_size[1]-10 :
			self.rect.y += 10
		elif teclas[K_a] and len(self.bullets) < self.limitBulets: #izquierda
			pos = [self.rect.centerx-10, self.rect.centery-20]
			self.bullets.append(Bullet(pos,0))
		elif teclas[K_w] and len(self.bullets) < self.limitBulets: #arriba
			pos = [self.rect.centerx-10, self.rect.centery-20]
			self.bullets.append(Bullet(pos,1))
		elif teclas[K_d] and len(self.bullets) < self.limitBulets: #derecha
			pos = [self.rect.centerx-10, self.rect.centery-20]
			self.bullets.append(Bullet(pos,2))
		elif teclas[K_s] and len(self.bullets) < self.limitBulets: #abajo
			pos = [self.rect.centerx-10, self.rect.centery-20]
			self.bullets.append(Bullet(pos,3))
	
