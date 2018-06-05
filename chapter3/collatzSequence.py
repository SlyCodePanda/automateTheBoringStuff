# Exploring the 'Collatz Sequence'.

# If number is even, print number // 2 and returns this value.
# If number is odd, print and return 3 * number + 1.
def collatz( number ) :
  number = int(number)

  # number is even.
  if number % 2 == 0 :
    print( str(number // 2) )
    return number // 2
  # number is odd.
  else :
    print( str(3 * number + 1) )
    return 3 * number + 1

# Lets user type in an integer and keeps calling collatz() on that number until the funciton returns the value 1.
def main() :
  print( "Enter in a number: " )

  # Error handling to make sure number entered is an int.
  while True :
    try:
      numb = input()
      break
    except NameError :    # Stops user from entering a string.
      print( 'Please enter an integer.' )
    except SyntaxError :  # Stops user from entering a symbol, such as '@', '$', '?', etc.
      print( 'Please enter an integer.' )

  numb = collatz(numb)
  while numb != 1 :
    numb = collatz(numb)

if __name__ == "__main__":
  main()