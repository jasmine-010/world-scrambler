import random

word_bank = [
        ("syntax", "One missing bracket, and Python hits me with a ______ error."),
    ("meeting", "That ninety-minute ________ could havenbeen an e-mail."),
    ("prototype", "It's just an early ________, please ignore it.")
]

ROUNDS = 2
round_num = 1
used = []
score = 0

while round_num <= ROUNDS:
    word, hint = random.choice(word_bank)
    letters = list(word)
    random.shuffle(letters)
    scrambled_word = "".join(letters).upper()

    print()
    print(f"This is round {round_num}")
    print()
    print(f"Scrambled word: {scrambled_word}")
    
    player_input = input("Enter your answer (Note: You can also skip this word or ask for a hint or quit): ").strip().lower()
    
    print()

    while (word, hint) in used:
        word, hint = random.choice(word_bank)
        
    used.append((word, hint))

    if player_input == "hint":
        print(f"Here's the hint: {hint}")

        player_input = input("Guess again: ").strip().lower()

    if player_input == "quit":
       print("Thanks for playing!")
       break
    
    if player_input == "skip":
        print(f"Skipped: {word}")
        print()
    elif player_input == word:
        print(f"Correct: {word.strip().upper()}")
        score +=1

        print()
    else: 
        print(f"Incorrect: {word.strip().upper()}")

    round_num += 1
print(f"Final Score: {score}")
if score == 2:
        print(f"You did well!")
elif score == 1: 
        print(f"Mid!")
else:
        print("Try again!")


        


          

