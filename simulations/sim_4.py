from simulations import Simulation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


class Sim4(Simulation.Simulation):
    def simulate(self, cycles):
        description = 'Pick and slow return to default - something in mechanism'
        fig, ax, line, line1, line2 = self.prepare_sim(description)

        def update(i):
            label = 'Cycle {0} | saved {2} times in cycle: {1}'.format((i + 1), self.saved_in_cycle, self.save)
            line.set_ydata(self.saved)
            line1.set_ydata(self.adapted)
            line2.set_ydata(self.new)
            ax.set_xlabel(label)
            self.adapted = self.adapt(self.adapted, self.new)
            self.new = self.adapt(self.new, self.y_open)
            for j in range(len(self.adapted)):
                difference = abs(self.saved[j] - self.adapted[j])
                threshold = (difference * 100) / self.saved[j]
                if threshold > self.percent and difference > self.difference:  # 2.5%; 5 - current difference
                    self.saved = self.adapted
                    self.save += 1
                    self.saved_in_cycle.append(i)
            return line, ax

        animation = FuncAnimation(fig, update, repeat=False, frames=np.arange(0, cycles), interval=50)
        return animation


if __name__ == "__main__":
    sim = Sim4('../data.csv', 30, 180, 1, percent=2.5, difference=5)
    anim = sim.simulate(1000)
    plt.show()
