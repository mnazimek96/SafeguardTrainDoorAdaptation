from simulations import sim_1, sim_2, sim_3, sim_4, sim_5
import matplotlib.pyplot as plt
import PySimpleGUI as sg
from layout.main_layout import gui, update_buttons, play

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    exit = False
    window = gui()
    while True:
        event, values = window.read()
        input_data = 'data/data.csv'
        if event == '1':
            update_buttons(window, event)
            sim = sim_1.Sim1(input_data,
                             int(values['-START-']),
                             int(values['-STOP-']),
                             float(values['-LEVEL-']),
                             values,
                             percent=2.5,
                             difference=5)
            print(values)
        elif event == '2':
            update_buttons(window, event)
            sim = sim_2.Sim2(input_data,
                             int(values['-START-']),
                             int(values['-STOP-']),
                             float(values['-LEVEL-']),
                             values,
                             percent=2.5,
                             difference=5)
        elif event == '3':
            update_buttons(window, event)
            sim = sim_3.Sim3(input_data,
                             int(values['-START-']),
                             int(values['-STOP-']),
                             float(values['-LEVEL-']),
                             values,
                             percent=2.5,
                             difference=5)
        elif event == '4':
            update_buttons(window, event)
            sim = sim_4.Sim4(input_data,
                             int(values['-START-']),
                             int(values['-STOP-']),
                             float(values['-LEVEL-']),
                             values,
                             percent=2.5,
                             difference=5)
        elif event == '5':
            update_buttons(window, event)
            sim = sim_5.Sim5(input_data,
                             int(values['-START-']),
                             int(values['-STOP-']),
                             float(values['-LEVEL-']),
                             values,
                             percent=2.5,
                             difference=5)
        elif event == '6':
            update_buttons(window, event)
            sim = sim_2.Sim2(input_data,
                             int(values['-START-']),
                             int(values['-STOP-']),
                             float(values['-LEVEL-']),
                             values,
                             percent=2.5,
                             difference=5)
        elif event == 'PAUSE':
            animation.event_source.stop()
            continue
        elif event == 'QUIT' or event == sg.WIN_CLOSED:
            exit = True
            print('=========================')
            break
        else:
            print('Wrong input!')
            continue
        if not exit:
            animation = sim.simulate(1000, window)
            mng = plt.get_current_fig_manager()
            mng.full_screen_toggle()
            plt.show()




