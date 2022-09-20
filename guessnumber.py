import random

# Generate random numbers
random = random.randint(0, 999)

# Introduction/rules
print("-Guess the number between 0 and 999.")
print("-You have 10 attempts.")

attempts = 0

# Keep prompting the user with a while loop, until a break
while True:

    # Get user-provided numbers
    number = int(input("Guess: "))
    attempts += 1

    if number == random:
        print("Correct!")
        break

    else:
        if len(str(random)) != len(str(number)):
            print("Wrong number of digits!")

        else:
            # Get number's digits
            n_digit1 = int(number / 100)
            n_digit2 = int((number % 100) / 10)
            n_digit3 = int(number % 10)

            # Get random's digits
            r_digit1 = int(random / 100)
            r_digit2 = int((random % 100) / 10)
            r_digit3 = int(random % 10)

            # Get boolean values
            equal1 = (n_digit1 == r_digit1)
            equal2 = (n_digit2 == r_digit2)
            equal3 = (n_digit3 == r_digit3)

            if len(str(random)) == 3:
                if equal1 or equal2 or equal3:
                    print(f"{equal1} {equal2} {equal3}")
                else:
                    print(f"{equal1} {equal2} {equal3}")

            elif len(str(random)) == 2:
                if equal2 or equal3:
                    print(f"{equal2} {equal3}")
                else:
                    print(f"{equal2} {equal3}")

            elif len(str(random)) == 1:
                if equal3:
                    print("Correct!")
                    break
                else:
                    print(f"{equal3}")


    # After 10 wrong attempts, reveal the answer and exit the program
    if attempts > 10:
        print(f"The answer was {random}, sorry!")
        break
