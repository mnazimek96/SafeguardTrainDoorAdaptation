from simulations import Sim_1, Sim_2, Sim_3, Sim_4, Sim_5
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
            sim = Sim_1.Sim1(input_data,
                             int(values['-START-']),
                             int(values['-STOP-']),
                             float(values['-LEVEL-']),
                             values,
                             percent=2.5,
                             difference=5)
        elif event == '2':
            update_buttons(window, event)
            sim = Sim_2.Sim2(input_data,
                             int(values['-START-']),
                             int(values['-STOP-']),
                             float(values['-LEVEL-']),
                             values,
                             percent=2.5,
                             difference=5)
        elif event == '3':
            update_buttons(window, event)
            sim = Sim_3.Sim3(input_data,
                             int(values['-START-']),
                             int(values['-STOP-']),
                             float(values['-LEVEL-']),
                             values,
                             percent=2.5,
                             difference=5)
        elif event == '4':
            update_buttons(window, event)
            sim = Sim_4.Sim4(input_data,
                             int(values['-START-']),
                             int(values['-STOP-']),
                             float(values['-LEVEL-']),
                             values,
                             percent=2.5,
                             difference=5)
        elif event == '5':
            update_buttons(window, event)
            sim = Sim_5.Sim5(input_data,
                             int(values['-START-']),
                             int(values['-STOP-']),
                             float(values['-LEVEL-']),
                             values,
                             percent=2.5,
                             difference=5)
        elif event == '6':
            update_buttons(window, event)
            sim = Sim_2.Sim2(input_data,
                             int(values['-START-']),
                             int(values['-STOP-']),
                             float(values['-LEVEL-']),
                             values,
                             percent=2.5,
                             difference=5)
        elif event == 'QUIT' or event == sg.WIN_CLOSED:
            exit = True
            print('=========================')
            break
        elif event == '-RESET-':
            animation.event_source.start()
            plt.close(1)
            sim.i = 0
            sim.adapted = sim.saved
        elif event == '-PAUSE-':
            animation.event_source.stop()
            continue
        elif event == '-PLAY-':
            animation.event_source.start()
            plt.close(1)
        else:
            print(f'Wrong input! {event}')
            continue
        if not exit:
            animation = sim.simulate(1000, window)
            mng = plt.get_current_fig_manager()
            mng.full_screen_toggle()
            plt.show()




