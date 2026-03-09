#Python quiz game 

#tuple of questions
questions = ("How many planets are there?: ",
             "Who is the best football player in the world?: ",
             " Which animal lays the largest eggs?:",
            " How many bones are in the human body?: ",
            " Which planet is the biggest?: ",
           "  Which football team is the only team to win every uefa competition?:")

#2D tuple of options
options = (("A. 7", "B. 8", "C. 6", "D. 9"),
           ("A. CR7", "B. Neymar", "C. Messi", "D. Pele"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. 206", "B. 207", "C. 209", "D. 208"),
           ("A. Mars", "B. Jupiter", "C. Earth", "D. Neptune"),
           ("A. Real Madrid", "B. Bayern Munich", "C. Chelsea", "D. Liverpool"))

#A tuple of answers
answers = ("B", "A", "D", "A", "B", "C")

#A list of guesses
guesses = []
score = 0

#keeps track on wc question we on
question_num = 0 

for question in questions: 
    print("-------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG Dumb-ahh!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1     


print("-------------")
print("   RESULTS   ")
print("-------------")

print("answers: ", end="")
for answer in answers: 
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guess: 
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your is: {score}%")
