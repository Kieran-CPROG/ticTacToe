#Kieran Uptagrafft
#9/26/24
#Toe Tic Tac


import random
tokens = ['x', 'o']
class TicTacToe:

  def __init__(self):
    self.__board = [[[" "] for j in range(3)]for i in range(3)]
    self.__turn = random.choice(['x', 'o'])

  #display the game current board in a nice way
  def __str__(self):
    try:
      a = f"    {self.__board[0][0][0]}|{self.__board[0][1][0]}|{self.__board[0][2][0]}"
      b = "  -----------"
      c = f"    {self.__board[1][0][0]}|{self.__board[1][1][0]}|{self.__board[1][2][0]}"
      d = "  -----------"
      e = f"    {self.__board[2][0][0]}|{self.__board[2][1][0]}|{self.__board[2][2][0]}"
      return f"\n{a}\n{b}\n{c}\n{d}\n{e}\n"
    except:
      pass
#Places the tocken on the board
  def place_token(self, placement):
    #if len(self.__board[placement[1] - 1][placement[0] - 1]) == 1:
      #pass
    #else:
    self.__board[placement[1] - 1][placement[0] - 1].clear()
    self.__board[placement[1] - 1][placement[0] - 1].append(self.__turn)
    if self.__turn == 'x':
      self.__turn = 'o'

    else:
      self.__turn = 'x'
#Check for the three in a row
  def __check_win(self):
    #Top Row
    if self.__board[0][0] == self.__board[0][1] == self.__board[0][2]:
      return self.__board[0][0]
    #Middle Row
    elif self.__board[1][0] == self.__board[1][1] == self.__board[1][2]:
      return self.__board[1][0]
    #Bottom Row
    elif self.__board[2][0] == self.__board[2][1] == self.__board[2][2]:
      return self.__board[2][0]
    #Left col
    elif self.__board[0][0] == self.__board[1][0] == self.__board[2][0]:
      return self.__board[0][0]
    #Middle Col
    elif self.__board[0][1] == self.__board[1][1] == self.__board[2][1]:
      return self.__board[0][1]
    #Right col
    elif self.__board[0][2] == self.__board[1][2] == self.__board[2][2]:
      return self.__board[0][2]
    #first slant
    elif self.__board[0][0] == self.__board[1][1] == self.__board[2][2]:
      return self.__board[0][0]
    #Second Slant
    elif self.__board[0][2] == self.__board[1][1] == self.__board[2][0]:
      return self.__board[0][2]

#calls the check win then retuns who wins
  def is_winner(self):
    win = self.__check_win()
    return win
