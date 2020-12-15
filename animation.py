import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from main import modify, adapt

path = 'data.csv'
data = pd.read_csv(path, sep=';')
data.columns = ['Position', 'Opening', 'Closing', '0', '0']

x = data['Position'].to_numpy()
y_open = data['Opening'].to_numpy()
y_close = data['Closing'].to_numpy()
y_mod = modify(y_open, 40, 150, 1)
adapted = y_open

fig, ax = plt.subplots()
fig.set_tight_layout(True)

line, = ax.plot(x, adapted, 'c--', linewidth=1)
line1, = ax.plot(x, adapted, 'k-.', linewidth=0.6)
line2, = ax.plot(x, adapted, 'r', linewidth=1)

ax.plot(x, y_open, 'g', linewidth=1)

save = 0
saved_in_cycle = []
saved = y_open


def update(i):
    global adapted, save, saved_in_cycle, saved
    label = 'Cycle {0} saved in cycle: {1}'.format((i + 1), saved_in_cycle)
    line.set_ydata(saved)
    line1.set_ydata(adapted)
    line2.set_ydata(y_mod)
    ax.set_xlabel(label)
    adapted = adapt(adapted, y_mod)
    for j in range(len(adapted)):
        difference = abs(saved[j] - adapted[j])
        threshold = (difference * 100) / saved[j]
        if threshold > 2.5 and difference > 5:
            saved = adapted
            save += 1
            saved_in_cycle.append(i)
    return line, ax


anim = FuncAnimation(fig, update, repeat=False, frames=np.arange(0, 1000), interval=50)

plt.show()
