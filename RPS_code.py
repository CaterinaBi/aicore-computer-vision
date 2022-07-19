import cv2
from keras.models import load_model
import numpy as np
import random
import time

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

        self.computer_lives = 3
        self.user_lives = 3

        # layout miscellaneous prints
        self.spacer = "\n --------------------------------------------------------"

    def countdown_counter(self):
        countdown = 3
        print("\nPrepare to show me your chosen gesture in...")
        while countdown > 0:
            print(f'{countdown}')
            cv2.waitKey(1000)
            countdown -= 1
        print('\nShow your hand NOW!')
        # cv2.waitKey(1000)
    
    def counter_2(self):
        counter = 2
        while counter > 0:
            cv2.waitKey(1000)
            print("...")
            counter -= 1
    
    def get_computer_choice(self, computer_choice):
        # print(f"The computer choice is {computer_choice}")
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
    
    # gets gesture out of prediction
    def classify_output(self):
        """
        Uses the list of probabilities output from get_prediction
        to determine the image inputted in the camera.
        """
        prediction = self.get_prediction()
        choice_probability = {'Rock': prediction[0,1], 'Paper': prediction[0,2], 'Scissors': prediction[0,3]}
        self.user_prediction = max(choice_probability, key=choice_probability.get)
        # self.counter_2()
        print(f"The machine predicted that the user gesture was {self.user_prediction}")
        return self.user_prediction

    # determines winner
    def get_winner(self, computer_choice, user_choice, winner):
        computer_choice = self.get_computer_choice(computer_choice)
        user_choice = self.classify_output()
        self.counter_2()
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

    def remaining_lives(self):
        winner = self.get_winner(self.computer_choice, self.user_choice, self.winner)
        if winner == "user":
            self.computer_lives -= 1
            print(f"The computer now has {self.computer_lives} lives left.")
        elif winner == "computer":
            self.user_lives -=1
            print(f"The user now has {self.user_lives} lives left.")
        self.counter_2()
        if self.computer_lives == 0 or self.user_lives == 0:
            print(self.spacer, f"\n ****** GAME OVER! The {winner} wins the game! ******", self.spacer, "\n")

def play_game(gesture_list):
  round_number = 1
  game = Game(gesture_list)
  while game.computer_lives >= 1 and game.user_lives >= 1:
    # game.get_computer_choice(game.computer_choice)
    game.get_camera()
    print(game.spacer, f"\n ************** ROUND NUMBER {round_number} **************", game.spacer)
    game.countdown_counter()
    game.counter_2()
    # game.get_prediction()
    # game.classify_output()
    # user_prediction
    game.remaining_lives()
    round_number += 1
  # After the loop release the cap object
  game.cap.release()
  # Destroy all the windows
  game.cv2.destroyAllWindows()

if __name__ == '__main__':
  gesture_list = ["Rock", "Paper", "Scissors"]
  play_game(gesture_list)
# %%