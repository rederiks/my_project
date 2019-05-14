from board import *
from player_input import *

def check_field(board):
  field_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,8))
  for field in field_coord:
    if board[field[0]] == board[field[1]] == board[field[2]]:
      return board[field[0]]
  return False

def main(board):
  counter = 0
  win = False
  while not win:
    draw_board(board)
    if counter % 2 == 0:
      take_input('X')
    else:
      take_input("O")
    counter += 1
    if counter > 4:
      tmp = check_field(board)
      if tmp:
        print(tmp, 'win')
        win = True
        break
      if counter == 9:
        print("Draw!")
        break
  draw_board(board)
print('Help:\nrules - rules of the game\nstart - start to play\nexit - stop program')

while True:

  choice = input()
  if choice == 'rules':
    print('The object of Tic Tac Toe is to get three in a row. You play on a three by three game board. The first player is known as X and the second is O. \nPlayers alternate placing Xs and Os on the game board until either oppent has three in a row or all nine squares are filled. \nX always goes first, and in the event that no one has three in a row, the stalemate is called a cat game.')
  if choice == 'start':
    main(board)
  if choice == 'exit':
    break