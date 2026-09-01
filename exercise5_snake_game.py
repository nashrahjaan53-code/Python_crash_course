##exercise gun:
import random
def check_winner(user, computer):
    if user == computer:
        return "Draw"

    if (
        (user == "snake" and computer == "water") or
        (user == "water" and computer == "gun") or
        (user == "gun" and computer == "snake")
    ):
        return "You win"

    return "Computer wins"

def play_game():
    options = ["snake", "water", "gun"]

    user = input("Choose snake, water, or gun: ").lower()

    if user not in options:
        print("Invalid choice!")
        return

    computer = random.choice(options)

    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

    result = check_winner(user, computer)
    print(result)


play_game()

    
