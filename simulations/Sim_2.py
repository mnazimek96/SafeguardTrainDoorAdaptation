from simulations import Simulation
from matplotlib.animation import FuncAnimation
import numpy as np


class Sim2(Simulation.Simulation):
    def simulate(self, cycles, window):
        description = 'Simulation of constant major change in current curve'
        fig, ax, line, line1, line2, line4, line5, line6 = self.prepare_sim(description)

        def update(i):
            # label = 'Cycle {0} | saved {2} times in cycle: {1}'.format((i + 1), self.saved_in_cycle, self.save)
            line.set_ydata(self.saved)
            line1.set_ydata(self.adapted)
            line2.set_ydata(self.new)
            line4.set_ydata(self.saved_1)
            line5.set_ydata(self.adapted_1)
            line6.set_ydata(self.new_c)

            self.adapted = self.adapt(self.adapted, self.new)
            self.adapted_1 = self.adapt(self.adapted_1, self.new_c)
            if len(self.adapted) == len(self.adapted_1):
                for j in range(len(self.adapted)):
                    difference = abs(self.saved[j] - self.adapted[j])
                    threshold = (difference * 100) / self.saved[j]
                    difference_c = abs(self.saved_1[j] - self.adapted_1[j])
                    threshold_c = (difference_c * 100) / self.saved_1[j]
                    if threshold > self.percent and difference > self.difference:  # 2.5%; 5 - current difference
                        self.saved = self.adapted
                        self.save += 1
                        self.saved_in_cycle.append(i)
                    if threshold_c > self.percent and difference_c > self.difference:  # 2.5%; 5 - current difference
                        self.saved_1 = self.adapted_1
                        self.save += 1
                        self.saved_in_cycle.append(i)
                window["-SAVED-"].update(f'Saved in cycle: \n {self.saved_in_cycle}')
                window["-RAM-"].update(f'cycle nr.: {i+1}')
                self.i += 1
            else:
                print('Adapted length ERROR!')
            return line, ax

        # optional argument for FuncAnimation - frames = np.arange(0, cycles)
        animation = FuncAnimation(fig, update, frames=np.arange(0, cycles), repeat=False, interval=50)
        return animation
