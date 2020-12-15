import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

path = 'data.csv'
data = pd.read_csv(path, sep=';')
data.columns = ['Position', 'Opening', 'Closing', '0', '0']
x = data['Position'].to_numpy()
y_open = data['Opening'].to_numpy()
y_close = data['Closing'].to_numpy()

fig, ax = plt.subplots()
fig.set_tight_layout(True)

print('fig size: {0} DPI, size in inches {1}'.format(fig.get_dpi(), fig.get_size_inches()))

ax.plot(x, y_open)
line, = ax.plot(x, y_open, 'r-', linewidth=2)
line1, = ax.plot(x, y_open, 'g-', linewidth=2)


def update(i):
    label = 'timestep {0}'.format(i + 1)
    line.set_ydata(y_open + i)
    ax.set_xlabel(label)
    return line, ax


def update1(i):
    label = 'timestep {0}'.format(i + 1)
    line1.set_ydata(y_open - i)
    ax.set_xlabel(label)
    # return line1, ax


anim = FuncAnimation(fig, update, repeat=True, frames=np.arange(0, 100), interval=500)
anim1 = FuncAnimation(fig, update1, repeat=True, frames=np.arange(0, 100), interval=500)
plt.show()
