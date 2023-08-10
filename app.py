import random
import time

computer_score = 0
human_score = 0
print("Can you beat me in Rock Paper Scissors? First to 3, wins!")


while human_score < 3 and computer_score < 3:
	time.sleep(1.5)
	computer_choice = random.choice(["Rock", "Paper", "Scissors"]).lower()
	human_choice = input("Rock, paper or scissors? \n").lower()

	if human_choice == computer_choice:
		human_score += 1
		print("\nWell done. " + str(human_score) + " - " + str(computer_score))
	elif human_choice not in ["rock", "paper", "scissors"]:
		print("\nEnter either rock, paper or scissors")
	else:
		computer_score += 1
		print("\nHaha!! " + str(human_score) + " - " + str(computer_score))


time.sleep(1)

if human_score > computer_score:
	print("\nYou beat me!! Well done :)")
else:
	print("I beat you")