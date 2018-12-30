def isInteger(value):
  try:
    int(value)
    return True
  except Exception:
    return False