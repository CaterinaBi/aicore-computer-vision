import cv2
from keras.models import load_model
import numpy as np
import random

class Game:
  '''
    A game of Rock, Paper, Scissors in which the user plays against the computer.
    The user inputs their chosen gesture using the camera.
    The computer chooses its move randomly from a pre-determined list.

    Attributes:
    ----------
    model: load_model('keras_model.h5')
        Loads computer vision model used in the application.
    cap: cv2.VideoCapture(0)
        Video capture constructor for opencv.
    data: array of tuples
        The model's probabilities for each element of gesture_list.
    user: str
        Attributes the name "user" to the user.
    computer: str 
        Attributes the name "computer" to the computer.
    round_number: int
        Used to calculate the round number. Starts at 1 by default.
    computer_lives: int
        Number of lives left for the computer. Fixed at 3 by default.
    user_lives: int
        Number of lives left for the user. Fixed at 3 by default.
    spacer: str
        String that prints out a separator to make the application's output clearer.

    Methods:
    -------
    get_computer_choice()
        Gets the computer's input randomly from gesture_list.
    get_prediction()
        Understands the user's input using probability.
    classify_output()
        Uses the list of probabilities from get_prediction() to determine the image inputted in the camera.
    get_winner()
        Returns the name of the winner.
    count_lives()
        Keep track of the number of remaining lives for each user.
    counter_1(), counter_2()
        Slow down the machine to make the application accessible for the user.
    '''
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

  def get_camera(self):
    ret, frame = self.cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    cv2.imshow('frame', frame)
    return normalized_image
    
  def get_prediction(self):
    # ret, frame = self.cap.read()
    # resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    # image_np = np.array(resized_frame)
    # normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    self.data[0] = self.get_camera()
    prediction = self.model.predict(self.data)
    # cv2.imshow('frame', frame)
    return prediction
  
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

  def countdown_counter(self):
    countdown = 3
    print("\nPrepare to show me your chosen gesture in...")
    while countdown > 0:
      print(f'{countdown}')
      cv2.waitKey(1000)
      countdown -= 1
    print('\nShow your hand NOW!')
    # self.counter_2()

  def counter_2(self):
    counter = 2
    while counter > 0:
      cv2.waitKey(1000)
      print("...")
      counter -= 1

def play_game():
  game = Game()
  while game.computer_lives >= 1 and game.user_lives >= 1:
    print(game.spacer, f"\n ******************** ROUND NUMBER {game.round_number} ********************", game.spacer)
    print("\nPress 'c' to continue, or 'q' to quit.")
    game.get_camera()
    game.countdown_counter()
    game.get_prediction()
    game.count_lives()
    # game.get_prediction()
    # game.get_computer_choice()
    # game.count_lives()
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
