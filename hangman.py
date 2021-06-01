import random

with open("movie_names_2.txt",'r') as f:
	films = f.readlines()

word = random.choice(films)[:-1] #name of the film


allowed_errors = int()
choice = int(input("Select game difficulty: 1.Easy \t 2.Intermediate \t 3.Hard : \n ")) #setting up difficulty level

if choice == 1:
	allowed_errors = 7
elif choice == 2:
	allowed_errors = 5
elif choice == 3:
	allowed_errors = 3
else:
	print("invalid choice")
	exit()


guesses = [] #contains all the letters that we have already tried
done = False #true when the word is guessed

while not done:
	for letter in word:
		if letter.lower() in guesses:
			print(letter, end = " ")
		else :
			print("_", end = " ")
		print(" ", end = " ")
	guess= input("\n Allowed number of errors left : {} next guess: ".format(allowed_errors))
	guesses.append(guess.lower())

	if guess.lower() not in word.lower():
		allowed_errors -= 1
		if allowed_errors == 0 :
			break

	done = True

	for letter in word:
		if letter.lower() not in guesses:
			done = False

if done:
	print("You found the movie it was ", word)
else:
	print("Game Over! The movie was ", word)
