import welcomeScreen
import guessingGame
import time
def main():
  startTime = time.time()
  print("Initialising Welcome Screen...\n")
  welcomeScreen.welcomeScreen()
  print("\nIt is time to guess!!!\n")
  guessingGame.guessingGame()
  endTime = time.time()
  timePlayed = endTime - startTime
  print("Total time played: ", timePlayed)

if __name__ == "__main__":
  main()