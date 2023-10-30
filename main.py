from art import logo, vs
from game_data import data 
import random
import os

# Initialize game variables
game_on = True
score = 0

def clear_console():
    # Clear the console screen
    os.system('clear')
  
def display_comparison(person1, person2):
  # Display comparison information
  print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}")
  print(vs)
  print(f"Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}")

def ask_for_user_choice():
  # Get user's choice and validate it
  while True:
      choice = input("Who has more followers? Type 'A' or 'B': ").upper()
      if choice in ['A', 'B']:
          return choice
      else:
          print("Invalid input. Please enter 'A' or 'B.")

def check(high, low):
  # Check if the high follower count is greater
  return high > low

def win():
  # Handle a win
  global score
  score += 1
  clear_console()
  print(logo)
  print(f"You are Right! Current Score: {score}")

def lose():
  # Handle a loss
  global game_on
  print("You are wrong")
  game_on = False

while game_on is True:
  if score == 0:
    clear_console()
    print(logo)
  # select two random entries
  person1, person2 = random.sample(data, 2)
  display_comparison(person1,person2)
  user_choice = ask_for_user_choice()
  if (user_choice == 'A' and check(person1['follower_count'], person2['follower_count'])) or \
     (user_choice == 'B' and check(person2['follower_count'], person1['follower_count'])):
      win()
  else:
      lose()


# Display the final score when the game ends
print(f"Game Over! Your Final Score: {score}")