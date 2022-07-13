import cv2
from keras.models import load_model
import numpy as np
import random
import time
'''
    NEEDS UPDATING
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

    # model, video and data attributes
    self.model = load_model('keras_model.h5')
    self.cap = cv2.VideoCapture(0)
    self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # font to be used in text messages
    self.font = cv2.FONT_HERSHEY_SIMPLEX
    # messages to be displayed
    self.intro_message = "WELCOME TO THE GAME OF ROCK, PAPER, SCISSORS!"
    self.instruction_message = "Press 'c' to continue, or 'q' to quit."

    self.user_choice = self.get_prediction()
    self.user = "user"
    self.computer = "computer"
    self.winner = str
    self.seconds = 0

    # layout miscellaneous prints
    self.spacer = "\n --------------------------------------------------------"

  def get_computer_choice(self, computer_choice):
    # print(f"The computer choice is {computer_choice}")
    return computer_choice

  # replaces get_user_choice()
  def get_prediction(self):
    ret, frame = self.cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    self.data[0] = normalized_image
    prediction = self.model.predict(self.data)
    cv2.putText(frame, self.intro_message, (300, 600), self.font, 1, 
                                (255, 255, 255), 2, cv2.LINE_4)
    cv2.putText(frame, self.instruction_message, (300, 640), self.font, 1,
                                (255, 255, 255), 2, cv2.LINE_4)
    cv2.imshow('frame', frame)
    return prediction

  def counter_1(self):
    countdown = 3
    print("\nPrepare to show me your chosen gesture in...")
    while countdown > 0:
      print(f'{countdown}')
      time.sleep(1)
      countdown -= 1
    print('\nShow your hand NOW!')

  def counter_2(self):
    counter = 2
    while counter > 0:
      time.sleep(1)
      print("...")
      counter -= 1
    # print("Gesture detected.\n")
  
  # gets gesture out of prediction
  def classify_output(self):
    """
    Uses the list of probabilities output from get_prediction
    to determine the image inputted in the camera.
    """
    prediction = self.get_prediction()
    choice_probability = {'Rock': prediction[0,1], 'Paper': prediction[0,2], 'Scissors': prediction[0,3]}
    self.user_prediction = max(choice_probability, key=choice_probability.get)
    return self.user_prediction

  # determines winner
  def get_winner(self, computer_choice, user_choice, winner):
    computer_choice = self.get_computer_choice(computer_choice)
    user_choice = self.classify_output()
    if computer_choice == user_choice:
      print(f"\nThe computer too chose {computer_choice}. No one wins this round!\n")
    elif computer_choice == "Rock":
      if user_choice == "Paper":
        winner = self.user
        print(f"\nThe computer chose {computer_choice}. The user wins this round!")
      elif user_choice == "Scissors":
        winner = self.computer
        print(f"\nThe computer chose {computer_choice}. The computer wins this round!")
    elif computer_choice == "Paper":
      if user_choice == "Rock":
        winner = self.computer
        print(f"\nThe computer chose {computer_choice}. The computer wins this round!")
      elif user_choice == "Scissors":
        winner = self.user
        print(f"\nThe computer chose {computer_choice}. The user wins this round!")
    else:
      if user_choice == "Paper":
        winner = self.computer
        print(f"\nThe computer chose {computer_choice}. The computer wins this round!")
      elif user_choice == "Rock":
        winner = self.user
        print(f"\nThe computer chose {computer_choice}. The user wins this round!")
    return winner

def play_game(gesture_list):
  round_number = 1
  computer_lives = 3
  user_lives = 3
  game = Game(gesture_list)
  while computer_lives >= 1 and user_lives >= 1:
    print(game.spacer, f"\n ****************** ROUND NUMBER {round_number} ******************", game.spacer)
    game.get_computer_choice(game.computer_choice)
    # print("\nPrepare to show me your chosen gesture in 3 seconds!")
    # time.sleep(3)
    # print("Show me your hand NOW!")
    game.counter_1()
    game.get_prediction()
    game.counter_2()
    game.classify_output()
    print(f"\nThe machine predicted that the user gesture was {game.user_prediction}.")
    game.counter_2()
    winner = game.get_winner(game.computer_choice, game.user_choice, game.winner)
    if winner == "user":
      computer_lives -= 1
      if computer_lives == 2 or computer_lives == 0:
        print(f"The computer now has {computer_lives} lives left.\n")
      elif computer_lives == 1:
        print(f"The computer now has only {computer_lives} life left.\n")
    elif winner == "computer":
      user_lives -=1
      if user_lives == 2 or user_lives == 0:
        print(f"The user now has {user_lives} lives left.\n")
      elif user_lives == 1:
        print(f"The user now has only {user_lives} life left.\n")
    round_number += 1
    if computer_lives == 0 or user_lives == 0:
      print(game.spacer, f"\n ********** GAME OVER! The {winner} wins the game! **********", game.spacer, "\n")
  # After the loop release the cap object
  game.cap.release()
  # Destroy all the windows
  game.cv2.destroyAllWindows()

if __name__ == '__main__':
  gesture_list = ["Rock", "Paper", "Scissors"]
  play_game(gesture_list)
# %%
