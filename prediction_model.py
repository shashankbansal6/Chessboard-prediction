import tensorflow as tf
import numpy as np
import sklearn.model_selection import train_test_split
rom __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import random


def changeForm(data):
    boards = []
    checklist = ['r','n', 'b', 'q', 'k', 'p', 'R','N', 'B', 'Q', 'K', 'P', '.']
    boards_final = []
    for line in data:
        temp = line.strip().split(" ")
        boards.append(temp)

    return np.array(boards)

def main():
    white_data = open("white_wins.txt", 'r')
    black_data = open("black_wins.txt", 'r')

    print(white_data)
