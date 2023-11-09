import pygame

#initiate game
pygame.init()

#set display settings
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

#set color codes and font we will use later
black = (0,0,0)
white = (255,255,255)
font = pygame.font.Font(None, 36)

#set game clock to track of changes
clock = pygame.time.Clock()

#load player avatars
p1 = pygame.image.load('luke.jpg')
p2 = pygame.image.load('vader.jpg')

#set players' starting positions
p1_x_pos = (0)
p1_y_pos = (display_height - 100)
p2_x_pos = (display_width - 100)
p2_y_pos = (display_height - 100)

#set players' starting speeds
p1_speed = 0    
p2_speed = 0

#set players' starting health
p1_health = 100
p2_health = 100

#set winner to nothing on startup
winner = ''

#set game to running on startup
running = True

#everything that will happen while the game is running
while running: 

    #retrieve all events happening and take the following actions
    for event in pygame.event.get(): 

        #if a key is being pressed
        if event.type == pygame.KEYDOWN:
            
            #p1 movement via a/d
            if event.key == pygame.K_a:
                p1_speed -= 10
            elif event.key == pygame.K_d:
                p1_speed += 10 

            #p2 movement via left/right arrows
            elif event.key == pygame.K_LEFT:
                p2_speed -= 10
            elif event.key == pygame.K_RIGHT:
                p2_speed += 10

            #p1 and p2 collision logic
            if p1_x_pos - p2_x_pos > -100 and p1_x_pos - p2_x_pos < 100:

                #p1 attack via e
                if event.key == pygame.K_e and p1_health > 0 and p2_health > 0:
                    p2_health -= 10

                #p2 attack via l
                elif event.key == pygame.K_l and p1_health > 0 and p2_health > 0:
                    p1_health -= 10

        #if a key is released
        elif event.type == pygame.KEYUP:

            #p1 stop moving
            if event.key == pygame.K_a or event.key == pygame.K_d:
                p1_speed = 0

            #p2 stop moving
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                p2_speed = 0
    
    #change players' positions based on speed
    p1_x_pos += p1_speed
    p2_x_pos += p2_speed

    #p1 health bar
    p1_text = font.render("P1 Health: " + str(p1_health), True, black)
    p1_text_rect = p1_text.get_rect()
    p1_text_rect.center = (100, 100)

    #p2 health bar
    p2_text = font.render("P2 Health: " + str(p2_health), True, black)
    p2_text_rect = p2_text.get_rect()
    p2_text_rect.center = (700, 100)

    #set winner based on first player to 0 health
    if p1_health == 0:
        winner = 'P2 Wins!'
    elif p2_health == 0: 
        winner = 'P1 Wins!'

    #set winning screen based on who won
    winner_text = font.render(winner, True, black) 
    winner_rect = winner_text.get_rect()
    winner_rect.center = (300, 200) 

    #set background to white
    gameDisplay.fill(white)

    #display players' avatars on the screen in the proper position
    gameDisplay.blit(p1, (p1_x_pos, p1_y_pos))
    gameDisplay.blit(p2, (p2_x_pos, p2_y_pos))

    #display players' health bars
    gameDisplay.blit(p1_text, p1_text_rect)
    gameDisplay.blit(p2_text, p2_text_rect)

    #display winning screen
    gameDisplay.blit(winner_text, winner_rect)

    #update the screen
    pygame.display.update()

    #set game fps
    clock.tick(30)

#exit game
pygame.quit()
quit()