import pygame
import button

pygame.init()

#clock = 

screen_width = 550
screen_height = int(screen_width *0.5)
screen = pygame.display.set_mode((screen_width,screen_height))

clock = pygame.time.Clock()
FPS = 60

#windows caption
pygame.display.set_caption('shlomy the game')


#load pictures
restart_img = pygame.image.load('image/restart_btn.png')
exit_img1 = pygame.image.load('image/exit_btn1.png')

#create button instances
restart_button = button.Button(300, 70, restart_img, 1.8)
exit_button1 = button.Button(70, 70, exit_img1, 0.6)



run = True

def restart():

        run = True

        while run:
            screen.fill((0,0,0))
            if restart_button.draw(screen):
                print('gg')
            if exit_button1.draw(screen):
                print('yy')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()

        pygame.quit()
restart()
