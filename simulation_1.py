# Simulation of constant small change in current curve

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
new = modify(y_open, 30, 180, 0.1)
adapted = y_open

fig, ax = plt.subplots(figsize=(14, 8))
fig.set_tight_layout(True)

line, = ax.plot(x, adapted, 'c--', linewidth=1, label='Saved [EPROM]')
line1, = ax.plot(x, adapted, 'k-.', linewidth=0.6, label='Adapting [RAM]')
line2, = ax.plot(x, adapted, 'r', linewidth=1, label='New [RAM]')

ax.plot(x, y_open, 'g', linewidth=1, label='Original [EPROM]')
plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0.)
plt.title('Simulation of constant small change in current curve')

save = 0
saved_in_cycle = []
saved = y_open


def update(i):
    global adapted, save, saved_in_cycle, saved
    label = 'Cycle {0} | saved {2} times in cycle: {1}'.format((i + 1), saved_in_cycle, save)
    line.set_ydata(saved)
    line1.set_ydata(adapted)
    line2.set_ydata(new)
    ax.set_xlabel(label)
    adapted = adapt(adapted, new)
    for j in range(len(adapted)):
        difference = abs(saved[j] - adapted[j])
        threshold = (difference * 100) / saved[j]
        if threshold > 2.5 and difference > 5:  # 2.5%; 5 - current difference
            saved = adapted
            save += 1
            saved_in_cycle.append(i)
    return line, ax


anim = FuncAnimation(fig, update, repeat=False, frames=np.arange(0, 1000), interval=50)

plt.show()
