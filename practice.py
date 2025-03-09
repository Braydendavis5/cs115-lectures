from pygame.display import set_allow_screensaver


print("good morning!")

if True:
  print("true")

import helper_functions

while True:
  
  # draw text to screen
  text_image = my_font.render("SNAKE!", True, "red")
  text_rect = text_image.get_rect()
  text_rect.topleft = (20,20)
  screen.blit(text_image, text_rect)


  def draw_text():
  text_image = my_font.render(f"SNAKE! Score:", True, "red")
  text_rect = my_font.render(text, True, text_color)
  text_rect




  # create font
  systems_fonts = pygame.font.get_fonts()
  print(systems_fonts)
  my_font = pygame.font.SysFont(systems_fonts[0], size=48 bold=True, italic=False)



  global my_font
  global screen


  def double(num):
    global doubled_num 
    double_num= num*2
    print(double_num)

    return double_num

  a = 5
  new_variable = double(a)
  print(new_variable)




