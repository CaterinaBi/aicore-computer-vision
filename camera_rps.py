import cv2
from keras.models import load_model
import numpy as np
import random
import time
'''
    NEEDS UPDATING
    A game of Rock, Paper, Scissors in which the user plays against the computer.
    The user inputs their chosen gesture using the camera.
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
    classify_output():
    Uses the list of probabilities output from get_prediction
    to determine the image inputted in the camera.
    '''
class Game:
  def __init__(self):
    # model, video and data attributes
    self.model = load_model('keras_model.h5')
    self.cap = cv2.VideoCapture(0)
    self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # users attributes
    self.user = "user"
    self.computer = "computer"
    self.round_number = 1
    self.computer_lives = 3
    self.user_lives = 3
    # layout print
    self.spacer = "\n --------------------------------------------------------"

  def get_computer_choice(self):
    computer_choice = random.choice(gesture_list)
    return computer_choice

  def get_prediction(self):
    ret, frame = self.cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    self.data[0] = normalized_image
    prediction = self.model.predict(self.data)
    cv2.imshow('frame', frame)
    return prediction

  def counter_1(self):
    countdown = 3
    print("\nPrepare to show me your chosen gesture in...")
    while countdown > 0:
      print(f'{countdown}')
      cv2.waitKey(1000)
      countdown -= 1
    print('\nShow your hand NOW!')
    self.counter_2()

  def counter_2(self):
    counter = 2
    while counter > 0:
      cv2.waitKey(1000)
      print("...")
      counter -= 1
  
  def classify_output(self):
    prediction = self.get_prediction()
    choice_probability = {'Rock': prediction[0,1], 'Paper': prediction[0,2], 'Scissors': prediction[0,3]}
    self.user_prediction = max(choice_probability, key=choice_probability.get)
    print(f"\nThe machine predicted that the user gesture was {self.user_prediction}.")
    return self.user_prediction

  def get_winner(self):
    winner = str
    computer_choice = self.get_computer_choice()
    user_choice = self.classify_output()
    if computer_choice == user_choice:
      print(f"\nThe computer too chose {computer_choice}. No one wins this round!")
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

  def count_lives(self):
    winner = self.get_winner()
    self.counter_2()
    if winner == "user":
      self.computer_lives -= 1
      if self.computer_lives == 2 or self.computer_lives == 0:
        print(f"The computer now has {self.computer_lives} lives left.")
      elif self.computer_lives == 1:
        print(f"The computer now has only {self.computer_lives} life left.")
    elif winner == "computer":
      self.user_lives -=1
      if self.user_lives == 2 or self.user_lives == 0:
        print(f"The user now has {self.user_lives} lives left.")
      elif self.user_lives == 1:
        print(f"The user now has only {self.user_lives} life left.")
    # game over message
    if self.computer_lives == 0 or self.user_lives == 0:
      print(self.spacer, f"\n ******** GAME OVER! The {winner} wins the game! ********", self.spacer, "\n")

def play_game():
  game = Game()
  while game.computer_lives >= 1 and game.user_lives >= 1:
    print(game.spacer, f"\n ******************** ROUND NUMBER {game.round_number} ********************", game.spacer)
    print("\nPress 'c' to continue, or 'q' to quit.")
    game.get_computer_choice()
    game.counter_1()
    game.count_lives()
    game.round_number += 1
    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  # After the loop release the cap object
  game.cap.release()
  # Destroy all the windows
  cv2.destroyAllWindows()

if __name__ == '__main__':
  gesture_list = ["Rock", "Paper", "Scissors"]
  play_game()
# %%
