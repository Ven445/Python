import random

def play_game():
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"
    choices = [rock, paper, scissors]
    user_score = 0
    computer_score = 0
    print("Welcome to Rock-Paper-Scissors Game")
    print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock.\n")
    while True:
        choose = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n")
        if not choose.isdigit() or int(choose) not in [0, 1, 2]:
            print("Invalid input! Please enter 0, 1, or 2.\n")
            continue
        choose = int(choose)
        print(f"You chose: {choices[choose]}")
        computer = random.randint(0, 2)
        print(f"Computer chose: {choices[computer]}")
        if choose == computer:
            print("It's a draw!\n")
        elif (choose == 0 and computer == 2) or (choose == 1 and computer == 0) or (choose == 2 and computer == 1):
            print("You win\n")
            user_score += 1
        else:
            print("Computer wins\n")
            computer_score += 1
        print(f"Your Score: {user_score} | Computer score: {computer_score}\n")
        again = input("Do you want to play again? (y/n): ").lower()
        if again != "y":
            print("\nFinal Score:")
            print(f"Your: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("Congratulations! You win!!")
            elif computer_score > user_score:
                print("Computer wins the game! Better luck next time!")
            else:
                print("game is draw!!")
            break
play_game()

