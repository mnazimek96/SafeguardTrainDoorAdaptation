import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from random import randint
import random
import os


def modify(y_open, start, stop, level):
    y_new = []
    iterator = 0
    if start != 0:
        for j in range(start):
            y_new.append(y_open[j])
    for i in range(start, stop):
        if i < stop - ((stop - start) / 2):
            if level > 0:
                temp = y_open[i] + iterator
                y_new.append(temp)
                iterator += level
            else:
                temp = y_open[i] - iterator
                y_new.append(temp)
                iterator -= level
        else:
            if level > 0:
                temp = y_open[i] + iterator
                y_new.append(temp)
                if y_open[i] < y_new[i]:
                    iterator -= level / 2
            else:
                temp = y_open[i] - iterator
                y_new.append(temp)
                if y_open[i] > y_new[i]:
                    iterator += level / 2
    M = len(y_new)
    y = np.concatenate((y_new, y_open[M:len(y_open)]), axis=None)

    return y


def adapt(original_y, modified_y):
    count = 0
    new_tab = []
    for item in original_y:
        if item < modified_y[count]:
            new = ((item * 0.99) + (modified_y[count] * 0.01))
            new_tab.append(new)
        else:
            new = ((item * 0.99) + (modified_y[count] * 0.01))
            new_tab.append(new)
        count += 1

    return new_tab
