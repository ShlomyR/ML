import sys,random,time
import pygame
import button
#import snake_body

pygame.init()

WIN_X = 1100
WIN_Y = 550

#windows caption
pygame.display.set_caption('shlomy the game')


#load background pictures
BG = pygame.transform.scale(pygame.image.load('image/Snake.jpg'),(WIN_X,WIN_Y))

#body of thw snake
head_img = pygame.image.load('image/head_right.png')
bodyX_img = pygame.image.load('image/body_horizontal.png')
bodyY_img = pygame.image.load('image/body_vertical.png')



tailL_img = pygame.image.load('image/tail_left.png')
tailU_img = pygame.image.load('image/tail_up.png')
tailR_img = pygame.image.load('image/tail_right.png')
tailD_img = pygame.image.load('image/tail_down.png')

headD_img = pygame.image.load('image/head_down.png')
headU_img = pygame.image.load('image/head_up.png')
headL_img = pygame.image.load('image/head_left.png')
headR_img = pygame.image.load('image/head_right.png')

#apple picture
apple_img = pygame.image.load('image/apple.png')

#load button pictures
start_img = pygame.image.load('image/start_btn.jpg')
hover_start_img = pygame.image.load('image/hover_start_btn.jpg')
options_img = pygame.image.load('image/option_btn.jpg')
hover_options_img = pygame.image.load('image/hover_option_btn.jpg')
exit_img = pygame.image.load('image/exit_btn.jpg')
hover_exit_img = pygame.image.load('image/hover_btn.jpg')
restart_img = pygame.image.load('image/restart_btn.png')
exit_img1 = pygame.image.load('image/exit_btn1.png')

#create button instances
start_button = button.Button(200, 100, start_img, 0.6)
hover_start_button = button.Button(200, 100, hover_start_img, 0.6)
options_button = button.Button(200, 250, options_img, 0.6)
hover_options_button = button.Button(200, 250, hover_options_img, 0.6)
exit_button = button.Button(200, 400, exit_img, 0.6)
hover_exit_button = button.Button(200, 400, hover_exit_img, 0.6)
restart_button = button.Button(600, 230, restart_img, 1.8)
exit_button1 = button.Button(200, 230, exit_img1, 0.6)

WIN = pygame.display.set_mode((WIN_X,WIN_Y))

font = pygame.font.SysFont('comicsans',40)

