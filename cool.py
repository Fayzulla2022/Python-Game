import random

# Define a function to authenticate the player by asking for their password and confirming it
def authenticate_player(player_name):
    # Prompt the player to enter their password
    password = input(player_name + ", 🔐 please enter your password: ")

    # Prompt the player to re-enter their password for confirmation
    re_entered_password = input("🔁 Please re-enter your password: ")

    # Continue asking for the re-entered password until it matches the original password
    while re_entered_password != password:
        re_entered_password = input("❌ Password did not match, please re-enter your password: ")

    # Greet the player once they have successfully authenticated
    print(player_name + ", 🎉 Welcome! Let's Emjoy \n")

def roll_dice():
    return [random.randint(1, 6), random.randint(1, 6)]

def calculate_round_score(dice):
    round_score = sum(dice)

    if round_score % 2 == 0:
        round_score += 10
    else:
        round_score -= 5

    if dice[0] == dice[1]:
        round_score += random.randint(1, 6)

    return max(0, round_score)

def play_round(player_name):
    input(f"{player_name}, press enter to roll the dice.")
    dice = roll_dice()
    round_score = calculate_round_score(dice)
    print(f"{player_name} rolled {dice} and scored {round_score} points.")
    return round_score

# Authenticate both players
player1_name = input("Player one, Create a User Name: ")
authenticate_player(player1_name)

player2_name = input("Player two, Create a User Name: ")
authenticate_player(player2_name)

# Rules of the dice game
print("Welcome to the dice game! Here are the rules:\n")
print("1. Points rolled on each player’s dice ➕ to their score.")
print("2. Even total? ➕ 10 points to score.")
print("3. Odd total? ➖ 5 points from score.")
print("4. Roll a double? 🎲 Roll an extra die, add points to score.")
print("5. Score can't go below 0️⃣.")
print("6. Highest score after 5️⃣ rounds wins.")
print("7. Tie? Both players roll 1 die, highest wins (repeats until winner). \n")

# Initialize player scores to 0
player1_score = 0
player2_score = 0

# Play 5 rounds
for round in range(5):
    print(f"Round {round + 1}")

    player1_score += play_round(player1_name)
    player2_score += play_round(player2_name)

    print(f"{player1_name}'s total score: {player1_score}")
    print(f"{player2_name}'s total score: {player2_score}")
    print()

# Determine the winner
while player1_score == player2_score:
    print("It's a tie! Both players will roll 1 die to break the tie.")
    player1_tiebreaker = random.randint(1, 6)
    player2_tiebreaker = random.randint(1, 6)

    print(f"{player1_name} rolled a {player1_tiebreaker}")
    print(f"{player2_name} rolled a {player2_tiebreaker}")

    if player1_tiebreaker > player2_tiebreaker:
        player1_score += 1
    elif player2_tiebreaker > player1_tiebreaker:
        player2_score += 1

if player1_score > player2_score:
    print(f"{player1_name} wins with a score of {player1_score}!")

