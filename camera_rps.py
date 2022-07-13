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
    # self.user_choice = input("Please choose your move: ")

    # model, video and data attributes
    self.model = load_model('keras_model.h5')
    self.cap = cv2.VideoCapture(0)
    self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # messages to be displayed
    # font to be used in text messages
    self.font = cv2.FONT_HERSHEY_SIMPLEX
    self.intro_message = "WELCOME TO THE GAME OF ROCK, PAPER, SCISSORS!"
    self.instruction_message = "Press 'c' to continue, or 'q' to quit."

    self.user_choice = self.get_prediction()
    self.user = "user"
    self.computer = "computer"
    self.winner = str
    self.seconds = 0
    # self.start_time = 0
    # self.seconds = 0
    # self.show_time = 0
    # self.video_pause = 0
    # self.round_number = 1

    # layout miscellaneous prints
    self.spacer = "\n --------------------------------------------------------"

  def get_computer_choice(self, computer_choice):
    # print(f"The computer choice is {computer_choice}")
    return computer_choice

  # replaces get_user_choice()
  # do not change anything, it' projecting the video now
  def get_prediction(self):
    # timer 
    # start_time = time.time()
    # countdown = start_time + 5
    # end_time = start_time + 6
    # while start_time <= end_time:
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
    # self.classify_output(prediction)
    # if cv2.waitKey(1) & 0xFF == ord('c'):
    #    continue
    #  elif cv2.waitKey(1) & 0xFF == ord('q'):
    #    break
    return prediction

  #def countdown(self):
    #print("Countdown starts now. Show me your choice in...")
    #while True:
      #time.sleep(1)
      #self.seconds = time.time()
      #if self.seconds >= 1 and self.seconds <= 5:
        #print(f"{self.seconds} seconds left")
      #elif self.seconds == 6:
        #print("Show your choice to the camera NOW!")
        #break
  
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
      print(f"\nThe computer too chose {computer_choice}. No one wins this round!")
    elif computer_choice == "Rock":
      if user_choice == "Paper":
        winner = self.user
        #computer_lives -= 1
        print(f"\nThe computer chose {computer_choice}. The user wins this round!")
      elif user_choice == "Scissors":
        winner = self.computer
        #user_lives -= 1
        print(f"\nThe computer chose {computer_choice}. The computer wins this round!")
    elif computer_choice == "Paper":
      if user_choice == "Rock":
        winner = self.computer
        #user_lives -= 1
        print(f"\nThe computer chose {computer_choice}. The computer wins this round!")
      elif user_choice == "Scissors":
        winner = self.user
        #computer_lives -= 1
        print(f"\nThe computer chose {computer_choice}. The user wins this round!")
    else:
      if user_choice == "Paper":
        winner = self.computer
        #user_lives -= 1
        print(f"\nThe computer chose {computer_choice}. The computer wins this round!")
      elif user_choice == "Rock":
        winner = self.user
        #computer_lives -= 1
        print(f"\nThe computer chose {computer_choice}. The user wins this round!")
    return winner

# def close_window():
  # Press q to close the window
#   while True:
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#      break

def play_game(gesture_list):
  round_number = 1
  computer_lives = 3
  user_lives = 3
  # working like a charm, now camera stops after three rounds
  game = Game(gesture_list)
  while computer_lives >= 1 and user_lives >= 1:
    game.get_computer_choice(game.computer_choice)
    # game.countdown()
    # print(game.computer_choice)
    print(game.spacer)
    print(f"\n ************** ROUND NUMBER {round_number} **************")
    print(game.spacer)
    print("\nPrepare to show me your chosen gesture in 3 seconds!")
    # time.sleep(3)
    print("Show me your hand NOW!")
    #game.video_pause = time.time()
    game.get_prediction()
    # game.video_pause *= 100
    print("Thanks!")
    # game.start_time = time.time()
    # game.show_time = time.time() * 2
    # game.get_user_choice(game.user_choice)
    # game.classify_output()
    # Press q to close the window
    game.classify_output()
    print(f"The machine predicted that the user gesture was {game.user_prediction}")
    winner = game.get_winner(game.computer_choice, game.user_choice, game.winner)
    if winner == "user":
      computer_lives -= 1
      print(f"The computer now has {computer_lives} lives left.")
    elif winner == "computer":
      user_lives -=1
      print(f"The user now has {user_lives} lives left.")
    round_number += 1
    # Press q to close the window
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #  break
    # end-of-game if-statement
    # works fine
    if computer_lives == 0 or user_lives == 0:
      if computer_lives == 0:
        print("\nGAME OVER! The user wins the game!")
        print("\n --------------------------------------------------------\n")
      elif user_lives == 0:
        print("\nGAME OVER! The computer wins this game!")
        print("\n --------------------------------------------------------\n")
  # After the loop release the cap object
  game.cap.release()
  # Destroy all the windows
  game.cv2.destroyAllWindows()

if __name__ == '__main__':
  gesture_list = ["Rock", "Paper", "Scissors"]
  play_game(gesture_list)
# %%
