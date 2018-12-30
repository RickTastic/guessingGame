import random
import parseInput
def guessingGame():
  """
  This is the logic for the guessing game. Advanced hints and features to be added.
  author: Ashai Ramsunder
  param guess: An integer guess
  return:
  """
  guess = input()
  computerRandomNumber = random.randrange(0, 100)
  countGuess = 1
  done = False
  while not done:
    typeCheck = parseInput.parseInput(guess)
    if typeCheck['isValid']:
      guess = typeCheck['value']
      if guess == computerRandomNumber:
        print("Congratulation's, you win!! My random number is: ", computerRandomNumber)
        print("The number of tries taken to guess my number is: ", countGuess)
        tryAgain = input("Would you like to try again? (y/n)\n")
        if tryAgain == 'n' or tryAgain == 'N':
          break
        else:
          computerRandomNumber = random.randrange(0, 100)
          print("I have selected a new number between 0 and 100, try and guess the number or press q to quit!")
          print("Here is a free hint!")
          countGuess = 1
      if guess == 'q' or guess == 'Q':
        break
      if computerRandomNumber > 50 and computerRandomNumber < 75:
        guess = input("Hint: Your number is between 51 and 74. Guess again!\n")
        countGuess += 1
        print()
      if computerRandomNumber > 75:
        guess = input("Hint: Your number is greater than 75. Guess again!\n")
        countGuess += 1
        print()
      if computerRandomNumber > 25 and computerRandomNumber < 50:
        guess = input("Hint: Your number is between 26 and 49. Guess again!\n")
        countGuess += 1
        print()
      if computerRandomNumber < 25:
        guess = input("Hint: Your number is less than 25. Guess again!\n")
        countGuess += 1
        print()
    else:
      done = True
      print(typeCheck['errorMessage'])
  print("Exiting...")