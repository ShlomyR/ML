import pygame,sys
from player import Player

class Game:
	def __init__(self):
		player_sprite = Player((Screen_h / 2, Screen_w),Screen_h,5)
		self.player = pygame.sprite.GroupSingle(player_sprite)


	def run(self):
		self.player.update()
		self.player.draw(Screen)


if __name__ == '__main__':
	pygame.init()

	# window size
	Screen_h = 1100
	Screen_w = 550
	Screen = pygame.display.set_mode(( Screen_h, Screen_w))
	clock = pygame.time.Clock()
	game = Game()
	FPS = 60

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
		Screen.fill((0,0,0))
		game.run()
		pygame.display.flip()
		clock.tick(FPS)
