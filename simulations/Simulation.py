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
        self.thresh_open = data['Thresh_O'].to_numpy()
        self.thresh_close = data['Thresh_C'].to_numpy()
        first_data = pd.read_csv('data/first_cycle.csv', sep=';')
        first_data.columns = ['Position', 'Opening', 'Closing', 'Thresh_O', 'Thresh_C']
        self.first_x = first_data['Position'].to_numpy()
        self.first_y_open = first_data['Opening'].to_numpy()
        self.first_y_close = first_data['Closing'].to_numpy()
        self.adapted_open = self.first_y_open
        self.adapted_close = self.first_y_close
        self.save_count_open = 0
        self.save_count_close = 0
        self.saved_open = self.first_y_open
        self.saved_close = self.first_y_close
        self.saved_in_cycle_open = []
        self.saved_in_cycle_close = []
        if values['-MOD1-']:
            self.new_open, self.new_close = self.modify(start, stop, level)
            self.modified_y_open, self.modified_y_close = self.modify(start, stop, level)
        elif values['-MOD3-']:
            new1_open, new1_close = self.modify(start, int(stop / 2), level)[0:int(stop / 2)]
            new2_open, new2_close = self.modify(int(stop / 2), stop, -level)[int(stop / 2):]
            self.new_open = self.modified_y_open = np.concatenate((new1_open, new2_open), axis=None)
            self.new_close = self.modified_y_close = np.concatenate((new1_open, new2_open), axis=None)
        elif values['-MOD4-']:
            new1_open, new1_close = self.modify(start, int(stop / 2), -level)[0:int(stop / 2)]
            new2_open, new2_close = self.modify(int(stop / 2), stop, level)[int(stop / 2):]
            self.new_open = self.modified_y_open = np.concatenate((new1_open, new2_open), axis=None)
            self.new_close = self.modified_y_close = np.concatenate((new1_open, new2_open), axis=None)
        elif values['-MOD2-']:
            self.new_open, self.new_close = self.modify(start, stop, -level)
            self.modified_y_open, self.modified_y_close = self.modify(start, stop, -level)
        elif values['-MOD5-']:
            pieces = []
            pieces_1 = []
            N = 5
            for i in range(N):
                level = (np.random.random() * -3) + 1.5  # (-1.5, 1.5)
                m = ((stop - start) / N)
                a = int(start + ((stop - start) - ((N - i) * m)))
                b = int(stop - ((stop - start) - ((i + 1) * m)))
                o, c = self.modify(a, b, level)
                piece = o[a:b]
                pieces = np.concatenate((pieces, piece), axis=None)
                piece_1 = c[a:b]
                pieces_1 = np.concatenate((pieces_1, piece_1), axis=None)
            self.new_open = self.modified_y_open = np.concatenate((self.first_y_open[0:start], pieces, self.first_y_open[stop:]),
                                                                  axis=None)
            self.new_close = self.modified_y_close = np.concatenate(
                (self.first_y_close[0:start], pieces_1, self.first_y_close[stop:]), axis=None)
        else:
            self.new_open, self.new_close = self.modify(start, stop, level)
            self.modified_y_open, self.modified_y_close = self.modify(start, stop, level)

        self.percent = percent
        self.difference = difference
        self.i = 0
        self.j = 0
        self.temp_adapt = 0
        self.temp_save = 0
        self.cycle_count = 0

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
        y_close = np.concatenate((y_new_close, self.y_close[n:len(self.y_close)]), axis=None)
        return y_open, y_close

    def adapt(self, original_y, modified_y):
        count = 0
        new_tab = []
        for item in original_y:
            if item < modified_y[count]:
                new = ((item * 0.98) + (modified_y[count] * 0.02))
                new_tab.append(new)
            else:
                new = ((item * 0.98) + (modified_y[count] * 0.02))
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
        plt.ylim(-300, 2500)

        line, = ax.plot(self.x, self.adapted_open, '#881ee4', linestyle='-', linewidth=1.4, label='Saved [EPROM]')
        line1, = ax.plot(self.x, self.adapted_open, 'k-.', linewidth=0.6, label='Adapting [RAM]')
        line2, = ax.plot(self.x, self.adapted_open, 'r', linewidth=1, label='New [RAM]')
        line3, = ax.plot(self.x, self.thresh_open, 'b', linewidth=1, label='Threshold')

        ax.plot(self.first_x, self.first_y_open, 'g', linewidth=1, label='Original [EPROM]')
        plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0.)
        plt.title(title)

        # ======= CLOSE ===========
        ax1 = fig.add_subplot(212)
        fig.set_tight_layout(True)
        ax1.set_facecolor('#EEEEEEEE')
        plt.grid(color='k', linestyle='-.', linewidth=0.4)
        plt.ylabel('Current [mA]')
        ax1.set_xlabel('Position [CLOSE]')
        plt.ylim(-200, 1500)

        line4, = ax1.plot(self.x, self.adapted_close, '#881ee4', linestyle='-', linewidth=1.4, label='Saved [EPROM]')
        line5, = ax1.plot(self.x, self.adapted_close, 'k-.', linewidth=0.6, label='Adapting [RAM]')
        line6, = ax1.plot(self.x, self.adapted_close, 'r', linewidth=1, label='New [RAM]')
        line7, = ax1.plot(self.x, self.thresh_close, 'b', linewidth=1, label='Threshold')

        ax1.plot(self.first_x, self.first_y_close, 'g', linewidth=1, label='Original [EPROM]')
        plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0.)

        return fig, ax, line, line1, line2, line3, line4, line5, line6, line7

    def set_threshold(self, percent):
        high_o = high_c = low_o = low_c = 0
        for i in range(len(self.y_open)):
            high_o += self.thresh_open[i]
            high_c += self.thresh_close[i]
            low_o += self.saved_open[i]
            low_c += self.saved_close[i]
        average_difference_open = abs((high_o / len(self.y_open)) - (low_o / len(self.y_open)))
        average_difference_close = abs((high_c / len(self.y_open)) - (low_c / len(self.y_open)))
        threshold_open = average_difference_open * (percent/100)
        threshold_close = average_difference_close * (percent/100)
        print(f'{threshold_open}, {threshold_close}')

        return threshold_open, threshold_close

    def threshold_calculation(self, a):
        max_value = 0
        threshold = []
        if a == 0:
            param = self.adapted_open
            for i in range(int(len(param) / 3)):
                if param[i] > max_value:
                    max_value = param[i]
                    max_index = i
            for i in range(len(param)):
                if i < max_index + 20:
                    threshold.append(max_value + 1000)
                else:
                    threshold.append(param[i] + 800)
        elif a == 1:
            param = self.adapted_close
            for i in range(int(len(param) * 0.7), len(param)):
                if param[i] > max_value:
                    max_value = param[i]
                    max_index = i
            for i in range(len(param)):
                if i > max_index - 20:
                    threshold.append(max_value + 1000)
                else:
                    threshold.append(param[i] + 800)
        return threshold

    # This function needs to be overwritten in child class
    def simulate(self, cycles, window):
        def update(i):
            pass

        pass
