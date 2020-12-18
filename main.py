from simulations import sim_1, sim_2, sim_3, sim_4, sim_5
import matplotlib.pyplot as plt
import os


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    exit = False
    print()
    choice = input('Simulation number: ')
    input_data = 'data.csv'
    if choice == '1':
        sim = sim_1.Sim1(input_data, 0, 30, 2, mod='+', percent=2.5, difference=5)
    elif choice == '2':
        sim = sim_2.Sim2(input_data, 30, 180, 1, mod='+', percent=2.5, difference=5)
    elif choice == '3':
        sim = sim_3.Sim3(input_data, 30, 180, 1, mod='+', percent=2.5, difference=5)
    elif choice == '4':
        sim = sim_4.Sim4(input_data, 30, 180, 1, mod='+', percent=2.5, difference=5)
    elif choice == '5':
        sim = sim_5.Sim5(input_data, 0, 180, 1, mod='-+', percent=2.5, difference=5)
    elif choice == 'exit':
        exit = True
        print('=========================')
    else:
        print('Wrong input!')

    animation = sim.simulate(1000)
    plt.show()




