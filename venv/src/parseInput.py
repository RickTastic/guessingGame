import isInteger
def parseInput(guess):
  try:
    message = dict()
    if isInteger.isInteger(guess):
      if int(guess) < 0 or int(guess) > 100:
        message['errorMessage'] = "Please enter an integer in the range 0...100."
        message['isValid'] = False
        message['value'] = None
        return message
      else:
        message['errorMessage'] = ""
        message['isValid'] = True
        message['value'] = int(guess)
        return message
    elif type(guess) == str and (guess == 'q' or guess == 'Q'):
      message['errorMessage'] = ""
      message['isValid'] = True
      message['value'] = guess
      return message
    else:
      message['errorMessage'] = str(guess) + " is not a valid integer."
      message['isValid'] = False
      message['value'] = None
      return message
  except Exception:
    raise Exception("Unknown Exception. Please restart the application")