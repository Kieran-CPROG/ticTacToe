#Kieran Uptagrafft
#9/26/24
#Toe Tic Tac

from tic_tac_toe import *
import random
taken = []

def computer(Tic, sheTaken):
  Flag = True
  while Flag:
    x = random.randint(1, 3)
    y = random.randint(1, 3)
    for z in taken:
      if z[0] == x or z[1] == y:
        pass
      else:
        taken.append([x, y])
        Flag = False

  Tic.place_token([x, y])
  return sheTaken

def main():
  TTT = TicTacToe()
  
  Flag = True
  while Flag:
    state = TTT.is_winner()
    
    try:
      if state[0] == 'o':
        print("Winner o")
        Flag = False
        break
      elif state[0] == 'x':
        print("Winner x")
        Flag = False
        break
    except:
      pass
    
    spot = True
    babyProof = True
    while babyProof:
      try:
        x = int(input("Enter X: "))
        y = int(input("Enter -Y: "))
        if x <= 3 and y <= 3:
          babyProof = False
      except:
        continue

    for z in taken:
      if z[0] == x and z[1] == y:
        spot = False
      else:
        pass
    if spot == False:
      print("Try Again")
      continue 
    elif 3 < x or 3 < y:
      print("Try Again")
      continue
    else:
      taken.append([x, y])
      TTT.place_token([x, y])
    
    
    computer(TTT, taken)
    print(TTT)

if __name__ == "__main__":
  main()