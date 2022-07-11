import cv2
from keras.models import load_model
import numpy as np
import random
'''
    NEEDS UPLOADING
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

  def __init__(self):
    self.model = load_model('keras_model.h5')
    self.cap = cv2.VideoCapture(0)
    # self.user_choice = input("Please choose your move: ")
    # self.winner = str

  def get_computer_choice(self):
    '''
    Returns a string randomly selected from gesture_list
    '''
    self.computer_choice = random.choice(gesture_list)
    return self.computer_choice


# method that just captures the video
# method that gets the prediction

  def get_video(self):
    '''
    Activates the camera
    '''
    self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    self.ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        self.normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        self.data[0] = self.normalized_image

        # font to be used in text message
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        # uses putText() to insert text in video
        cv2.putText(frame,
                    'WELCOME TO ROCK, PAPER, SCISSORS!',
                    (300, 600),
                    self.font, 1,
                    (255, 255, 255),
                    2,
                    cv2.LINE_4)
        cv2.putText(frame,
                    'Press c to continue, or q to exit.',
                    (300, 640),
                    self.font, 1,
                    (255, 255, 255),
                    2,
                    cv2.LINE_4)
        # displays the resulting frame
        cv2.imshow('frame', frame)
        # releases the cap object after the loop
        self.cap.release()
        # destroys all windows
        cv2.destroyAllWindows()

  def close_window(self):
    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):

  def open_window(self):
    if cv2.waitKey(1) & 0xFF == ord('s'):
      self.video_started = True

  def get_prediction(self):
    '''
    Returns the predictions of the model in the form
    of a list called prediction.
    '''
    prediction = self.model.predict(self.data)
    print(prediction)
    return prediction

  def get_gesture(self, prediction):
    '''
    Gets the index of the biggest number in the prediction list.
    Extracts the element with the corresponding index from gesture_list
    '''
    # use np.arg_max
    # prediction = self.get_prediction()
    self.gesture_index = np.argmax(prediction)
    self.user_gesture = gesture_list[self.gesture_index]
    print(self.user_gesture)
    return self.user_gesture

  def get_winner(self, computer_choice, winner):
    '''
    Outputs the winner of each round, and then the game
    '''
    user = str
    computer = str
    user_choice = self.get_gesture()
    if computer_choice == user_choice:
      print(f"The computer too chose {computer_choice}. No one wins this round!")
    elif computer_choice == "Rock":
      if user_choice == "Paper":
        winner = user
        print(f"The computer chose {computer_choice}. The user wins this round!")
      elif user_choice == "Scissors":
        winner = computer
        print(f"The computer chose {computer_choice}. The computer wins this round!")
    elif computer_choice == "Paper":
      if user_choice == "Rock":
        winner = computer
        print(f"The computer chose {computer_choice}. The computer wins this round!")
      elif user_choice == "Scissors":
        winner = user
        print(f"The computer chose {computer_choice}. The user wins this round!")
    else:
      if user_choice == "Paper":
        winner = computer
        print(f"The computer chose {computer_choice}. The computer wins this round!")
      elif user_choice == "Rock":
        winner = user
        print(f"The computer chose {computer_choice}. The user wins this round!")
    return winner

def play_game():
  game = Game()
  #game.get_computer_choice()
  # game.get_user_choice(game.user_choice)
  game.get_video()
  #game.get_prediction()
  #game.get_gesture(game.prediction)
  #game.get_winner(game.computer_choice, game.winner)

if __name__ == '__main__':
  gesture_list = ["None", "Rock", "Paper", "Scissors"]
  play_game()
# %%
