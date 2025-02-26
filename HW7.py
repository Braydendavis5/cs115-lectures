import pygame

#init pygame
pygame.init()

#window dimensions
width = 800
height = 800
screen = pygame.display.set_mode((width,height))

#set window title
pygame.display.set_caption("Frogger")

#fps
clock = pygame.time.Clock()
dt = 0
speed = 10

"""game loop"""
running = True
while running:
  """Handle events"""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  """update our game state"""
  
  """draw to our screen"""
  #clear screen
  screen.fill("green")

  #draw line
  pygame.draw.line(
    screen, 
    "grey", 
    (0,600), (800,600), 50
  )

    #draw line
  pygame.draw.line(
    screen, 
    "black", 
    (0,400), (800,400), 100
  )

      #draw line
  pygame.draw.line(
    screen, 
    "black", 
    (0,200), (800,200), 100
  )

      #draw line
  pygame.draw.line(
    screen, 
    "yellow", 
    (0,400), (800,400), 5
  )

        #draw line
  pygame.draw.line(
    screen, 
    "yellow", 
    (0,200), (800,200), 5
  )
 
  # draw rectangle
  pygame.draw.rect(
    screen, 
    "dark green", 
    pygame.Rect((300,590),(25,25))
  )












  #update screen
  pygame.display.flip()


  #fps
  dt = clock.tick(speed)/1000


  #quit pygame
pygame.quit()
