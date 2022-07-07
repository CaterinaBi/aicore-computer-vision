import cv2
from keras.models import load_model
import numpy as np
import random
'''
    A game of Rock, Paper, Scissors in which the user plays against the computer.
    The user inputs their chosen gesture using the webcam.
    The user input is understood by the computer via a ML model, keras.model.h5.

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
    get_predicion(user_choice)
        Gets the user's input from the camera.
    get_winner(computer_choice, user_choice, winner)
        Returns the name of the winner.
    '''
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

class Game:
    def __init__(self, gesture_list):
        self.computer_choice = random.choice(gesture_list)
        self.user_choice = input("Please enter your choice: ")
        self.winner = str

    def get_computer_choice(self, computer_choice):
        return computer_choice
    
    def get_user_choice(self, user_choice):
        return user_choice

    def get_prediction(self):
        prediction = self.model.predict(self.data)
        index = np.argmax(prediction[0])
        return index

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
    game.get_prediction()
    game.get_winner(game.computer_choice, game.user_choice, game.winner)

if __name__ == '__main__':
    gesture_list = ["Rock", "Paper", "Scissors"]
    play_game(gesture_list)
# %%