#main function
def main_menu():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   game_intro()
               if event.key == pygame.K_RETURN:
                   main()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
        WIN.fill((0,0,0))
        main_menu_message = font.render('Press anywhere to start the game' , True , (255,255,255))
        font_pos = main_menu_message.get_rect(center=(WIN_X//2, WIN_Y//2))
        WIN.blit(main_menu_message , font_pos)
        pygame.display.update()



def game_over(score):
        try:
           highestscore = int(get_higescore())
        except:
           highestscore = 0
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            WIN.fill((0,0,0))
            game_over_message = font.render('You Lost' , True , (255,0,0))
            game_over_score = font.render(f'Your Score was {score}' , True , (255,255,255))
            game_over_highscore = font.render(f'Your highScore is: {highestscore}' , True , (0,0,255))
            font_pos_message = game_over_message.get_rect(center=(WIN_X//2, WIN_Y//2))
            font_pos_score = game_over_score.get_rect(center=(WIN_X//2, WIN_Y//2+40))
            font_pos_highscore = game_over_highscore.get_rect(center=(WIN_X//2, WIN_Y//2+80))
            WIN.blit(game_over_message , font_pos_message)
            WIN.blit(game_over_score , font_pos_score)
            WIN.blit(game_over_highscore , font_pos_highscore)
            pygame.display.update()
            #checking highscore
            if (highestscore < score):
                highestscore = score
            with open("highscore.txt","w") as f:
                f.write(str(highestscore))
            time.sleep(3)
            get_higescore()
            
            restart()
            main_menu()
def get_higescore():
	with open("highscore.txt","r") as f:
		return f.read()

def restart():

        run = True

        while run:
            WIN.fill((0,0,0))
            if restart_button.draw(WIN):
                main_menu()
            if exit_button1.draw(WIN):
                game_intro()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                       game_intro()
                    if event.key == pygame.K_r:
                       main_menu()
#                       pygame.quit()
#                       exit()
#                    run = False
            pygame.display.update()

        pygame.quit()

#restart()


def game_intro():
        run = True

        while run:

            WIN.blit(BG,(0,0))
            mouse = pygame.mouse.get_pos()
#            print(mouse)
            if 200 + 170 > mouse[0] > 200 and 100 + 76 > mouse[1] > 100:
                if hover_start_button.draw(WIN):
                   main()
            else:
                if start_button.draw(WIN):
                   main()
            if 200 + 170 > mouse[0] > 200 and 250 + 76 > mouse[1] > 250:
                if hover_options_button.draw(WIN):
                   print('wo')
            else:       
                if options_button.draw(WIN):
                   print('wo')
            if 200 + 170 > mouse[0] > 200 and 400 + 76 > mouse[1] > 400:
                if hover_exit_button.draw(WIN):
                   pygame.quit()
                   exit()
            else:
                if exit_button.draw(WIN):
                   pygame.quit()
                   exit()

            for event in pygame.event.get():
	#   print(event)
		#quit game
                if event.type == pygame.QUIT:
                     pygame.quit()
                     exit()

                if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_ESCAPE:
                          pygame.quit()
                          exit()
            pygame.display.update()

        pygame.quit()

def main():
    CLOCK = pygame.time.Clock()
    snake_pos=[200,70]
    snake_body=[[200,70] , [200-10 , 70] , [200-(2*10),70]]
#    snake_body1=[[100,70] , [100-10 , 70] , [100-(2*10),70]]
    fruit_pos = [0,0]
    fruit_spawn = True
    direction = 'right'
    score = 0
#    higescore = 0
    highestscore = 0
    #game loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   restart()
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_w] or keys[pygame.K_UP]) and direction != 'down':
                direction = 'up'
            if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and direction != 'up':
                direction = 'down'
            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and direction != 'left':
                direction = 'right'
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and direction != 'right':
                direction = 'left'

        WIN.fill((0,0,0))
        WIN.blit( apple_img, (fruit_pos))
        
        for i, square in enumerate(snake_body):
#            print(square)
            print(i)
            if(i == len(snake_body) - 1):

                if direction == 'right':
                    WIN.blit( headR_img, (square))
                elif direction == 'left':
                    WIN.blit( headL_img, (square))
                elif direction == 'up':
                    WIN.blit( headU_img, (square))
                elif direction == 'down':
                    WIN.blit( headD_img, (square))

            elif i == 0:
                if direction == 'right':
                    WIN.blit( tailL_img, (square))
                elif direction == 'left':
                    WIN.blit( tailR_img, (square))
                elif direction == 'up':
                    WIN.blit( tailD_img, (square))
                elif direction == 'down':
                    WIN.blit( tailU_img, (square))
#                pygame.draw.rect(WIN ,(30,144,255), (square[0],square[1],10,10))
            else:
                if direction == 'right' or direction == 'left':
                   WIN.blit( bodyX_img, (square))
                elif direction == 'up' or direction == 'down':
                   WIN.blit( bodyY_img, (square))
                
#                pygame.draw.rect(WIN ,(255, 255, 0), (square[0],square[1],10,10))
            
        if direction == 'right':
            snake_pos[0] += 10
        elif direction == 'left':
            snake_pos[0] -= 10
        elif direction == 'up':
            snake_pos[1] -= 10
        elif direction == 'down':
            snake_pos[1] += 10

        snake_body.append(list(snake_pos))
#        print( snake_body.append(list(snake_pos)))
        if fruit_spawn:
            fruit_pos = [random.randrange(40,WIN_X-40),random.randrange(40,WIN_Y-40)]
            fruit_spawn = False

#        pygame.draw.rect(WIN ,(138,43,226),(fruit_pos[0],fruit_pos[1],10,10))
        score_font = font.render(f'score: {score}' , True , (255,255,255))
#        higescore_font = font.render(f"highscore: {highestscore}" , True , (255,255,255))
        font_pos = score_font.get_rect(center=(WIN_X//2-300 , 30))
#        font_pos1 = higescore_font.get_rect(center=(WIN_X//2+300 , 30))
        WIN.blit(score_font , font_pos)
#        WIN.blit(higescore_font , font_pos1)

        if pygame.Rect(snake_pos[0],snake_pos[1],30,30).colliderect(pygame.Rect(fruit_pos[0],fruit_pos[1],40,40)):
            fruit_spawn=True
            score += 5
#            higescore += 5
        else:
            snake_body.pop(0)

        for square in snake_body[:-1]:
            if pygame.Rect(square[0],square[1],10,10).colliderect(pygame.Rect(snake_pos[0],snake_pos[1],10,10)):
                game_over(score)

        if snake_pos[0]+10 <=0 or snake_pos[0] >= WIN_X:
            game_over(score)
        if snake_pos[1]+10 <=0 or snake_pos[1] >= WIN_Y:
            game_over(score)
#        game_over_highscore = font.render(f'Your highScore is: {highestscore}' , True , (0,0,255))
#        font_pos_highscore = game_over_highscore.get_rect(center=(WIN_X//2, WIN_Y//2+80))
#        WIN.blit(game_over_highscore , font_pos_highscore)
        pygame.display.update()

        CLOCK.tick(25)

#caliing the main function
game_intro()
main_menu()
