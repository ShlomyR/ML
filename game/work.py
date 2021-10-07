import pygame

pygame.init()

clock = pygame.time.Clock()

s_width = 1100
s_height = 600

screen = pygame.display.set_mode((s_width,s_height))

pygame.display.set_caption("the game")

isjump = False
jumpCount = 10

x = s_height
y = 440
width = 40
height = 60
vol = 5
FPS = 60
run = True

while run:
#	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > vol:
		x -= vol
	if keys[pygame.K_RIGHT] and x < s_width - width - vol:
		x += vol
	if not(isjump):

		if keys[pygame.K_UP] and y > vol:
			y -= vol
		if keys[pygame.K_DOWN] and y < s_height - height -  vol:
			y += vol
		if keys[pygame.K_SPACE]:
			isjump = True
	else:
		if jumpCount >= -10:
			neg = 1
			if jumpCount < 0:
				neg = -1
			y -= (jumpCount ** 2) * 0.5 * neg
			jumpCount -= 1
		else:
			isjump = False
			jumpCount = 10
	screen.fill((0,0,0))
	pygame.draw.rect(screen,(0,0,255),(x,y,width,height))
	pygame.display.update()
	clock.tick(FPS)


pygame.quit()
