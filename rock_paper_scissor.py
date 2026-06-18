import random

print("================================")
print(" ROCK PAPER SCISSORS GAME ")
print("================================")

user_score = 0
computer_score = 0

while True:

    print("\nChoose:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter your choice (1/2/3): ")

    options = ["Rock", "Paper", "Scissors"]

    if choice == "1":
        user_choice = "Rock"
    elif choice == "2":
        user_choice = "Paper"
    elif choice == "3":
        user_choice = "Scissors"
    else:
        print("Invalid Choice!")
        continue

    computer_choice = random.choice(options)

    print("\nYour Choice:", user_choice)
    print("Computer Choice:", computer_choice)

    if user_choice == computer_choice:
        print("It's a Tie!")

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        print(" You Win!")
        user_score += 1

    else:
        print(" Computer Wins!")
        computer_score += 1

    print("\nScore Board")
    print("You      :", user_score)
    print("Computer :", computer_score)

    play_again = input("\nPlay Again? (yes/no): ")

    if play_again.lower() != "yes":
        break

print("\nFinal Score")
print("You      :", user_score)
print("Computer :", computer_score)

print("Thank you for playing!")
