import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from random import randint
import random


def create_data(path):
    data = pd.read_csv(path, sep=';')
    data.columns = ['Position', 'Opening', 'Closing', '0', '0']
    x = data['Position'].to_numpy()
    y_open = data['Opening'].to_numpy()
    y_close = data['Closing'].to_numpy()

    return x, y_open, y_close


def modify(y_open, start, stop, level):
    y_new = []
    iter = 0
    if start != 0:
        for j in range(start):
            y_new.append(y_open[j])
    for i in range(start, stop):
        if i < stop - ((stop - start) / 2):
            if level > 0:
                temp = y_open[i] + iter
                y_new.append(temp)
                iter += level
            else:
                temp = y_open[i] - iter
                y_new.append(temp)
                iter -= level
        else:
            if level > 0:
                temp = y_open[i] + iter
                y_new.append(temp)
                if y_open[i] < y_new[i]:
                    iter -= level / 2
            else:
                temp = y_open[i] - iter
                y_new.append(temp)
                if y_open[i] > y_new[i]:
                    iter += level / 2
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


def visualise(origin, mod, adapted, description):
    plt.figure(figsize=(13, 4))
    plt.plot(x, mod, 'r', label='Modified')
    plt.plot(x, origin, 'g', label='Origin')
    plt.plot(x, adapted, 'k--', label='Saved')
    plt.title(description)
    plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0.)
    plt.show()


# simple constant change - mechanism wear
def simulation_1(data, cycles, start, stop, percent, current):
    description = 'simple constant change - mechanism wear'
    new = modify(data, start, stop, 1)
    adapted = data
    saved = data
    save = 0
    saved_in_cycle = []
    for i in range(cycles):
        adapted = adapt(adapted, new)
        for j in range(len(adapted)):
            difference = abs(saved[j] - adapted[j])
            threshold = (difference*100)/saved[j]
            if threshold > percent and difference > current:
                saved = adapted
                save += 1
                saved_in_cycle.append(i)
    print(f'{description} -> Saved {save} times in cycles: {saved_in_cycle}')
    visualise(y_open, new, saved, description)
    pass


# Pick for x cycles and instant return to default - one time change
def simulation_2(data, cycles, start, stop, percent, current, duration):
    description = 'Pick for x cycles and instant return to default - one time change'
    new = modify(data, start, stop, 3)
    adapted = data
    saved = data
    save = 0
    saved_in_cycle = []
    for i in range(cycles):
        if i < duration:
            adapted = adapt(adapted, new)
        else:
            new = data
            adapted = adapt(adapted, new)
        for j in range(len(adapted)):
            difference = abs(saved[j] - adapted[j])
            threshold = (difference*100)/saved[j]
            if threshold > percent and difference > current:
                saved = adapted
                save += 1
                saved_in_cycle.append(i)
    print(f'{description} -> Saved {save} times in cycles: {saved_in_cycle}')
    visualise(y_open, new, saved, description)
    pass


# Pick and slow return to default - something in mechanism
def simulation_3(data, cycles, start, stop, percent, current):
    description = 'Pick and slow return to default - something in mechanism'
    new = modify(data, start, stop, 1)
    adapted = data
    saved = data
    save = 0
    saved_in_cycle = []
    for i in range(cycles):
        adapted = adapt(adapted, new)
        new = adapt(new, data)
        for j in range(len(adapted)):
            difference = abs(saved[j] - adapted[j])
            threshold = (difference * 100) / saved[j]
            if threshold > percent and difference > current:
                saved = adapted
                save += 1
                saved_in_cycle.append(i)
    print(f'{description} -> Saved {save} times in cycles: {saved_in_cycle}')
    visualise(y_open, new, saved, description)
    pass


# Small change
def simulation_4(data, cycles, start, stop, percent, current):
    description = 'Small change'
    new = modify(data, start, stop, 0.1)
    adapted = data
    saved = data
    save = 0
    saved_in_cycle = []
    for i in range(cycles):
        adapted = adapt(adapted, new)
        for j in range(len(adapted)):
            difference = abs(saved[j] - adapted[j])
            threshold = (difference*100)/saved[j]
            if threshold > percent and difference > current:
                saved = adapted
                save += 1
                saved_in_cycle.append(i)
    print(f'{description} -> Saved {save} times in cycles: {saved_in_cycle}')
    visualise(y_open, new, saved, description)
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x, y_open, y_close = create_data('data.csv')
    # simulation_1(y_open, 1000, 30, 180, 2.5, 5)
    # simulation_4(y_open, 1000, 30, 180, 2.5, 5)
    # simulation_2(y_open, 1000, 30, 180, 2.5, 5, 5)
    simulation_3(y_open, 314, 30, 180, 2.5, 5)

