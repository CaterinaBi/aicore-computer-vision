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
    countdown_counter())
        Slows down the machine; asks the user to prepare to show their hand.
    counter_spacer()
        Slows down the program to make the application accessible for the user.
    get_computer_choice()
        Gets the computer's input randomly from gesture_list.
    get_camera()
        Turns on the camera to be used to play.
    get_prediction()
        Understands the user's input using probability.
    classify_output()
        Uses the list of probabilities from get_prediction() to determine the image inputted in the camera.
    get_winner()
        Returns the name of the winner.
    lives_counter()
        Keep track of the number of remaining lives for each user.
    '''
    def __init__(self, gesture_list):
        self.computer_choice = str

        # model, video and data attributes
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        self.user_choice = self.get_prediction()
        self.user = "user"
        self.computer = "computer"
        self.winner = str

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
    
    def counter_spacer(self):
        counter = 2
        while counter > 0:
            cv2.waitKey(1000)
            print("...")
            counter -= 1
    
    def get_computer_choice(self, computer_choice):
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
        self.data[0] = self.get_camera()
        prediction = self.model.predict(self.data)
        return prediction
    
    def classify_output(self):
        prediction = self.get_prediction()
        choice_probability = {'Rock': prediction[0,1], 'Paper': prediction[0,2], 'Scissors': prediction[0,3]}
        self.user_prediction = max(choice_probability, key=choice_probability.get)
        print(f"The machine predicted that the user gesture was {self.user_prediction}")
        return self.user_prediction

    def get_winner(self, computer_choice, user_choice, winner):
        computer_choice = self.get_computer_choice(computer_choice)
        user_choice = self.classify_output()
        self.counter_spacer()
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

    def lives_counter(self):
        winner = self.get_winner(self.computer_choice, self.user_choice, self.winner)
        if winner == "user":
            self.computer_lives -= 1
            print(f"The computer now has {self.computer_lives} lives left.")
        elif winner == "computer":
            self.user_lives -=1
            print(f"The user now has {self.user_lives} lives left.")
        self.counter_spacer()
        if self.computer_lives == 0 or self.user_lives == 0:
            print(self.spacer, f"\n ****** GAME OVER! The {winner} wins the game! ******", self.spacer, "\n")

def play_game(gesture_list):
  round_number = 1
  game = Game(gesture_list)
  while game.computer_lives >= 1 and game.user_lives >= 1:
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    game.get_camera()
    print(game.spacer, f"\n ************** ROUND NUMBER {round_number} **************", game.spacer)
    game.countdown_counter()
    game.counter_spacer()
    game.lives_counter()
    round_number += 1
  # After the loop release the cap object
  game.cap.release()
  # Destroy all the windows
  game.cv2.destroyAllWindows()

if __name__ == '__main__':
  gesture_list = ["Rock", "Paper", "Scissors"]
  play_game(gesture_list)
# %%