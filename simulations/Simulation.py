import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


class Simulation:
    def __init__(self, path, start, stop, level, values, percent, difference):
        self.path = path
        data = pd.read_csv(path, sep=';')
        data.columns = ['Position', 'Opening', 'Closing', 'Thresh_O', 'Thresh_C']
        self.x = data['Position'].to_numpy()
        self.y_open = data['Opening'].to_numpy()
        self.y_close = data['Closing'].to_numpy()
        self.thresh_O = data['Thresh_O'].to_numpy()
        self.thresh_C = data['Thresh_C'].to_numpy()
        self.adapted = self.y_open
        self.adapted_1 = self.y_close
        self.save = 0
        self.saved = self.y_open
        self.saved_1 = self.y_close
        self.saved_in_cycle = []
        if values['-MOD1-']:
            self.new = self.modify(start, stop, level)
            self.y_mod = self.modify(start, stop, level)
        elif values['-MOD3-']:
            new1 = self.modify(start, int(stop/2), level)[0:int(stop/2)]
            new2 = self.modify(int(stop/2), stop, -level)[int(stop/2):]
            self.new = self.y_mod = np.concatenate((new1, new2), axis=None)
        elif values['-MOD4-']:
            new1 = self.modify(start, int(stop/2), -level)[0:int(stop/2)]
            new2 = self.modify(int(stop/2), stop, level)[int(stop/2):]
            self.new = self.y_mod = np.concatenate((new1, new2), axis=None)
        elif values['-MOD2-']:
            self.new = self.modify(start, stop, -level)
            self.y_mod = self.modify(start, stop, -level)
        elif values['-MOD5-']:
            pieces = []
            N = 5
            for i in range(N):
                level = (np.random.random() * -3) + 1.5  # (-1.5, 1.5)
                m = ((stop - start) / N)
                a = int(start + ((stop - start) - ((N - i) * m)))
                b = int(stop - ((stop - start) - ((i+1) * m)))
                p = self.modify(a, b, level)
                piece = p[a:b]
                pieces = np.concatenate((pieces, piece), axis=None)
            self.new = self.y_mod = np.concatenate((self.y_open[0:start], pieces, self.y_open[stop:]), axis=None)
        else:
            self.new = self.modify(start, stop, level)
            self.y_mod = self.modify(start, stop, level)
        self.percent = percent
        self.difference = difference
        self.i = 0
        self.temp_adapt = 0
        self.temp_save = 0

    def modify(self, start, stop, level):
        y_new_open = []
        y_new_close = []
        iterator = 0
        if start != 0:
            for j in range(start):
                y_new_open.append(self.y_open[j])
                y_new_close.append(self.y_close[j])
        for i in range(start, stop):
            if i < stop - ((stop - start) / 2):
                if level > 0:
                    temp = self.y_open[i] + iterator
                    y_new_open.append(temp)
                    temp1 = self.y_close[i] + iterator
                    y_new_close.append(temp1)
                    iterator += level
                else:
                    temp = self.y_open[i] - iterator
                    y_new_open.append(temp)
                    temp1 = self.y_close[i] - iterator
                    y_new_close.append(temp1)
                    iterator -= level
            else:
                if level > 0:
                    temp = self.y_open[i] + iterator
                    y_new_open.append(temp)
                    temp1 = self.y_close[i] + iterator
                    y_new_close.append(temp1)
                    if self.y_open[i] < y_new_open[i]:
                        iterator -= level / 2
                    if self.y_close[i] < y_new_close[i]:
                        iterator -= level / 2
                else:
                    temp = self.y_open[i] - iterator
                    y_new_open.append(temp)
                    temp1 = self.y_close[i] - iterator
                    y_new_close.append(temp1)
                    if self.y_open[i] > y_new_open[i]:
                        iterator += level / 2
                    if self.y_close[i] > y_new_close[i]:
                        iterator += level / 2
        m = len(y_new_open)
        n = len(y_new_close)
        y_open = np.concatenate((y_new_open, self.y_open[m:len(self.y_open)]), axis=None)
        y_close = np.concatenate((y_new_close, self.y_close[m:len(self.y_close)]), axis=None)
        return y_open

    def adapt(self, original_y, modified_y):
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

    def prepare_sim(self, title):
        # ======== OPEN ============
        fig = plt.figure(figsize=(14, 7))
        ax = fig.add_subplot(211)
        fig.set_tight_layout(True)
        ax.set_facecolor('#EEEEEEEE')
        plt.grid(color='k', linestyle='-.', linewidth=0.4)
        plt.ylabel('Current [mA]')
        ax.set_xlabel('Position [OPEN]')
        plt.ylim(-300, 2000)

        line, = ax.plot(self.x, self.adapted, '#881ee4', linestyle='-', linewidth=1.4, label='Saved [EPROM]')
        line1, = ax.plot(self.x, self.adapted, 'k-.', linewidth=0.6, label='Adapting [RAM]')
        line2, = ax.plot(self.x, self.adapted, 'r', linewidth=1, label='New [RAM]')
        line3, = ax.plot(self.x, self.thresh_O, 'b', linewidth=1, label='Threshold')

        ax.plot(self.x, self.y_open, 'g', linewidth=1, label='Original [EPROM]')
        plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0.)
        plt.title(title)

        # ======= CLOSE ===========
        ax1 = fig.add_subplot(212)
        fig.set_tight_layout(True)
        ax1.set_facecolor('#EEEEEEEE')
        plt.grid(color='k', linestyle='-.', linewidth=0.4)
        plt.ylabel('Current [mA]')
        ax1.set_xlabel('Position [CLOSE]')
        plt.ylim(-300, 2000)

        line4, = ax1.plot(self.x, self.adapted_1, '#881ee4', linestyle='-', linewidth=1.4, label='Saved [EPROM]')
        line5, = ax1.plot(self.x, self.adapted_1, 'k-.', linewidth=0.6, label='Adapting [RAM]')
        line6, = ax1.plot(self.x, self.adapted_1, 'r', linewidth=1, label='New [RAM]')
        line7, = ax1.plot(self.x, self.thresh_C, 'b', linewidth=1, label='Threshold')

        ax1.plot(self.x, self.y_close, 'g', linewidth=1, label='Original [EPROM]')
        plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0.)

        return fig, ax, line, line1, line2

    # Tish function needs to be overwritten in child class
    def simulate(self, cycles, window):

        def update(i):
            pass

        pass
