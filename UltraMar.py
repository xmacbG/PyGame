#Manuenl Cardenas
#xmacb@hotmail.com
#20/06/2017

import sys, pygame
from pygame.locals import *
from pygame.sprite import Sprite
import time

##### Game
from ship import Ship
from pirate import Pirate

##Display
size = width, height = 1440, 810
screen = pygame.display.set_mode(size)

##Sounds
def cargar_sonido(nombre):     
	return pygame.mixer.Sound(nombre)

###Main
def main():
	pygame.init()
	pygame.mixer.init()

	with open('data.txt') as f:
		for line in f:
			int_list = [int(i) for i in line.split()]
			print int_list[0]
	##Sounds	
	pierde_vida = cargar_sonido('sonidos/fin.mp3')
	backSound = cargar_sonido('sonidos/backSound.mp3')
	fire = cargar_sonido('sonidos/gunFire.mp3')
	#BackGround
	backSound.play()
	background_image = pygame.image.load("imagenes/sea.png")
	background_rect = background_image.get_rect()

	pygame.display.set_caption( "Ultra Mar" )

	##Entidades
	ship=Ship(size)
	pirates= []
	#Variables auxiliares de tiempo
	lasttime=time.time()
	limitVel=3
	lastT=-1
	lastP=-1

	pirates.append(Pirate(size,limitVel))

	#Ciclo del juego
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
	#Campbio de nivel
		if int(time.time()-lasttime) % 60 == 0 and int(time.time()-lasttime) != lastT:
			limitVel=limitVel+2
			for pirate in pirates:
				pirates.remove(pirate)
			lastT = int(time.time()-lasttime)

		if int(time.time()-lasttime) % 2 == 0 and len(pirates) <= 10 and int(time.time()-lasttime) != lastP:
			pirates.append(Pirate(size,limitVel))
			lastP = int(time.time()-lasttime)

	#Actulizacionesd de display barco
		ship.update()
		screen.blit(background_image, background_rect)
		screen.blit(ship.image, ship.rect)
	
	#Actulizacionesd de display bals y enemigos destruidos		
		for bullet in ship.bullets:
			bullet.update()
			fire.play()
			for pirate in pirates:
				if bullet.rect.colliderect(pirate.rect):
					ship.bullets.remove(bullet)
					pirates.remove(pirate)
					pierde_vida.play()
			if bullet.rect.top <= 0 or bullet.rect.left <= 0 or bullet.rect.right>=size[0] or bullet.rect.bottom>=size[1]:
				ship.bullets.remove(bullet)
			screen.blit(bullet.image, bullet.rect)
	#actualizacion de enemigos	
		for pirate in pirates:
			pirate.update()
			screen.blit(pirate.image, pirate.rect)
	#Evento final
		for pirate in pirates:
			if pirate.rect.colliderect(ship.rect):
				if int(time.time()-lasttime) > int_list[0]:
					with open('data.txt', 'r+') as f:
	    					f.seek(0)
	    					f.write(str(int(time.time()-lasttime)))
	   					f.truncate()
				fuente2 = pygame.font.Font(None,100)
				texto_Fin = fuente2.render("JUEGO TERMINADO - Puntaje "+str(int(time.time()-lasttime)),1,(255,255,255))
				screen.blit(texto_Fin,(150,400)) 
				pygame.display.update()
				pierde_vida.play()
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							sys.exit()
	#Puntajes finales
		fuente = pygame.font.Font(None,30)
		texto_vida = fuente.render("Puntaje: "+str(int(time.time()-lasttime)),1,(0,0,0))
		texto_best = fuente.render("Mejor Puntaje: "+str(int_list[0]),1,(0,0,0))
		screen.blit(texto_vida,(700,30)) 
		screen.blit(texto_best,(700,80)) 

		pygame.display.update()
		pygame.time.delay(20)

		#print int(time.time()-lasttime)		

if __name__ == '__main__':
	main()
