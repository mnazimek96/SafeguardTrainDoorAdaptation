from simulations import sim_1, sim_2, sim_3, sim_4, sim_5
import matplotlib.pyplot as plt
import PySimpleGUI as sg
from layout import gui
import os


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    exit = False
    window = gui()
    while True:
        event, values = window.read()
        input_data = 'data.csv'
        if event == '1':
            sim = sim_1.Sim1(input_data, 30, 180, 1, mod='+-', percent=2.5, difference=5)
        elif event == '2':
            sim = sim_2.Sim2(input_data, 30, 180, 1, mod='+', percent=2.5, difference=5)
            window['2'].Update(button_color=('black', 'yellow'))
        elif event == '3':
            sim = sim_3.Sim3(input_data, 30, 180, 1, mod='+', percent=2.5, difference=5)
        elif event == '4':
            sim = sim_4.Sim4(input_data, 30, 180, 1, mod='+', percent=2.5, difference=5)
        elif event == '5':
            sim = sim_5.Sim5(input_data, 0, 180, 1, mod='-+', percent=2.5, difference=5)
        elif event == '6':
            sim = sim_2.Sim2(input_data, 30, 180, 1, mod='random', percent=2.5, difference=5)
        elif event == 'quit' or event == sg.WIN_CLOSED:
            exit = True
            print('=========================')
            break
        else:
            print('Wrong input!')
            continue
        if not exit:
            animation = sim.simulate(1000, window)
            # mng = plt.get_current_fig_manager()
            # mng.full_screen_toggle()
            plt.show()




