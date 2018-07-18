if name == 'Alice' :
    print('Hi Alice.')
elif age < 12 :
    print('You are not Alice, kiddo.')
elif age > 100 :
    print('You are not Alice, grannie')
elif age > 2000 :
    print('Unlike you, Alice is not undead, immortal vampire.')

# This would be a bug. Say if age = 3000, you would get the 'grannie' output.
# Because it gets to the 'age > 100' checker first, then exits.
