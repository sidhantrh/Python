import random  # Importing the random module for generating random numbers

# Function to generate a random number between 1 and 'a'
def randomnumber(a):
    random_number = random.randint(1, a)
    return random_number

# Function for the computer to generate a random number between 1 and 'a'
def computerinput(a,b):
    random_number = random.randint(a, b)
    return random_number

# Displaying a welcome message
print("Welcome to the random number guessing game!")
print("A random number between 1 and 20 has been selected")

# Infinite loop to keep the game running until the user decides to quit
while True:
    computer_input1 = 1  # Initial range for the computer's guess
    computer_input2 = 20 
    r_number = randomnumber(20)  # Generating a random number for the game
    user = input("Choose a random number between 1 and 20:")  # User input
    
    # Checking if the user's guess is correct
    if int(user) == int(r_number):
        print("You guessed correctly! You win!")
        yes_no = input("Would you like to play again(Yes/No)?")  # Asking the user if they want to play again
        if yes_no == "no" or "No" or "N" or "n":
            break  # Exit the loop if the user chooses "no"
        elif yes_no == "yes" or "Yes" or "Y" or "y":
            continue  # Continue the loop if the user chooses "yes"
        else:
            print("Invalid input, try again")  # Handling invalid input

    elif int(user) > int(r_number):
        print("Too High")
        computer_input2 < int(user)  # Sets top range to be less than user input
        
    elif int(user) < int(r_number):
        print("Too Low")
        computer_input1 > int(user)  # Sets bottom range to be greater than user input
        
    elif int(user) > 20 or int(user) < 1:
        print("Invalid input, pick number between 1 and 20")
        continue
    
    else:
        print("Invalid input, pick number between 1 and 20")
        continue
        
    
    # Generating a guess for the computer
    c_input = int(computerinput(computer_input1, computer_input2))
    print("Computer Guesses:", c_input)

    # Checking if the computer's guess is correct
    if c_input == int(r_number):
        print("Computer guessed correctly! You lose!")
        yes_no = input("Would you like to play again?")  # Asks if the user wants to play again
        if yes_no == "no":
            break  # Exit the loop if the user chooses "no"
        elif yes_no == "yes":
            continue  # Continue the loop if the user chooses "yes"
        else:
            print("Invalid input, try again")  # Handling invalid input
    elif c_input > int(r_number):
        print("Computer Picked Too High")
    
    elif c_input < int(r_number):
        print("Computer Picked Too Low")

