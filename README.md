# Computer Vision (AiCore training): Rock, Paper, Scissors!

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)](https://bitbucket.org/lbesson/ansi-colors)

Computer vision project that I am working on as part of my 'AI and Data Engineering' training at [AiCore](https://www.theaicore.com/).

![This is an image taken from the AiCore portal](images/portal_png.png)

> Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive "Rock Paper Scissors" game in which the user can play with the computer using the camera.

# Project structure

The project comprises of four milestones organised as follows:

1 - MILESTONE 1: Creation of the model.
- creation of the dataset to be used to train the model used in the programme;
- creation of the model using [Teachable Machine](https://teachablemachine.withgoogle.com/).

2 - MILESTONE 2: Installation of the dependencies.
- creation of a new virtual environment;
- model testing on the local machine.

3 - MILESTONE 3: Creation of a 'Rock, Paper, Scissors' game.
- store the user's and the computer's choices;
- figure out who won;
- create a function to simulate the game.

4 - MILESTONE 4: Using the camera to play the game.
- set up the camera and test the game;
- bonus implementations.

# Creation of the model

The creation of this computer vision application requires setting up a dataset to be used to train a model that recognises four different hand gestures: 1: Rock; 2- Paper; 3- Scissors; 4- None.

None is the lack of any gesture, while the first three gestures are those commonly used during the game of 'Rock, Paper, Scissors'. These are as in the image below.

<p align="center">
<img src="images/gestures.png" alt="This is an image of the gestures commonly used in the game of Rock, Paper, Scissors" />
</p>

Four representative pictures taken from the training images are provided below.

<p>
<img src="images/gestures_demo.png" alt="These are four images of the four different gestures taken from the training set" />
</p>

The creation of the dataset is followed by the training and creation of the model. These are done on [Teachable Machine](https://teachablemachine.withgoogle.com/), as I discuss in what follows.

## Creation of the dataset

The project required that the pictures used to train the model were half-bust shots of only one person, myself in this case. The creation of the pictures was done so as to limit overfitting, a common concern of all machine learning projects. 

While overfitting cannot be completely avoided in a model trained on images of only one person (the model is likely to perform poorly with users different from the one in the training images), it is possible to limit situations in which the model overfits because of a simple change of setting or outfit by varying the input images as much as possible.

To do so, the created images varied along the following axes (representative pictures are provided for reference):

- hair do (hair up/hair down)
- facial expression (resting vs. smiling face)
- hand (right vs left)
- setting (for a total of 5)
- outfit (for a total of 6)
- locus where the gesture is realised (all over the screen, both over the person's body and on the side).

## Output accuracy

A first model trained on less than 400 images turned out to be very deceiving, and almost completely unable to distinguish both 'Rock' and 'Paper' gestures. A second dataset was thus created, which included a total of 1007 images.

## Biases and limitations