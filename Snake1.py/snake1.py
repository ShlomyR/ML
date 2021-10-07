import os
import sys,random,time
import pygame
import button

CLOCK = pygame.time.Clock()

from pygame.locals import *

pygame.init()

pygame.display.set_caption('snake game by Shlomy')

# Initialize constants
font = pygame.font.SysFont("comicsansms", 30)
smallfont = pygame.font.SysFont("comicsansms", 14)
slategrey = (112, 128, 144)
lightgrey = (165, 175, 185)
blackish = (10, 10, 10)
white = (255, 255, 255)
black = (0, 0, 0)


#image = pygame.image.load("main.png")

WIN_X = 1100
WIN_Y = 600
WIN = pygame.display.set_mode((WIN_X, WIN_Y))

FPS = 25
font=pygame.font.SysFont('p052',40)


#Loade image
BG = pygame.transform.scale(pygame.image.load('earth.png'),(WIN_X,WIN_Y))
crush = pygame.transform.scale(pygame.image.load('isto.jpg'),(WIN_X,WIN_Y))
play_img = pygame.transform.scale(pygame.image.load('start_btn.jpg'),(200,50))#.convert_alpha()
options_img = pygame.transform.scale(pygame.image.load('option_btn.jpg'),(200,50))#.convert_alpha()
exit_img = pygame.transform.scale(pygame.image.load('exit_btn.jpg'),(200,50))#.convert_alpha()





# Function to create a button
def create_button(x, y, width, height, hovercolor, defaultcolor):
    mouse = pygame.mouse.get_pos()
    # Mouse get pressed can run without an integer, but needs a 3 or 5 to indicate how many buttons
    click = pygame.mouse.get_pressed(3)
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hovercolor, (x, y, width, height))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(WIN, defaultcolor, (x, y, width, height))

def start_menu():
    while True:
        WIN.fill((0, 0, 0))
        WIN.blit(BG ,(0,0))
        # start button (left, top, width, height)
        #play button
        play_button = create_button(WIN_X + 5, 7, 125, 26, lightgrey, slategrey)
        #options button
        options_button = create_button(WIN_X - 5, 15, 125, 26, lightgrey, slategrey)
        #exit button
        exit_button = create_button(WIN_X + 80, 20, 125, 26, lightgrey, slategrey)

"""
        if play_button:
            main_manu()


        # play button text
        playbuttontext = smallfont.render("Click to Play!", True, blackish)
        WIN.blit(playbuttontext, (WIN_X - 125, 9))
     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        CLOCK.tick(FPS)
        return True
"""
#create button instances
play_button = button.Button(100, 150, play_img,1.1)
options_button = button.Button(100, 250, options_img,1.1)
exit_button = button.Button(100, 350, exit_img,1.1)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    while True:
        WIN.fill((0,0,0))
        WIN.blit(BG, (0,0))
        draw_text('main menu', font, (120, 255, 0), WIN, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(100, 150, 200, 50)
        button_2 = pygame.Rect(100, 250, 200, 50)
        button_3 = pygame.Rect(100, 350, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                play()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                exit()
        play_button.draw(WIN)
        options_button.draw(WIN)
        exit_button.draw(WIN)
#        pygame.draw.rect(WIN ,(255, 0, 0), button_1)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        CLOCK.tick(FPS)
def play():
    running = True
    while running:
        WIN.fill((0,0,0))
        WIN.blit(BG, (0,0))
        draw_text('select mode', font, (255, 255, 255), WIN, 20, 20)
        draw_text('easy', font, (255, 255, 255), WIN, 200, 200)
        draw_text('moderated', font, (255, 255, 255), WIN, 200, 300)
        draw_text('hard', font, (255, 255, 255), WIN, 200, 400)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        CLOCK.tick(FPS)

def options():
    running = True
    while running:
        WIN.fill((0,0,0))
        WIN.blit(BG, (0,0))
        draw_text('options', font, (255, 255, 255), WIN, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        CLOCK.tick(FPS)

def exit():
    running = True
    while running:
        WIN.fill((0,0,0))

        draw_text('exit', font, (255, 255, 255), WIN, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == draw_text('exit', font, (255, 255, 255), WIN, 20, 20):
                running = False

        pygame.display.update()
        CLOCK.tick(FPS)

main_menu()



def main_menu():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
        WIN.fill((0,0,0))
        WIN.blit(BG, (0,0))
        main_menu_message = font.render('Press anywhere to start the game' , True , (255,255,255))
        font_pos = main_menu_message.get_rect(center=(WIN_X//2, WIN_Y//2))
        WIN.blit(main_menu_message, font_pos)
        pygame.display.update()


def game_over(score):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            WIN.fill((0,0,0))
            WIN.blit(crush , (0,0))
            game_over_message = font.render('You Lost' , True , (255,0,0))
            game_over_score = font.render(f'Your Score was {score}' , True , (255,255,255))

            font_pos_message = game_over_message.get_rect(center=(WIN_X//2, WIN_Y//2))
            font_pos_score = game_over_score.get_rect(center=(WIN_X//2, WIN_Y//2+40))
            WIN.blit(game_over_message , font_pos_message)
            WIN.blit(game_over_score , font_pos_score)
            pygame.display.update()
            time.sleep(3)
            main_menu()


def main():
    CLOCK = pygame.time.Clock()
    snake_pos=[200,70]
    snake_body=[[200,70] , [200-10 , 70] , [200-(2*10),70]]
    fruit_pos = [0,0]
    fruit_spawn = True
    direction = 'right'
    score=0
#    CLOCK = pygame.time.Clock()
 
    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            keys= pygame.key.get_pressed()
            if (keys[pygame.K_w] or keys[pygame.K_UP]) and direction != 'down':
                direction = 'up'
            if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and direction != 'up':
                direction = 'down'
            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and direction != 'left':
                direction = 'right'
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and direction != 'right':
                direction = 'left'

        WIN.fill((0,0,0))
        WIN.blit(BG, (0,0))
        for square in snake_body:
            pygame.draw.rect(WIN ,(255, 255, 0), (square[0],square[1],10,10))
        if direction == 'right':
            snake_pos[0] += 10
        elif direction == 'left':
            snake_pos[0] -= 10
        elif direction == 'up':
            snake_pos[1] -= 10
        elif direction == 'down':
            snake_pos[1] += 10

        snake_body.append(list(snake_pos))

        if fruit_spawn:
            fruit_pos = [random.randrange(40,WIN_X-40),random.randrange(40,WIN_Y-40)]
            fruit_spawn = False

        pygame.draw.rect(WIN ,(138,43,226),(fruit_pos[0],fruit_pos[1],10,10))

        score_font = font.render(f'{score}' , True , (255,255,255))
        font_pos = score_font.get_rect(center=(WIN_X//2-40 , 30))
        WIN.blit(score_font , font_pos)

        if pygame.Rect(snake_pos[0],snake_pos[1],10,10).colliderect(pygame.Rect(fruit_pos[0],fruit_pos[1],10,10)):
            fruit_spawn=True
            score += 5
        else:
            snake_body.pop(0)

        for square in snake_body[:-1]:
            if pygame.Rect(square[0],square[1],10,10).colliderect(pygame.Rect(snake_pos[0],snake_pos[1],10,10)):
                game_over(score)

        if snake_pos[0]+10 <=0 or snake_pos[0] >= WIN_X:
            game_over(score)
        if snake_pos[1]+10 <=0 or snake_pos[1] >= WIN_Y:
            game_over(score)
        pygame.display.update()

        CLOCK.tick(FPS)

#caliing the main function
#start_menu()
main_menu()
