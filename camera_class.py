import cv2
from keras.models import load_model
import numpy as np
import random

# no __init___ ???? (it's called from the other file, Game class)
# get_output(): Opens camera and returns the probability that 
# the image belongs to each category (rock, paper, scissors, nothing).
# classify_output(self, prediction): Uses the list of probabilities output 
# from get_output to determine the image in the camera.
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
    get_prediction(user_choice)
        Gets the user's input from the camera.
    get_winner(computer_choice, user_choice, winner)
        Returns the name of the winner.
    '''

def get_prediction(self):
    self.model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while True: 
        self.ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = self.model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return prediction

# %%