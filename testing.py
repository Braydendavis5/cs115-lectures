age = 15
age2 = 15

if age > 21:
  print("You are an adult")
  Print("You are old")
else:Print("You are young.")


age = 30 #difference = 15
difference = age - age2
if difference >= 0:
  print("Positive or zero")
elif difference > 5:
  print("big number")
elif difference < 0:
  print("negative")

if difference > 5:
  print("big number")


counter = 0
while counter <= 10:
  print(counter)
  #increment counter
  #counter = counter + 1 
  counter += 1

#for loop
inventory = ["sword", "sheild","key"]
for item in inventory:
  print(item)

# boolean operaters
is_game_paused = False
is_dead = False

if is_game_paused or is_dead:
  print("game paused")
else:
  print("game not paused")

if is_game_paused and is_dead:
  print("game over")

health = 50
if is_dead <= 0:
  is_dead = true