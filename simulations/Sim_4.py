from simulations import Simulation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


class Sim4(Simulation.Simulation):
    def simulate(self, cycles, window):
        description = 'Pick and slow return to default - something in mechanism'
        fig, ax, line, line1, line2, line4, line5, line6 = self.prepare_sim(description)

        def update(i):
            # label = 'Cycle {0} | saved {2} times in cycle: {1}'.format((i + 1), self.saved_in_cycle, self.save)
            line.set_ydata(self.saved_open)
            line1.set_ydata(self.adapted_open)
            line2.set_ydata(self.new_open)
            line4.set_ydata(self.saved_close)
            line5.set_ydata(self.adapted_close)
            line6.set_ydata(self.new_close)

            self.adapted_open = self.adapt(self.adapted_open, self.new_open)
            self.adapted_close = self.adapt(self.adapted_close, self.new_close)
            self.new_open = self.adapt(self.new_open, self.first_y_open)
            self.new_close = self.adapt(self.new_close, self.first_y_close)

            if len(self.adapted_open) == len(self.adapted_close):
                for j in range(len(self.adapted_open)):
                    difference = abs(self.saved_open[j] - self.adapted_open[j])
                    difference_c = abs(self.saved_close[j] - self.adapted_close[j])
                    threshold = (difference * 100) / self.saved_open[j]
                    threshold_c = (difference_c * 100) / self.saved_close[j]
                    if threshold > self.percent and difference > self.difference:  # 2.5%; 5 - current difference
                        self.saved_open = self.adapted_open
                        self.save_count_open += 1
                        self.saved_in_cycle_open.append(i)
                    if threshold_c > self.percent and difference_c > self.difference:  # 2.5%; 5 - current difference
                        self.saved_close = self.adapted_close
                        self.save_count_close += 1
                        self.saved_in_cycle_close.append(i)

                window["-SAVED-"].update(f'OPEN - Saved [cycle]: \n {self.saved_in_cycle_open}')
                window["-SAVED_C-"].update(f'CLOSE - Saved [cycle]: \n {self.saved_in_cycle_close}')
                window["-RAM-"].update(f'cycle nr.: {self.i}')
                self.i += 1
            else:
                print('Adapted length ERROR!')
            return line, ax

        animation = FuncAnimation(fig, update, repeat=False, frames=np.arange(0, cycles), interval=50)
        return animation
