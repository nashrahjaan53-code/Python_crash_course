#import random
#def number_guessing_game():
   # """A simple number guessing game"""
    #print("🎮 Welcome to the Number Guessing Game!")
   # print("I'm thinking of a number between 1 and 100.")
    #secret_number = random.randint(1, 100)
    #attempts = 0
   # max_attempts = 10
    
    #while attempts < max_attempts:
       # try:
            #guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}. Enter your guess: "))
           # attempts += 1
            
           # if guess < secret_number:
          #      print("📈 Too low! Try a higher number.")
         #   elif guess > secret_number:
        #        print("📉 Too high! Try a lower number.")
       #     else:
      #          print(f"🎉 Congratulations! You guessed the number in {attempts} attempts!")
     #           return
        
    #    except ValueError:
   #         print("⚠️ Please enter a valid number!")
    
  #  print(f"\n💔 Game Over! The number was {secret_number}.")


#if __name__ == "__main__":
 #   number_guessing_game()




simport random

def rock_paper_scissors():
    """Rock, Paper, Scissors game"""
    choices = ["rock", "paper", "scissors"]
    
    print("🪨 📄 ✂️  Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors'. Type 'quit' to exit.")
    
    score = {"player": 0, "computer": 0}
    
    while True:
        print(f"\n📊 Score - You: {score['player']} | Computer: {score['computer']}")
        player_choice = input("\nYour choice: ").lower().strip()
        
        if player_choice == "quit":
            print("\nThanks for playing! Final score:")
            print(f"👤 You: {score['player']} | 🤖 Computer: {score['computer']}")
            break
        
        if player_choice not in choices:
            print("❌ Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"🤖 Computer chose: {computer_choice}")
        
        # Determine winner
        if player_choice == computer_choice:
            print("🤝 It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("🎉 You win this round!")
            score["player"] += 1
        else:
            print("💻 Computer wins this round!")
            score["computer"] += 1

# Run the game
if __name__ == "__main__":
    rock_paper_scissors()
