def process(number):
  if number % 4 == 0:
    return True
    if number % 100 == 0:
       return True
       if number % 400 == 0:
          return 'Leap Year'
       else:
        return False
    else:
      return False
  else:
    return False
    
