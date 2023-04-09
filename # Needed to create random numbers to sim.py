# Needed to create random numbers to simulate a dice roll
import random

#Each player must have a name
player1_name = input("Player one, please enter your name: ") 
player2_name = input("Player two, please enter your name: ") 

#Create a password for player1_name
player1_password = input(player1_name +", please enter your password: ") 
player1_password1 = input("Please re-enter your password: ") 
while player1_password1 != player1_password: 
   player1_password1 = input("Password did not match, please re-enter your password: ") 
print(player1_name +", Welcome \n") 

#Create a password for player2_name 
player2_password = input(player2_name +", please enter your password: ") 
player2_password2 = input("Re-enter your password: ") 
while player2_password2 != player2_password: 
   player2_password2 = input("Password did not match, please re-enter your password: ") 
print(player2_name +", Welcome \n") 

#Rules of the dice game 
print("Welcome, to the dice game here is the some rules you should know. \n") 
print("""1. The points rolled on each player’s dice are added to their score.
2. If the total is an even number, an additional 10 points are added to their score.
3. If the total is an odd number, 5 points are subtracted from their score.
4. If they roll a double, they get to roll one extra die and get the number of points rolled added to their score.
5. A player's score cannot go below 0 at any point.
6. The person with the highest score at the end of the 5 rounds wins.
7. If both players have the same score at the end of the 5 rounds, they each roll 1 die and whoever gets the highest score wins (this repeats until someone wins). \n""")


# Initialise player scores to 0
player1_score = 0
player2_score = 0

# Repeat everything in this block 10 times
for i in range(5):

    # Generate random numbers between 1 and 6 for each player.
    player1_value = random.randint(1, 6)
    player2_value = random.randint(1, 6)

    # Display the values
    print(player1_name + " rolled: ", player1_value)
    print(player2_name + " rolled: ", player2_value)

    # Selection: based on a comparison of the values, take the appropriate path through the code.
    if player1_value > player2_value:
        print(player1_name + " wins.")
        player1_score = player1_score   # This is how we increment a variable
    elif player2_value > player1_value:
        print(player2_name + " wins")
        player2_score = player2_score + 1
    else:
        print("It's a draw")

    input("Press enter to continue. \n")  # Wait for user input to proceed
print(player1_name + " scores:", player1_score)
print(player2_name + " scores:", player2_score)  
