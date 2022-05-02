def game(prevPicks, count):#gets user input of square they want to select
  if (count%2 == 1):#rotates between player 1 and 2
    while True:
      userPick = int(input("Player 1: Enter the number in the square that you want to fill(See Reference)\n"))
      if prevPicks[userPick] >= 1: #checks if selected square is filled
        print("Pick an unused square")
      else:
        break
    prevPicks[userPick] = 1 #sets user pick to the square on the prevPicks array
  else:
    while True:
      userPick = int(input("Player 2: Enter the number in the square that you want to fill(See Reference)\n"))
      if prevPicks[userPick] >= 1: #checks if selected square is filled
        print("Pick an unused square")
      else:
        break
    prevPicks[userPick] = 2 #sets user pick to the square on the prevPicks array
  return prevPicks #returns the updated list
  
def board(prevPicks):#prints board 
  print(100 * "\n")
  print("What number to enter for each square:")
  print("\u0332".join("  0|1|2\n 3|4|5"))#Use the join function to get underlines in the top two rows to make the horizontal marks on the tic tac toe board
  print("  6|7|8\n")
  board = "\n {0}|{1}|{2}\n {3}|{4}|{5}".format(prevPicks[0], prevPicks[1], prevPicks[2], prevPicks[3], prevPicks[4], prevPicks[5])
  print("\u0332".join(board))
  print("  {0}|{1}|{2}\n".format(prevPicks[6], prevPicks[7], prevPicks[8])) #prints the active game board 

def checkWin(list):#Checks all possible win combinations
  if list[0] == 1 and list[1] == 1 and list[2] == 1:
    return 1
  elif list[3] == 1 and list[4] == 1 and list[5] == 1:
    return 1
  elif list[6] == 1 and list[7] == 1 and list[8] == 1:
    return 1
  elif list[0] == 1 and list[3] == 1 and list[6] == 1:
    return 1
  elif list[1] == 1 and list[4] == 1 and list[7] == 1:
    return 1
  elif list[2] == 1 and list[5] == 1 and list[8] == 1:
    return 1
  elif list[0] == 1 and list[4] == 1 and list[8] == 1:
    return 1
  elif list[2] == 1 and list[4] == 1 and list[6] == 1:
    return 1
  elif list[0] == 2 and list[1] == 2 and list[2] == 2:
    return 2
  elif list[3] == 2 and list[4] == 2 and list[5] == 2:
    return 2
  elif list[6] == 2 and list[7] == 2 and list[8] == 2:
    return 2
  elif list[0] == 2 and list[3] == 2 and list[6] == 2:
    return 2
  elif list[1] == 2 and list[4] == 2 and list[7] == 2:
    return 2
  elif list[2] == 2 and list[5] == 2 and list[8] == 2:
    return 2
  elif list[0] == 2 and list[4] == 2 and list[8] == 2:
    return 2
  elif list[2] == 2 and list[4] == 2 and list[6] == 2:
    return 2
  elif list[0] >= 1 and list[1] >= 1 and list[2] >= 1 and list[3] >= 1 and list[4] >= 1 and list[5] >= 1 and list[6] >= 1 and list[7] >= 1 and list[8] >= 1: #Checks Tie
    return 3
  else:#if no one has won, return 0
    return 0

def playAgain():#Restart method, stops software if no
  while True:
    ans = input("Would you like to play again?(yes/no)\n")
    if ans.lower() == "yes" or ans.lower() == "no":
      break
    else:
      print("Invalid input, try again.")
  return ans

def main():
  prevPicks = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  winCondition = 0
  count = 1 #initializing variables 
  while True:
    board(prevPicks) #calls board method so it pops up every loop first
    winCondition = checkWin(prevPicks) #Check win BEFORE we get user input
    if winCondition == 1 or winCondition == 2:#if a player wins, print they won and call the play again method 
      print("Congrats player {}, you are the winner!".format(winCondition))
      ans = playAgain()
      if ans.lower() == 'yes': #restarts all variables to play again
        prevPicks = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        winCondition = 0
        count = 1
      else: #Ends program
        print("Program Ending...")
        break
    elif winCondition == 3:
      print("The game ends in a tie!")
      ans = playAgain()
      if ans.lower() == 'yes': #restarts all variables to play again
        prevPicks = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        winCondition = 0
        count = 1
      else: #Ends program
        print("Program Ending...")
        break
    else: #if no one has one, then call the game method to get the players input and set it equal to the precPicks array
      prevPicks = game(prevPicks, count)
      count += 1 #rotates players 

if __name__ == "__main__":
  main()