'''
Python challenge
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

    # This while block will make sure player input are integers only
    while True:
        try:
            player_guess = int(input("What is your guess? "))
            break
        except ValueError:
            print("Please input integers only.\n")
            continue

    # This while loop checks if the player_guess is not equal to the secret_number then runs the main game loop
    while player_guess != secret_number:
        if player_guess < secret_number:
            try:
                print("Sorry " + name + ", that's too low of a guess.\n")
                player_guess = int(input("Try again. What's your next guess? "))
                continue
            except ValueError:
                print("Please input integers only.\n")
                player_guess = int(input("Try again. What's your next guess? "))
                continue
        if player_guess > secret_number:
            try:
                print("Sorry " + name + ", that's too high of a guess.\n")
                player_guess = int(input("Try again. What's your next guess? "))
                continue
            except ValueError:
                print("Please input integers only.\n")
                player_guess = int(input("Try again. What's your next guess? "))
                continue
        else:
            try:
                player_guess = int(input("Try again. What's your next guess? "))
                continue
            except ValueError:
                print("Please input integers only.\n")
                continue

    # This if statement is the win condition for the game. If player_guess is equal to secret_number, print statement and exit.
    if player_guess == secret_number:
        print("That's the correct number. Good job " + name + "!")

# Ask player for difficulty level
def difficulty_selector():
    '''
    This function sets the difficulty for the player.
    '''
    min_num = None
    max_num = None
    print("Which difficulty would you like to play at?")
    selected_diff = input(" [1] Easy:   0 - 100\n [2] Medium: 0 - 500\n [3] Hard:   0 - 1000\n [4] Insane: 0 - 10,000\n [5] Custom: Pick your range\n")
    selected_diff_int = int(selected_diff)
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
        min_num = input("What is your minimum number? ")
        min_num_int = int(min_num)
        max_num = input("What is your maximum number? [Number must be higher than " + min_num +"]: ")
        max_num_int = int(max_num)
        while max_num_int <= min_num_int:
            print("Please choose a higher value.")
            max_num = input("What is your maximum number? [Number must be higher than " + min_num +"]: ")
            max_num_int = int(max_num)
        return min_num_int, max_num_int
    else:
        min_num = 0
        max_num = 100
        return min_num, max_num

# Ask player for name and assign it to the name variable. Using title method to capitalize letters.
name = input("What is your name? ").title()
print("Hello " + name + ", welcome to the guessing game.")

numbers = difficulty_selector()
print(numbers)
# Assign a secret number to secret_number variable using the random.randint method.
secret_number = random.randint(numbers[0],numbers[1])
print(secret_number)
## MAIN LOGIC

# Run numbers_game function
numbers_game()

# Asks player if they want to play again after inital game.
check = input("Do you want to play again? [y/n] ")
if check[0].upper() == "Y":
    print("welcome back " + name + "!")
    secret_number = random.randint(0, 100)
    numbers_game()
else:
    print("Thanks for playing!")

## End of code ##
