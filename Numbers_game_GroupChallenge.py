'''
Python challenge - Create a number guessing game
'''
# Import random module
import random

# Creating a function of numbers_game that will run main game code
def numbers_game():
    '''
    This is the main function used to run the game code.
    It will take an integer value from the player and check if it is correct.
    '''
    # Create player_guess variable with integer type. Used to avoid issues due to not type not being declared.
    player_guess = int()
    count = 0

    # This while block will make sure player input are integers only
    while True:
        try:
            player_guess = int(input("What is your guess? "))
            count += 1
            break
        except ValueError:
            print("Please input integers only.\n")
            continue

    # This while loop checks if the player_guess is not equal to the secret_number then runs the main game loop
    while player_guess != secret_number:
        if (player_guess < secret_number) and (player_guess >= numbers[0]) and (player_guess <= numbers[1]):
            print("Sorry " + name + ", that's too low of a guess.\n")
        if (player_guess > secret_number) and (player_guess >= numbers[0]) and (player_guess <= numbers[1]):
            print("Sorry " + name + ", that's too high of a guess.\n")
        else:
            try:
                print("\nPlease enter a value between " + str(numbers[0]) + " - " + str(numbers[1]))
                player_guess = int(input("Try again. What's your next guess? "))
                count += 1
                continue
            except ValueError:
                print("Please input integers only.\n")
                continue
        try:
            player_guess = int(input("Try again. What's your next guess? "))
            count += 1
            continue
        except ValueError:
            print("Please input integers only.\n")
            continue

    # This if statement is the win condition for the game. If player_guess is equal to secret_number, print statement and exit.
    if player_guess == secret_number:
        if count == 1:
            print("Amazing! You got it in the first try.\n")
        else:
            print("That's the correct number. Good job " + name + "!")
            print("It took you " + str(count) + " tries to get it right.")

# Ask player for difficulty level
def difficulty_selector():
    '''
    This function sets the difficulty for the player.
    '''
    min_num = None
    max_num = None
    print("Which difficulty would you like to play at?")
    # This while loop is here for error handling.
    while True:
        try:
            selected_diff = input(" [1] Easy:   0 - 100\n [2] Medium: 0 - 500\n [3] Hard:   0 - 1000\n [4] Insane: 0 - 10,000\n [5] Custom: Pick your range\n Make a selection [1 - 5]: ")
            selected_diff_int = int(selected_diff)
            break
        except ValueError:
            print("\n### Enter a value 1 - 5. ###\n")
            continue

    if selected_diff_int == 1:
        min_num = 0
        max_num = 100
        return min_num, max_num
    if selected_diff_int == 2:
        min_num = 0
        max_num = 500
        return min_num, max_num
    if selected_diff_int == 3:
        min_num = 0
        max_num = 1000
        return min_num, max_num
    if selected_diff_int == 4:
        min_num = 0
        max_num = 10000
        return min_num, max_num
    if selected_diff_int == 5:
        # This while loop is for ValueError handling. Prevents user from entering non-integer values.
        while True:
            try:
                min_num = input("What is your minimum number? ")
                min_num_int = int(min_num)
                max_num = input("What is your maximum number? [Number must be higher than " + min_num +"]: ")
                max_num_int = int(max_num)
                while max_num_int <= min_num_int:
                    print("Please choose a higher value.")
                    max_num = input("What is your maximum number? [Number must be higher than " + min_num +"]: ")
                    max_num_int = int(max_num)
                return min_num_int, max_num_int
            except ValueError:
                print("Enter a valid integer value.\n")
                continue
    else:
        min_num = 0
        max_num = 100
        return min_num, max_num



# Ask player for name and assign it to the name variable. Using title method to capitalize letters.
name = input("What is your name? ").title()
print("Hello " + name + ", welcome to the Guessing Game.\n")

# Running difficulty selector function and assigning returned values to numbers variable
numbers = difficulty_selector()

# DEBUG for testing numbers variable assignment
# print(numbers)

# Assign a secret number to secret_number variable using the random.randint method.
secret_number = random.randint(numbers[0],numbers[1])

# DEBUG prints secret_number
# print(secret_number)

## MAIN ##

# Run numbers_game function
numbers_game()

# Asks player if they want to play again after inital game.
while True:
    check = input("Do you want to play again? [y/N] ")
    try:
        if check[0].upper() == "Y":
            print("Welcome back " + name + "!\n")
            numbers = difficulty_selector()
            secret_number = random.randint(numbers[0],numbers[1])
            numbers_game()
        else:
            print("Thanks for playing!")
            break
    # For exiting program when no input is provided
    except IndexError:
        print("Thanks for playing!")
        break


## End of code ##
