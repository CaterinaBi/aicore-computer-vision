import random
'''
    A game of Rock, Paper, Scissors in which the user plays against the computer.
    The user inputs their chosen gesture in writing.
    The computer chooses its move randomly from a pre-determined list.

    Parameters:
    ----------
    gesture_list: list
        List of gestures to be used in the game

    Attributes:
    ----------
    computer_choice: str
        The gesture to be played by the computer, picked randomly from gesture_list
    user_choice: str
        The gesture played by the user (input)
    winner: str
        The winner of the match/game

    Methods:
    -------
    get_computer_choice(computer_choice)
        Gets the computer's input.
    get_user_choice(user_choice)
        Gets the user's input.
    get_winner(computer_choice, user_choice, winner)
        Returns the name of the winner.
    '''
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

def play_game(gesture_list):
  game = Game(gesture_list)
  game.get_computer_choice(game.computer_choice)
  game.get_user_choice(game.user_choice)
  game.get_winner(game.computer_choice, game.user_choice, game.winner)

if __name__ == '__main__':
  gesture_list = ["Rock", "Paper", "Scissors"]
  play_game(gesture_list)
# %%
