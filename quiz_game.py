# Ask the users a bunch of questions & maintain a score

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    exit()

print("Okay, let's play!")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")