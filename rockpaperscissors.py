import cv2
from keras.models import load_model
import numpy as np
import random

'''
Docstring here
'''

class RockPaperScissors:

  def __init__(self):
    self.model = load_model('keras_model.h5')
    self.cap = cv2.VideoCapture(0)
    self.gesture_list = ["none", "rock", "paper", "scissors"]

    # messages to desplay on the screen
    self.intro_message = "" # bottom centered
    self.instruction_message = "" # right below intro_message

  def get_computer_choice(self):
    # returns a string randomly selected from gesture_list
    self.computer_choice = random.choice(self.gesture_list)
    return self.computer_choice

  def get_video(self):
    # activates the camera
    self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    self.ret, frame = self.cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    self.normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    self.data[0] = self.normalized_image

    # font to be used in text messages
    self.font = cv2.FONT_HERSHEY_SIMPLEX
    # uses putText() to insert text in the video
    cv2.putText(frame, self.intro_message, (300, 600), self.font, 1, 
                                (255, 255, 255), 2, cv2.LINE_4)
    cv2.putText(frame, self.instruction_message, (300, 640), self.font, 1,
                                (255, 255, 255), 2, cv2.LINE_4)
    # displays the resulting frame
    cv2.imshow('frame', frame)

  def close_window(self):
    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
      # releases the cap object after the loop
      self.cap.release()
      # destroys all windows
      cv2.destroyAllWindows()

  def intro_messages(self):
    self.intro_message = "WELCOME TO ROCK, PAPER, SCISSORS!"
    self.instruction_message = "Press c to continue."
    self.open_window()

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
    self.user_gesture = self.gesture_list[self.gesture_index]
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
  game = RockPaperScissors()
  #game.get_computer_choice()
  # game.get_user_choice(game.user_choice)
  game.get_video()
  #game.get_prediction()
  #game.get_gesture(game.prediction)
  #game.get_winner(game.computer_choice, game.winner)

# %%
