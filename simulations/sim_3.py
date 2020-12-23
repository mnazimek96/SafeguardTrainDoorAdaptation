from simulations import Simulation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


class Sim3(Simulation.Simulation):
    def simulate(self, cycles, window):
        description = 'Pick for x cycles and instant return to default - one time change'
        fig, ax, line, line1, line2 = self.prepare_sim(description)

        def update(i):
            label = 'Cycle {0} | saved {2} times in cycle: {1}'.format((i + 1), self.saved_in_cycle, self.save)
            line.set_ydata(self.saved)
            line1.set_ydata(self.adapted)
            line2.set_ydata(self.new)
            ax.set_xlabel(label)
            if i < 20:
                self.adapted = self.adapt(self.adapted, self.new)
            else:
                self.new = self.y_open
                self.adapted = self.adapt(self.adapted, self.new)

            for j in range(len(self.adapted)):
                difference = abs(self.saved[j] - self.adapted[j])
                threshold = (difference * 100) / self.saved[j]
                if threshold > self.percent and difference > self.difference:  # 2.5%; 5 - current difference
                    self.saved = self.adapted
                    self.save += 1
                    self.saved_in_cycle.append(i)
            window["-EPROM-"].update(f'Saved in cycle: \n {self.saved_in_cycle}')
            window["-RAM-"].update(f'cycle nr.: {i}')
            return line, ax

        animation = FuncAnimation(fig, update, repeat=False, frames=np.arange(0, cycles), interval=50)
        return animation