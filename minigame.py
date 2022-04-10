def minigame():
 import pygame 
 import sys
 import pictures
 import random

 
 status = 'alive'
 zombie_size = [50,100,150,200,250,300]
 obstacle_list = []
 bg_pos = 0
 move= 0
 side = 0
 score = 0

 game_screen = pygame.display.set_mode((608,342)) #creates a screen 1024 pixels wide and 576 pixels long
 clock = pygame.time.Clock() # creates clock object, this will be used later to control the fps

 def move_bg():
  game_screen.blit(background,(bg_pos,0))
  game_screen.blit(background,(bg_pos+608,0))

 def new_obstacle():
  z_size = random.choice(zombie_size)
  new_obstacle = obstacle.get_rect(center =(800,z_size))
  return new_obstacle

 def move_obstacle(obstacle):
   for obstacle in obstacle_list:
     obstacle.centerx = obstacle.centerx -1

 def obstacle_screen(obstacle):
  for obstacles in obstacle_list:
    game_screen.blit(obstacle, obstacles)

 def death (obstacle):
  status = 'alive'
  for obstacle in obstacle_list:
    if avatar_bound.colliderect(obstacle):
     status = 'dead'
  return status


 pygame.init() #initialize pygame module
 
 #uploading all the necessary images
 background = pygame.image.load('pictures/bg.jpg').convert()
 avatar = pygame.image.load('pictures/avatar.png').convert_alpha()
 obstacle = pygame.image.load('pictures/zombie.png').convert_alpha()
 gameover = pygame.image.load('pictures/gameover.jpg').convert()
 gamewin = pygame.image.load('pictures/win.webp').convert()

 #transforming and scaling images
 avatar = pygame.transform.scale(avatar, (58, 62))
 obstacle = pygame.transform.scale(obstacle, (60, 80))
 gameover= pygame.transform.scale(gameover,(608,342))
 gamewin= pygame.transform.scale(gamewin,(608,342))
 avatar_bound = avatar.get_rect(center =(50,150)) # get rectangle around surface this will help us check for collisions


 add_obstacle = pygame.USEREVENT
 pygame.time.set_timer(add_obstacle, 2200) #every 1500 millseconds event 

 while True:
  # write code to exit out of module (add score parameters
  for event in pygame.event.get():
    if event.type == pygame.QUIT: #or score reaches 10
     pygame.quit()
     sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP or event.key == ord('w'):
            move =0
            move = move - 3
        if event.key == pygame.K_DOWN or event.key == ord('s'):
            move =0
            move = move + 3
        if event.key == pygame.K_LEFT or event.key == ord('a'):
            side = 0
            side = side - 3
        if event.key == pygame.K_RIGHT or event.key == ord('d'):
            side = 0
            side = side + 3
    if event.type == pygame.KEYUP:
       side = 0
       move = 0
    if event.type == add_obstacle :
       obstacle_list.append(new_obstacle())
    

  bg_pos = bg_pos-1
  game_screen.blit(background,(bg_pos,0)) # block transfer of bg image, upper left corner at (0,0)
  move_bg()
  if bg_pos <= -608:
    bg_pos = 0
  
  if status == 'alive' and  score<= 20:
   move_obstacle(obstacle_list)
   obstacle_screen(obstacle)
   game_screen.blit(avatar, avatar_bound)
   # controlling movements of avatar
   avatar_bound.centery = avatar_bound.centery + move
   avatar_bound.centerx = avatar_bound.centerx + side
   status = death(obstacle_list)
   score = score + 0.01
   


  elif status == 'dead':
    game_screen.blit(gameover,(-20,0))
  
  elif score >= 20:
     game_screen.blit(gamewin,(0,0))



  pygame.display.update() # updating the display screen
  clock.tick(100) #updates 100 times in a second