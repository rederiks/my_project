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

main(board)