from simulations import sim_1
import matplotlib.pyplot as plt
import os


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sim = sim_1.Sim1('data.csv', 30, 180, 0.2, percent=2.5, difference=5)
    anim = sim.simulate(1000)
    plt.show()

