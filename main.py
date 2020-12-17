import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from random import randint
import random
import os


def create_data(path):
    data = pd.read_csv(path, sep=';')
    data.columns = ['Position', 'Opening', 'Closing', '0', '0']
    x = data['Position'].to_numpy()
    y_open = data['Opening'].to_numpy()
    y_close = data['Closing'].to_numpy()

    return x, y_open, y_close


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    os.system('python simulation_1.py')
    os.system('python simulation_2.py')
    os.system('python simulation_3.py')
    os.system('python simulation_4.py')
    os.system('python simulation_5.py')

