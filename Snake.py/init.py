import pygame
import button
import sys

pygame.init()

WIN_X = 1100
WIN_Y = 550


#windows caption
pygame.display.set_caption('shlomy the game')


#load background pictures

BG = pygame.transform.scale(pygame.image.load('image/Snake.jpg'),(WIN_X,WIN_Y))


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
