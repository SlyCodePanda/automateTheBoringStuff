# If user inputs name Joe, it will ask for a password. If they give the password 'swordfish', access is granted.
# If they give any other name, it will repeatedly ask 'Who are you?'.
# If they give the wrong password, they will go back to 'Who are you?' prompt.

while True :
    print( 'Who are you?')
    name = input()

    if name != 'Joe' :
        continue # If name isn't 'Joe', triggers continue statement. Which causes program to jump back to start of loop.
    print( 'Hello, Joe. What is the password? (It is a fish.)')
    password = input()

    if password == 'swordfish' :
        break # Exit loop. Goes to 'Access granted'.

print( 'Access granted.' )
