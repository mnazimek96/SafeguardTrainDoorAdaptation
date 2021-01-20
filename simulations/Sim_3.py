from simulations import Simulation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


class Sim3(Simulation.Simulation):
    def simulate(self, cycles, window):
        description = 'Pick for x cycles and instant return to default - one time change'
        fig, ax, line, line1, line2, line3, line4, line5, line6, line7 = self.prepare_sim(description)

        def update(i):
            # label = 'Cycle {0} | saved {2} times in cycle: {1}'.format((i + 1), self.saved_in_cycle, self.save)
            line.set_ydata(self.saved_open)
            line1.set_ydata(self.adapted_open)
            line2.set_ydata(self.new_open)
            line3.set_ydata(self.thresh_open)
            line4.set_ydata(self.saved_close)
            line5.set_ydata(self.adapted_close)
            line6.set_ydata(self.new_close)
            line7.set_ydata(self.thresh_close)

            if i < 20:
                self.adapted_open = self.adapt(self.adapted_open, self.new_open)
                self.adapted_close = self.adapt(self.adapted_close, self.new_close)
            else:
                self.new_open = self.first_y_open
                self.new_close = self.first_y_close
                self.adapted_open = self.adapt(self.adapted_open, self.new_open)
                self.adapted_close = self.adapt(self.adapted_close, self.new_close)
            if len(self.adapted_open) == len(self.adapted_close):
                thresh_o, thresh_c = self.set_threshold(12)
                for j in range(len(self.adapted_open)):
                    difference = abs(self.saved_open[j] - self.adapted_open[j])
                    difference_c = abs(self.saved_close[j] - self.adapted_close[j])
                    threshold = (difference * 100) / self.saved_open[j]
                    threshold_c = (difference_c * 100) / self.saved_close[j]
                    if difference > thresh_o and self.i > 3:  # 2.5%; 5 - current difference
                        self.saved_open = self.adapted_open
                        self.save_count_open += 1
                        self.saved_in_cycle_open.append(i)
                        self.thresh_open = self.threshold_calculation(0)
                        self.i = 0
                    if difference_c > thresh_c and self.j > 3:  # 2.5%; 5 - current difference
                        self.saved_close = self.adapted_close
                        self.save_count_close += 1
                        self.saved_in_cycle_close.append(i)
                        self.thresh_close = self.threshold_calculation(1)
                        self.j = 0

                window["-SAVED-"].update(f'OPEN - Saved [cycle]: \n {self.saved_in_cycle_open}')
                window["-SAVED_C-"].update(f'CLOSE - Saved [cycle]: \n {self.saved_in_cycle_close}')
                window["-RAM-"].update(f'cycle nr.: {self.cycle_count}')
                self.i += 1
                self.j += 1
                self.cycle_count += 1
            else:
                print('Adapted length ERROR!')
            return line, ax

        animation = FuncAnimation(fig, update, repeat=False, frames=np.arange(0, cycles), interval=50)
        return animation
