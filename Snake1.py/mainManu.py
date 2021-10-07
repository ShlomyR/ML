import snake1




class main_manu():
 def __init__(self , play , options , exit ):
  

  def main_menu():
    while True:
        WIN.fill((0,0,0))
        WIN.blit(BG, (0,0))
        draw_text('main menu', font, (255, 255, 255), WIN, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                play()
        if button_2.collidepoint((mx, my)):
            if click:
                game()
        if button_3.collidepoint((mx, my)):
            if click:
                options()
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
        mainClock.tick(FPS)
def play():
    running = True
    while running:
        WIN.fill((0,0,0))

        draw_text('play', font, (255, 255, 255), WIN, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(FPS)

def game():
    running = True
    while running:
        WIN.fill((0,0,0))
        draw_text('game', font, (255, 255, 255), WIN, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(FPS)
        
def options():
    running = True
    while running:
        WIN.fill((0,0,0))

        draw_text('options', font, (255, 255, 255), WIN, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(FPS)

main_menu()
