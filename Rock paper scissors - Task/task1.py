import random

options=("rock","paper","scissors")
running=True

while running:
    player=None
    computer=random.choice(options)


    while player not in options:
        player = input("Enter a choice(rock,paper,scissors): ")

    print(f"player.{player}")
    print(f"computer.{computer}")

    if player ==computer:
        print("its a tie!")
    elif player =="rock"and computer == "paper":
        print("paper wins")
    elif player=="rock" and computer=="scissors":
        print("Rock wins")
    elif player=="paper" and computer=="scissors":
        print("Scissor wins")
    else:
        print("You loose!")
    if not input("play again? (Y/n):").lower()=='y':
        running = False
print("Thanks for playing!")    