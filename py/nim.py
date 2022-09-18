# nim.py
# Yenmin Young
# CSCI 77800 Fall 2022
# Collaborators: None
# Consulted: ThinkPython


import random

stones = 12
stonesTaken = 0

print("Each player can only take 1-3 stones per turn.")
print("The goal is to be the last one to take a stone.")
print("There are", stones, "stones in the bag.")
print("")

while stones > 0:
  stonesTaken = int(input("How many stones do you want to take? "))
  # Check to see if player took too many stones (either more than 3 or more than the number of available stones)
  while stonesTaken < 1 or stonesTaken > 3 or stonesTaken > stones:
    print ("stop in the name of loveeeee")
    print ("remember the rules: only take 1-3 stones. try again you dodo")
    print("")
    stonesTaken = int(input("How many stones do you want to take? "))

  stones -= stonesTaken
  
  print("There are now", stones, "stones left in the bag.")
  # Check if there are 0 stones now
  if stones == 0:
    print("Congrats! You won!")
    exit()
  
  machineTaken = random.randrange(1,4)
  stones -= machineTaken
  print("The computer took", machineTaken, "stones.")
  print("There are now", stones, "stones left in the bag.")
  # Check if there are 0 stones now
  if stones == 0:
    print("Womp womp... You lost :(")

  print("")
  
print("GAME OVER")