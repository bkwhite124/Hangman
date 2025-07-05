import random
user_name = input("What is your name? ")
print(f'Hello {user_name} time to play hangman')

words = ['rainbow', 'zebra', 'poodle', 'girlfriend', 'earth', 'football', 'weightlifting',
         'godzilla', 'programming', 'chicago', 'happiness', 'dog', 'apartment', 'friday', 
         'ohio', 'fight', 'program', 'germany']

random_word = random.choice(words)

guesses = ''
turns = 12 

while turns > 0:
    failed = 0
    for char in random_word:
        if char in guesses:
            print(char, end='')
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You win")
        print("The word is: ", random_word)
        break
    print()
    guess = input("guess a character:")
    guesses += guess 
    if guess not in random_word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, "more guesses")
        if turns == 0:
            print("You loose")


