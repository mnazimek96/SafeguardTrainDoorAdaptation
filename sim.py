import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from functions import modify, adapt


class Simulation:
    def __init__(self, path):
        self.path = path
        data = pd.read_csv(path, sep=';')
        data.columns = ['Position', 'Opening', 'Closing', '0', '0']
        self.x = data['Position'].to_numpy()
        self.y_open = data['Opening'].to_numpy()
        self.y_close = data['Closing'].to_numpy()
        self.adapted = self.y_open
        self.save = 0
        self.saved = self.y_open
        self.saved_in_cycle = []

    def modify(self, start, stop, level):
        y_new = []
        iterator = 0
        if start != 0:
            for j in range(start):
                y_new.append(self.y_open[j])
        for i in range(start, stop):
            if i < stop - ((stop - start) / 2):
                if level > 0:
                    temp = self.y_open[i] + iterator
                    y_new.append(temp)
                    iterator += level
                else:
                    temp = self.y_open[i] - iterator
                    y_new.append(temp)
                    iterator -= level
            else:
                if level > 0:
                    temp = self.y_open[i] + iterator
                    y_new.append(temp)
                    if self.y_open[i] < y_new[i]:
                        iterator -= level / 2
                else:
                    temp = self.y_open[i] - iterator
                    y_new.append(temp)
                    if self.y_open[i] > y_new[i]:
                        iterator += level / 2
        m = len(y_new)
        y = np.concatenate((y_new, self.y_open[m:len(self.y_open)]), axis=None)
        return y

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
        fig, ax = plt.subplots(figsize=(14, 7))
        fig.set_tight_layout(True)

        line, = ax.plot(self.x, self.adapted, 'c--', linewidth=1, label='Saved [EPROM]')
        line1, = ax.plot(self.x, self.adapted, 'k-.', linewidth=0.6, label='Adapting [RAM]')
        line2, = ax.plot(self.x, self.adapted, 'r', linewidth=1, label='New [RAM]')

        ax.plot(self.x, self.y_open, 'g', linewidth=1, label='Original [EPROM]')
        plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0.)
        plt.title(title)

        return fig, ax, line, line1, line2

    def simulate(self, cycles):
        title = 'Simulation of constant small change in current curve'
        sim = Simulation('data.csv')
        new = sim.modify(30, 180, -0.5)
        fig, ax, line, line1, line2 = sim.prepare_sim(title)

        def update(i):
            label = 'Cycle {0} | saved {2} times in cycle: {1}'.format((i + 1), self.saved_in_cycle, self.save)
            line.set_ydata(self.saved)
            line1.set_ydata(self.adapted)
            line2.set_ydata(new)
            ax.set_xlabel(label)
            self.adapted = adapt(self.adapted, new)
            for j in range(len(self.adapted)):
                difference = abs(self.saved[j] - self.adapted[j])
                threshold = (difference * 100) / self.saved[j]
                if threshold > 2.5 and difference > 5:  # 2.5%; 5 - current difference
                    self.saved = self.adapted
                    self.save += 1
                    self.saved_in_cycle.append(i)
            return line, ax

        anim = FuncAnimation(fig, update, repeat=False, frames=np.arange(0, cycles), interval=50)
        return anim


if __name__ == "__main__":
    title = 'Simulation of constant small change in current curve'
    sim = Simulation('data.csv')
    anim = sim.simulate(1000)
    plt.show()

