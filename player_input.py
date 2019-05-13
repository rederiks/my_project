from board import *

def take_input(player_symbol):
  valid = False
  while not valid:
    player_choice = input("Where to put " + player_symbol + "? ")
    try:
      player_choice = int(player_choice)
    except:
      print('Wrong input. Choose number 1-9')
      continue
    if player_choice >= 1 and player_choice <=9:
      if (str(board[player_choice-1]) not in 'XO'):
        board[player_choice-1] = player_symbol
        valid = True
      else:
        print("This point is engaged")
    else:
      print('Wrong input. Choose number in range 1-9')
