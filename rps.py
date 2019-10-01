# Jacob Pfaff
# Rock Paper Scissors

# Welcome message
# 1. Prints a welcome message
# 2. Prompts for a name

#Game loop
#print score
#prompt for player choice
#get the computer choice (random)
#compare
#print results
#change score variable


# Score Screen
# Print "Score: "
# Print the player score using the name
# Print the computer score
import random
#Variables
pScore = 0
cScore = 0
ties = 0
computerChoices = ["rock" , "paper" , "scissors"]




#Welcome message
print("Welcome to Rock, Paper, Scissors")
playerName = input("What is your name?:")
#Print Score
def printScore():
	print("Score:")
	print(playerName + ":" +str(pScore))
	print("Computer Score:" + str(cScore))
	print("Ties:"+ str(ties))

#Game Loop
while True:
	# print the score
	printScore()
	#prompt for player choice
	pChoice = input("Enter 'r' for rock, 'p' for paper, 's' for scissors or 'q' to quit:")
	#get the computer choice (random)
	cChoice = random.choice(computerChoices)
	#compare
	#compare pChoice to "q"
	# 1. break out
	if pChoice == "q":
		break
	#compare pChoice to "r"
	# compare rock to computer choice
	elif pChoice == "r":
		print("You picked rock")
		if cChoice =="rock":
			print("Computer picked rock")
			print("This is a tie")
			ties = ties + 1
		elif cChoice == "paper":
			print("Computer picked paper")
			print("Paper beats rock")
			cScore = cScore + 1  
		else: # scissors is left
			print("Computer picked scissors")
			print("Rock beats scissors")
			pScore = pScore + 1
	#compare pChoice to "p"
	elif pChoice == "p": #player picks paper
		print("You picked paper")
		print("Paper beats scissors")
		pScore = pScore + 1
	elif pChoice == "s":
		print("You picked scissors")
		if cChoice == "p"
		print("Computer picked paper ")
		print("Scissors beats paper")
		pScore = pScore + 1
	else:
		print("You picked something not on the list")


	#compare pChoice to "s"
	#print results
	#change score variable

printScore()