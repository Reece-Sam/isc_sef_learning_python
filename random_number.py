import random

# low = 1
# high = 100
# options = ("rock", "paper", "scissors")
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "12", "J", "Q", "B", "A", "K"]

# number = random.randint(low, high)
# number = random.random()
# option = random.choice(options)
# random.shuffle(cards)

# print(cards)


#==== EXERCISE ====
#Number guessing game 

# lowest_num = 1
# highest_num = 100 
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True 

# print("Python Number Guessing Game")
# print("------------------------------")
# print(f"Select a number between {lowest_num} and {highest_num} ")

# while is_running:

#     guess = input("Enter your guess: ")

#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1

#         if guess < lowest_num or guess > highest_num:
#           print("That number is out of range")
#           print(f"Select a number between {lowest_num} and {highest_num}: ")

#         elif guess < answer: 
#             print("Too low! Try again!")
#         elif guess > answer:
#             print("Too high! Try again!")
#         else:
#             print(f"CORRECT! The answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             is_running = False

#     else:
#         print("Invalid Guess")
#         print(f"Select a number between {lowest_num} and {highest_num}: ")

#=================================================================================

#=== EXERCISE ===
#Rock, Paper ,Scissors

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice(rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It is a tie")

    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")

    else:
        print("You lose Sucker!!!!")
    
    play_again = input("Do u want to play again? (y/n): ").lower()
    if not play_again == "y":
        running = False 
           #OR
    # if not input("Play again? (y/n): ").lower() == "y":
    #     running = False 

print("=====================================")
print("Thanks for playing!")

