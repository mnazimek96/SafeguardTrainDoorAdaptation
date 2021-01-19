from simulations import Simulation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


class Sim1(Simulation.Simulation):
    def simulate(self, cycles, window):
        description = 'Simulation of constant small change in current curve'
        fig, ax, line, line1, line2, line3, line4, line5, line6, line7 = self.prepare_sim(description)

        def update(i):
            # label = 'Cycle {0} | saved {2} times in cycle: {1}'.format((i + 1), self.saved_in_cycle, self.save)
            line.set_ydata(self.saved)
            line1.set_ydata(self.adapted)
            line2.set_ydata(self.new)
            line3.set_ydata(self.thresh_O)
            line4.set_ydata(self.saved_1)
            line5.set_ydata(self.adapted_1)
            line6.set_ydata(self.new_c)
            line7.set_ydata(self.thresh_C)

            self.adapted = self.adapt(self.adapted, self.new)
            self.adapted_1 = self.adapt(self.adapted_1, self.new_c)
            if len(self.adapted) == len(self.adapted_1):
                thresh_o, thresh_c = self.set_threshold(percent=12)
                for j in range(len(self.adapted)):
                    difference = abs(self.saved[j] - self.adapted[j])
                    threshold = (difference * 100) / self.saved[j]
                    difference_c = abs(self.saved_1[j] - self.adapted_1[j])
                    threshold_c = (difference_c * 100) / self.saved_1[j]
                    # 2.5%; 5 - current difference
                    if difference > thresh_o and self.i > 3:
                        self.saved = self.adapted
                        self.save += 1
                        self.saved_in_cycle.append(i)
                        self.i = 0
                        self.thresh_O = self.threshold_calculation(0)
                            # [x + (self.adapted[j] - temp[j]) for x in self.thresh_O]
                    if difference_c > thresh_c and self.j > 3:
                        self.saved_1 = self.adapted_1
                        self.save_c += 1
                        self.saved_in_cycle_c.append(i)
                        self.j = 0
                        self.thresh_C = self.threshold_calculation(1)

                window["-SAVED-"].update(f'OPEN - Saved [cycle]: \n {self.saved_in_cycle}')
                window["-SAVED_C-"].update(f'CLOSE - Saved [cycle]: \n {self.saved_in_cycle_c}')
                window["-RAM-"].update(f'cycle nr.: {self.cycle}')
                self.i += 1
                self.j += 1
                self.cycle += 1

            else:
                print('Adapted length ERROR!')

            return line, ax

        animation = FuncAnimation(fig, update, frames=np.arange(0, cycles), repeat=False, interval=50)
        return animation
