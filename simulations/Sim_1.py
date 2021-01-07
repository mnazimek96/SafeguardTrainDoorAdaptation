from simulations import Simulation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


class Sim1(Simulation.Simulation):
    def simulate(self, cycles, window):
        description = 'Simulation of constant small change in current curve'
        fig, ax, line, line1, line2 = self.prepare_sim(description)

        def update(i):
            # label = 'Cycle {0} | saved {2} times in cycle: {1}'.format((i + 1), self.saved_in_cycle, self.save)
            line.set_ydata(self.saved)
            line1.set_ydata(self.adapted)
            line2.set_ydata(self.new)

            self.adapted = self.adapt(self.adapted, self.new)
            for j in range(len(self.adapted)):
                difference = abs(self.saved[j] - self.adapted[j])
                threshold = (difference * 100) / self.saved[j]
                if threshold > self.percent and difference > self.difference:  # 2.5%; 5 - current difference
                    self.saved = self.adapted
                    self.save += 1
                    self.saved_in_cycle.append(i)
            if self.i % 10 == 0:
                self.temp_adapt = self.adapted
                self.temp_save += 1
                window['-ADAPT_EPROM-'].update(f'Adaptation backup: \n{self.temp_save}')
            window["-SAVED-"].update(f'Saved in cycle: \n {self.saved_in_cycle}')
            window["-RAM-"].update(f'cycle nr.: {self.i}')
            self.i += 1
            return line, ax

        animation = FuncAnimation(fig, update, frames=np.arange(0, cycles), repeat=False, interval=50)
        return animation
