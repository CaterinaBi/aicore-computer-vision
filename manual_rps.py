import random

class Game:
  def __init__(self, gesture_list):
        self.computer_choice = random.choice(gesture_list)
        self.user_choice = input("Please choose your move: ")
        self.winner = str

  def get_computer_choice(self, computer_choice):
    return computer_choice

  def get_user_choice(self, user_choice):
    return user_choice

  def get_winner(self, computer_choice, user_choice, winner):
    user = str
    computer = str
    if computer_choice == user_choice:
      print(f"The computer too chose {computer_choice}. No one wins this match!")
    elif computer_choice == "Rock":
      if user_choice == "Paper":
        winner = user
        print(f"The computer chose {computer_choice}. The user wins this match!")
      elif user_choice == "Scissors":
        winner = computer
        print(f"The computer chose {computer_choice}. The computer wins this match!")
    elif computer_choice == "Paper":
      if user_choice == "Rock":
        winner = computer
        print(f"The computer chose {computer_choice}. The computer wins this match!")
      elif user_choice == "Scissors":
        winner = user
        print(f"The computer chose {computer_choice}. The user wins this match!")
    else:
      if user_choice == "Paper":
        winner = computer
        print(f"The computer chose {computer_choice}. The computer wins this match!")
      elif user_choice == "Rock":
        winner = user
        print(f"The computer chose {computer_choice}. The user wins this match!")
   return winner
