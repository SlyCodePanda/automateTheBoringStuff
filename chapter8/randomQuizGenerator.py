#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generates 35 quiz files.
for quizNum in range(35) :
	# --- Create the quiz and answer key files. ---
	# The filenames for the quizzes will be capitalsquiz<N>.txt, where <N> is a unique number for the quiz that comes from quizNum, the for loop’s counter.
	# The answer key for capitalsquiz<N>.txt will be stored in a text file named capitalsquiz_answers<N>.txt.
	quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')				# Create file in write mode.
	answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')	# Create file in write mode.

	# --- Write out the header for the quiz. ---
	# create a quiz header for the student to fill out.
	quizFile.write('Name: \n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
	quizFile.write('\n\n')

	# --- Shuffle the order of the states. ---
	# A randomized list of US states is created using the random.shuffle() function, which randomly reorders the values in any list that is passed to it.
	states = list(capitals.keys())
	random.shuffle(states)

	# --- Loop through all 50 states, making a question for each. ---
	for questionNum in range(50) :
		# Get right and wrong answers.
		# Correct answer stored as a value in the capitals dictionary.
		correctAnswer = capitals[states[questionNum]]
		# To get the wrong answer, STEP 1: duplicate ALL the values in the capitals dictionary.
		wrongAnswers = list(capitals.values())
		# STEP 2: delete all the correct answers.
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		# STEP 3: select three random values from the list using the sample() function.
		wrongAnswers = random.sample(wrongAnswers, 3)
		# The full list of answer options is the combination of these 3 wrong answers with the correct answers.
		answerOptions = wrongAnswers + [correctAnswer]
		# Then the answer is randomized so that the correct answer isn't always choice D.
		random.shuffle(answerOptions)

		# --- Write the question and answer options to the quiz file. ---
		quizFile.write('%s. What is the captial of %s?\n' % (questionNum + 1, states[questionNum]))
		# Loops goes through integers 0 to 3 will write the answer options in the answerOptions list.
		for i in range(4) :
			# The expression 'ABCD'[i] treats the string 'ABCD' as an array and will evaluate to 'A', 'B', 'C', and then 'D' on each respective iteration through the loop.
			quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
		quizFile.write('\n')

		# --- Write the answer key to a file. ---
		# answerOptions.index(correctAnswer) will find the integer index of the correct answer in the randomly ordered answer options, and 'ABCD'[answerOptions.index(correctAnswer)] will evaluate to the correct answer's letter to be written to the answer key file.
		answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

	quizFile.close()
	answerKeyFile.close()