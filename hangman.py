# A command-line hangman game.

import random
import csv


# Read the CSV file and generate a random word
with open("words.csv", "r") as file:
    reader = csv.reader(file)
    randomWord = random.choice(list(reader))

# Introduction
print("|----------------------------------------------------------|")
print("|-All words contain only 5 letters.                        |")
print("|-You have 10 chances to guess the letters.                |")
print("|-You can make 5 word guesses by typing 'guess'.           |")
print("|-You can take 2 hints by typing 'hint'.                   |")
print("|----------------------------------------------------------|")

foundLetters = []
usedLetters = []

guesscounter = 0
hintcounter = 0
wrongattempts = 0

# Keep prompting the user with a while loop
while True:

    # Get user's letter guesses
    letter = input("Letter: ")

    # Add guessed letters into usedLetters list
    if not letter[0] in usedLetters:
        usedLetters.append(letter[0])

    # Word guesses
    if letter == "guess":
        usedLetters.remove("g")  # Remove "g" letter (which is letter[0]) from usedLetters list
        guesscounter += 1
        guess = input("Guess: ")

        if guesscounter > 5:
            print("Sorry, you've made 5 guesses already.")
            print(f"The word was '{randomWord[1]}'.")
            break

        if guess == randomWord[1]:
            print("CORRECT!")
            break
        else:
            print("Sorry, that was not the word.")
            print("------------------------------------------------------------")
            continue

    # Hints
    if letter == "hint":
        usedLetters.remove("h")  # Remove "h" letter (which is letter[0]) from usedLetters list
        hintcounter += 1

        if hintcounter == 1:
            hint1 = randomWord[1][0]
            if not hint1 in foundLetters:
                foundLetters.append(randomWord[1][0])
            print(f"{hint1} _ _ _ _")
            print("------------------------------------------------------------")
            continue

        elif hintcounter == 2:
            hint2 = randomWord[1][4]
            if not hint2 in foundLetters:
                foundLetters.append(randomWord[1][4])
            print(f"_ _ _ _ {hint2}")
            print("------------------------------------------------------------")
            continue

        elif hintcounter > 2:
            print("Sorry, you can take only 2 hints.")
            continue

    # Compare guessed letters to randomWord's letters
    if letter[0] in randomWord[1]:
        if not letter[0] in foundLetters:
            foundLetters.append(letter[0])
            print("This letter exists!")
            print(f"Found Letters: {', '.join(foundLetters)}")
            print(f"Used Letters: {', '.join(usedLetters)}")
            print("------------------------------------------------------------")
    else:
        wrongattempts += 1

        # Print hangman, according to wrong attempts
        if wrongattempts == 1:
            print("This letter does not exist.")
            print(" ______")
            print(" |/")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("_|_")
            print(f"Found Letters: {', '.join(foundLetters)}")
            print(f"Used Letters: {', '.join(usedLetters)}")
            print("------------------------------------------------------------")

        elif wrongattempts == 2:
            print("This letter does not exist.")
            print(" ______")
            print(" |/   |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("_|_")
            print(f"Found Letters: {', '.join(foundLetters)}")
            print(f"Used Letters: {', '.join(usedLetters)}")
            print("------------------------------------------------------------")

        elif wrongattempts == 3:
            print("This letter does not exist.")
            print(" ______")
            print(" |/   |")
            print(" |    |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("_|_")
            print(f"Found Letters: {', '.join(foundLetters)}")
            print(f"Used Letters: {', '.join(usedLetters)}")
            print("------------------------------------------------------------")

        elif wrongattempts == 4:
            print("This letter does not exist.")
            print(" ______")
            print(" |/   |")
            print(" |    |")
            print(" |   (_)")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("_|_")
            print(f"Found Letters: {', '.join(foundLetters)}")
            print(f"Used Letters: {', '.join(usedLetters)}")
            print("------------------------------------------------------------")

        elif wrongattempts == 5:
            print("This letter does not exist.")
            print(" ______")
            print(" |/   |")
            print(" |    |")
            print(" |   (_)")
            print(" |    |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("_|_")
            print(f"Found Letters: {', '.join(foundLetters)}")
            print(f"Used Letters: {', '.join(usedLetters)}")
            print("------------------------------------------------------------")

        elif wrongattempts == 6:
            print("This letter does not exist.")
            print(" ______")
            print(" |/   |")
            print(" |    |")
            print(" |   (_)")
            print(" |   \|")
            print(" |")
            print(" |")
            print(" |")
            print("_|_")
            print(f"Found Letters: {', '.join(foundLetters)}")
            print(f"Used Letters: {', '.join(usedLetters)}")
            print("------------------------------------------------------------")

        elif wrongattempts == 7:
            print("This letter does not exist.")
            print(" ______")
            print(" |/   |")
            print(" |    |")
            print(" |   (_)")
            print(" |   \|/")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("_|_")
            print(f"Found Letters: {', '.join(foundLetters)}")
            print(f"Used Letters: {', '.join(usedLetters)}")
            print("------------------------------------------------------------")

        elif wrongattempts == 8:
            print("This letter does not exist.")
            print(" ______")
            print(" |/   |")
            print(" |    |")
            print(" |   (_)")
            print(" |   \|/")
            print(" |    |")
            print(" |")
            print(" |")
            print(" |")
            print("_|_")
            print(f"Found Letters: {', '.join(foundLetters)}")
            print(f"Used Letters: {', '.join(usedLetters)}")
            print("------------------------------------------------------------")

        elif wrongattempts == 9:
            print("This letter does not exist.")
            print(" ______")
            print(" |/   |")
            print(" |    |")
            print(" |   (_)")
            print(" |   \|/")
            print(" |    |")
            print(" |    |")
            print(" |")
            print(" |")
            print("_|_")
            print(f"Found Letters: {', '.join(foundLetters)}")
            print(f"Used Letters: {', '.join(usedLetters)}")
            print("------------------------------------------------------------")

        elif wrongattempts == 10:
            print("This letter does not exist.")
            print(" ______")
            print(" |/   |")
            print(" |    |")
            print(" |   (_)")
            print(" |   \|/")
            print(" |    |")
            print(" |    |")
            print(" |   / ")
            print(" |")
            print("_|_")
            print(f"Found Letters: {', '.join(foundLetters)}")
            print(f"Used Letters: {', '.join(usedLetters)}")
            print("------------------------------------------------------------")

        # When wrong attempts > 10, reveal the word and exit the program
        elif wrongattempts == 11:
            print("-GAME OVER-")
            print(" ______")
            print(" |/   |")
            print(" |    |")
            print(" |   (_)")
            print(" |   \|/")
            print(" |    |")
            print(" |    |")
            print(" |   / \‎")
            print(" |")
            print("_|_")
            print(f"The word was '{randomWord[1]}'.")
            print("------------------------------------------------------------")
            break
