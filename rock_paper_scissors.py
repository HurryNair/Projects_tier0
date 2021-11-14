import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break
    else:
        if user_input not in ["rock", "paper", "scissors"]:
            print("Bad input. Try again")
            continue

        random_number = random.randint(0,2)
        # rock: 0, paper: 1, scissor:2
        computer_pick = options[random_number]
        print(f"Computer picked {computer_pick} .")

        if user_input == "rock" and computer_pick == "scissors":
            print("You win!")
            user_wins += 1
        
        elif user_input == "scissors" and computer_pick == "paper":
            print("You win!")
            user_wins += 1

        elif user_input == "paper" and computer_pick == "rock":
            print("You win!")
            user_wins += 1
        
        else:
            print("You lose!")
            computer_wins += 1

    print(f"Scores: You score: {user_wins} Computer scores: {computer_wins}")
    winner = max(user_wins, computer_wins)

    print(f"The winner is {winner}")
print("Good Bye!")