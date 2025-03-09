# Brayden Davis
# 3/2/1015
# HW7
# This is the art/screen for Frogger

# This is to import pygame, so that I can make my game.
import pygame

# init pygame
pygame.init()

system_fonts = pygame.font.get_fonts()
myFont = pygame.font.SysFont(name=system_fonts[0], size=48,
                             bold=True, italic=False)

# window dimensions
width = 800
height = 625

screen = pygame.display.set_mode((width,height))

# set window title
pygame.display.set_caption("Frogger")

# fps
clock = pygame.time.Clock()
dt = 0
speed = 10
score = 0
# game loop
running = True
while running:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # update our game state

  # draw to our screen
  # clear screen
  screen.fill("green")
  
  # draw sidewalk, at the bottum of the screen
  pygame.draw.line(
    screen, 
    "grey", 
    (0,600), (800,600), 50
  )

  # Win state
  pygame.draw.line(
    screen, 
    "dark green", 
    (0,0), (800,0), 50
  ) 
  
  # draw road1
  pygame.draw.line(
    screen, 
    "black", 
    (0,400), (800,400), 100
  )

  # draw road2
  pygame.draw.line(
    screen, 
    "black", 
    (0,200), (800,200), 100
  )

  # draw middle of road1
  pygame.draw.line(
    screen, 
    "yellow", 
    (0,400), (800,400), 5
  )

  # draw middle of road2
  pygame.draw.line(
    screen, 
    "yellow", 
    (0,200), (800,200), 5
  )
 
  # draw frog
  pygame.draw.rect(
    screen, 
    "light green", 
    pygame.Rect((300,590),(25,25))
  )

  # draw car1
  pygame.draw.rect(
    screen, 
    "silver", 
    pygame.Rect((500,360),(40,25))
  )

  # draw car2
  pygame.draw.rect(
    screen, 
    "red", 
    pygame.Rect((300,420),(40,25))
  )

  # draw car3
  pygame.draw.rect(
    screen, 
    "white", 
    pygame.Rect((400,220),(40,25))
  )

  # draw car4
  pygame.draw.rect(
    screen, 
    "blue", 
    pygame.Rect((220,160),(40,25))
  )

  # This is for the score
  score_image = myFont.render(f"Score: {score}", True, "white")
  score_rect = score_image.get_rect()
  score_rect.topleft = (20, 20)
  screen.blit(score_image, score_rect)

  # update screen
  pygame.display.flip()

  # fps
  dt = clock.tick(speed)/1000

  # quit pygame
pygame.quit()
