import pygame,sys,time,random,math
from pygame import mixer




pygame.init()

#windows caption
pygame.display.set_caption('shlomy the game')

#font
font = pygame.font.SysFont('comicsans',30)
Font = pygame.font.SysFont('comicsans',100)

#screen window
Screen_w = 1100
Screen_h = Screen_w // 2
Screen = pygame.display.set_mode(( Screen_w, Screen_h))

# background image
BG = pygame.transform.scale(pygame.image.load('image/Space background.jpg'),(Screen_w,Screen_h))

# background Sound
mixer.music.load('Sound/background.wav')
mixer.music.play(-1)

#ship picture
ship = pygame.transform.scale(pygame.image.load('image/rocket3.gif'),(100,150))

#alien picture
#alien.append(pygame.transform.scale(pygame.image.load('image/alien.png'),(50,40)))

# bullet picture
bullet = pygame.image.load('image/bullet.png')

# ship startint point
shipX = Screen_w// 2 - 100
shipY = Screen_h - 150


# multipuls aliens
alien = []
alienX = []
alienY = []
directionY_alien = []
directionX_alien = []
num_of_enemies = 26


# alien rendom spot location whitin the screen borders
for i in range(num_of_enemies):
	alien.append(pygame.transform.scale(pygame.image.load('image/alien.png'),(50,40)))
	alienX.append(random.randint(0,1060))
	alienY.append(random.randint(10,30))
	directionX_alien.append(15)
	directionY_alien.append(20)

# bullet pos
bulletX = 0
bulletY = Screen_h - 150
bullet_state = "ready"
bulletX_chenge = 0
bulletY_chenge = 10

# ship movment
direction_ship = 0

#ship and alien x border
ship_X_B = Screen_w - 100
alien_X_B = Screen_w - 50

Score = 0
run = True
CLOCK = pygame.time.Clock()


def game_over():
	
	game_over_text = Font.render('game over',True,(255,0,0))
	Screen.blit( game_over_text,( 350, 275))
#	pygame.display.update()
#	time.sleep(3)


def Ship(shipX , shipY):
	Screen.blit(ship , ( shipX, shipY))




def Alien(alienX , alienY, i):
	Screen.blit(alien[i] , ( alienX, alienY))



def Fire_Bullet(x , y):
	global bullet_state
	bullet_state = "fire"
	Screen.blit(bullet , (x + 35 , y - 15 ))# bullet location on the ship

def isCollision(alienX, alienY, bulletX, bulletY):
	distance = math.sqrt((math.pow(alienX - bulletX,2)) + (math.pow(alienY - bulletY,2)))
	if distance < 50:
		return True
 


while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		#ship movment	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				direction_ship = 5
			if event.key == pygame.K_LEFT:
				direction_ship = -5
			if event.key == pygame.K_SPACE:
				if bullet_state == "ready":
					Bullet_Sound = mixer.Sound('Sound/laser.wav')
					Bullet_Sound.play()
					bulletX = shipX
					Fire_Bullet( bulletX, bulletY)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
				direction_ship = 0
	shipX += direction_ship

	Screen.fill((0,0,0))
	Screen.blit(BG , (0,0))
	Ship(shipX,shipY)


	#ship and alien screen borders
	if shipX <= 0:
		shipX = 0
	elif shipX >= ship_X_B:
		shipX = ship_X_B
	for i in range(num_of_enemies):
		# define when in thw y axis it going to detarment game over
		if alienY[i] > 350:
			for j in range(num_of_enemies):
				alienY[j] = 1000
			game_over()
			break

		alienX[i] += directionX_alien[i]	
		if alienX[i] <= 0:
			directionX_alien[i] = 5
			alienY[i] += directionY_alien[i]
		elif alienX[i] >= alien_X_B:
			directionX_alien[i] = -5
			alienY[i] += directionY_alien[i]
		# collision
		collision = isCollision(alienX[i], alienY[i], bulletX, bulletY)
		if collision:
			exploation_Sound = mixer.Sound('Sound/explosion.wav')
			exploation_Sound.play()
			bulletY =  Screen_h - 150
			bullet_state = "ready"
			Score += 1
#			print(Score)
			alienX[i] = random.randint(0,1060)
			alienY[i] = random.randint( 10, 10)
		Alien(alienX[i],alienY[i] , i)



	# score on screen
	Score_O_S = font.render(f'score : {Score}' , True, (255,255,255))
	pos_Score_O_S = Score_O_S.get_rect( topleft = ( 50, 10))	
	Screen.blit(Score_O_S , (pos_Score_O_S))

	# bullet movment
	if bulletY <= 0:
		bulletY = Screen_h - 150
		bullet_state = "ready"
	if bullet_state == "fire":
		Fire_Bullet( bulletX, bulletY)
		bulletY -= bulletY_chenge

		
	pygame.display.update()
	CLOCK.tick(480)
