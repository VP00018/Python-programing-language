import random 
options = ("Rock","Paper","scissors")
# player = None
# computer = random.choice(options)
running = True

while running: 

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (Rock, Paper, Scissors): ")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's a Tie!")
    elif player == "Rock" and computer == "scissors":
        print("YOU WIN!")
    elif player == "Paper" and computer == "Rock":
        print("YOU WIN!")
    elif player == "scissors" and computer == "Paper":
        print("YOU WIN!")
    else:
        print("YOU LOSE!")

    play_again = input("Play Again? (y/n): ").lower()
    if not play_again == "y": 
        running = False

print("Thanks for Playing")

