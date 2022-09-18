# gol.py
# Yenmin Young
# CSCI 77800 Fall 2022
# Collaborators: 
# Consulted: ThinkPython, W3Schools, tutorialspoint.com

import random
import numpy as np
from array import *

print("Welcome to Conway's Game of Life")
print("There is a special breed of bacteria growing (Don't worry, they're friendly)")
print("If a cell has 2 or 3 living neighbors, it will survive.")
print("If it has more than 3 neighbors, it'll suffocate and DIE")
print("If it has less than 2 neighbors, it'll be lonely and DIE")
print("If an empty lot has exactly 3 living neighbors next to it, it'll magically generate a new life. Babies are made!")
print("")

# Let's make a board
size = 5
initialPopulation = 7
generations = 3
board = []
nestedboard = []
countBoard = []
newBoard = []

"""
# Something about the code below makes it impossible to make a randomly generated life so we will manually make a board
for i in range(size):
  nestedboard.insert(0, i)
print(nestedboard)
print("")
for i in range(size):
  board.insert(0, nestedboard)
print(board)
print("")
"""
# Make a manual board
for i in range(size):
  board.insert(0, [0, 0, 0, 0, 0])

# Make a board that keeps track of neighbors
for i in range(size):
  countBoard.insert(0, [0, 0, 0, 0, 0])  

# Randomly insert life in the first generation
for i in range (initialPopulation):
  x = random.randrange(0, size)
  y = random.randrange(0, size)
  board[y][x] = 1

# Print the first generation
print("Generation 1")
for r in board:
  for c in r:
    print(c, end=" ")
  print()

# Copy old board to new board
newBoard = board

# Begin regeneration

for x in range(generations):

  # Count number of neighbors
  for row in range(size):
    for col in range(size):
      count = 0
      # Check to see how many living neighbors
      for i in range(-1, 2):
        for j in range(-1, 2):
          if row+i>=0 and row+i<size:
            if col+j>=0 and col+j<size:          
              if i!=0 or j!=0:
                if board[row+i][col+j] == 1:
                  count += 1
      # print(row, ",", col, ": I have", count, "neighbors.")
      countBoard[row][col] = count
  
  # Display neighbors count
  """
  print("")
  print("CountBoard:")
  for r in countBoard:
    for c in r:
      print(c, end=" ")
    print()
  """
  
  # Next Generation rules
  for row in range(size):
    for col in range(size):
    # If alive and has 2 or 3 neighbors, remain same
      # If alive and has <2 or >3 neighbors, change to 0
      # If dead and has == 3 neighbors, change 1
      if board[row][col] == 1:
        if countBoard[row][col]<2 or countBoard[row][col]>3:
          newBoard[row][col] = 0
      else:
        if countBoard[row][col] == 3:
          newBoard[row][col] = 1
  
  # Print the next generation
  print("")
  print("Generation", x+2)
  for r in newBoard:
    for c in r:
      print(c, end=" ")
    print()
  
  board = newBoard
