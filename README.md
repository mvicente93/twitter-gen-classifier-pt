# twitter-gen-classifier-pt
> A supervised learning approach with Python to automatically identify gender in a Portuguese Twitter profile.

## Requirements

This classifier was trained with Scikit-Learn. The available script uses Tweepy to fetch the Twitter profile data.

To use it you must have installed on your system:

Numpy

SciPy

Scikit-Learn

Tweepy

## Usage

1. `git clone https://github.com/mvicente93/twitter-gen-classifier-pt.git`
2. `cd twitter-gen-classifier-pt`
3. `python twitter-gen-class.py [twitter screen name]`

## Other

The dataset used to train (and test) the classifier is on the folder datasets, use it as you please :)

## Future

Soon i'll release a Python script that allows the training of the model under diferent configurations.
The model's accuracy is currently at 86% with 1000 training samples and 400 testing samples.

## Info

The work was developed for my MSc dissertation in Computer and Telematics Engineering at [Universidade de Aveiro](http://www.ua.pt).
