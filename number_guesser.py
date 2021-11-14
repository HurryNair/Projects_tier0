import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0")
        exit()
else:
    print("Please enter a number next time")

random_number = random.randint(0, top_of_range)
print(random_number)

guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
    
    if user_guess == random_number:
        print("You got it!")
        break
    else:
        print("You got it wrong!")

print(f"You got it in {guesses} guesses")