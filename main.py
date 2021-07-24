#import library to get random number
import random

from art import logo # Include an ASCII art logo.
print(logo)

auto_gen_number=random.randint(1,100)
#let user choose the difficulty level - easy level has 10 tries hard one has 5
difficulty_level=input("Choose a difficulty level: easy or hard ")
if difficulty_level=="easy" or difficulty_level=="Easy" or difficulty_level=="e":
  chances=10
  print(f"You have {chances} chances to guess")
else:
  chances=5
  print(f"You have {chances} chances to guess")

game_over=False

while chances>=1 and game_over==False:
  user_number=int(input("Please guess a number from 1 to a 100: "))

  if user_number==auto_gen_number:
    print(f"You won! It's {user_number}")
    game_over=True
  elif user_number>auto_gen_number:
    print("Too high")
    chances -= 1
  elif user_number<auto_gen_number:
    print("Too low")
    chances-=1

if chances == 0:
  print("You have run out of guesses! You lost! Try again")


