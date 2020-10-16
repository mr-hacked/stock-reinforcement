import numpy as np

import pandas as pd

import itertools

from time import sleep

from random import randint as rnd

import sys

import pickle

import matplotlib.pyplot as plt


def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)

    plt.title(title)

    plt.colorbar()

    tick_marks = np.arange(len(classes))

    plt.xticks(tick_marks, classes, rotation=45)

    plt.yticks(tick_marks, classes)

    if normalize:

        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

        print("Normalized confusion matrix")

    else:

        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.

    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],

                 horizontalalignment="center",

                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()

    plt.ylabel('True label')

    plt.xlabel('Predicted label')


def save(model, file):
    filename = str(file)
    pickle.dump(model, open(filename, "wb"))


def evaluate(model):
    if model == 'initial':
        loaded_model = pickle.load(open('model_i', 'rb'))
        result = loaded_model.score('/Testing_dataset')
        print(result)
    elif model == 'final':
        loaded_model = pickle.load(open('model_f', 'rb'))
        result = loaded_model.score('/Testing_dataset')
        print(result)
    else:
        print("Invalid Argument")