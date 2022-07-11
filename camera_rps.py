import cv2
from keras.models import load_model
import numpy as np
import random
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
        # self.user_choice = input("Please choose your move: ")
        self.winner = str

        # model, video and data attributes
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

  def get_computer_choice(self, computer_choice):
    return computer_choice

  # replaces get_user_choice()
  def get_prediction(self):
    ret, frame = self.cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    self.data[0] = normalized_image
    prediction = self.model.predict(self.data)
    cv2.imshow('frame', frame)
    return prediction

  def get_winner(self, computer_choice, user_choice, winner):
    user = str
    computer = str
    user_choice = self.get_prediction()
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
  while True:
    game = Game(gesture_list)
    game.get_computer_choice(game.computer_choice)
    game.get_prediction()
    # game.get_user_choice(game.user_choice)
    game.get_winner(game.computer_choice, game.get_prediction, game.winner)
    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  # After the loop release the cap object
  game.cap.release()
  # Destroy all the windows
  game.cv2.destroyAllWindows()

if __name__ == '__main__':
  gesture_list = ["Rock", "Paper", "Scissors"]
  play_game(gesture_list)
# %%
