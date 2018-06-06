import random

print( 'Ask the magic 8 ball a quesiton...')
question = raw_input()

messages = ['It is certain',
			'It is decidedly so.',
			'Yes definitely.',
			'Reply hazy try again.',
			'Ask again later.',
			'Concentrate and ask again.',
			'My reply is no.',
			'Outlook not so good',
			'Very doubtful.']

# Give random number between 0 and the length of the messages list minus 1.
# Use that number as the index for printing one of the messages.
randomNumb = random.randint( 0, len(messages) - 1)
print( messages[randomNumb] )