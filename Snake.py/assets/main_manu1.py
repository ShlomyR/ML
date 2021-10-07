import pygame
import button
from curser import *




def exit_mn():
	
	CLOCK = pygame.time.Clock()
	#screen
	screen_width = 1100
	screen_height = int(screen_width *0.5)
	screen = pygame.display.set_mode((screen_width,screen_height))

	#windows caption
	pygame.display.set_caption('shlomy the game')

	start_game = False
	#load pictures

	BG = pygame.transform.scale(pygame.image.load('Snake.jpg'),(screen_width,screen_height))

	#curser icon next to buttons
	curser = pygame.transform.scale(pygame.image.load('snake.gif'),(700,700))

	#load button pictures

	start_img = pygame.image.load('start_btn.jpg')
	options_img = pygame.image.load('option_btn.jpg')
	exit_img = pygame.image.load('exit_btn.jpg')


	#create button instances
	start_button = button.Button(200, 100, start_img, 0.6)
	options_button = button.Button(200, 250, options_img, 0.6)
	exit_button = button.Button(200, 400, exit_img, 0.6)
	curser1 = button.Button(400, 100, curser, 0.1)


	run = True
	while run:
		screen.blit(BG,(0,0))
		if start_button.draw(screen):
			import snake
		if options_button.draw(screen):
			print('wo')
		if exit_button.draw(screen):
			run = False

		for event in pygame.event.get():
#        	print(event)
			#quit game
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()
		CLOCK.tick(25)
	pygame.quit()
exit_mn()
#if __name__=="__main__":
    # call the main function
#	exit_mn()
