from simulations import Sim_1, Sim_2, Sim_3, Sim_4, Sim_5
import matplotlib.pyplot as plt
import PySimpleGUI as sg
from layout.main_layout import gui, update_buttons
from win32api import GetSystemMetrics
from support_functions.update_data import update_data
from communication.COM_connect import start_COM

input_data = 'data/new_data.csv'
port_nr = 'COM3'
percent = 10
difference = 100


def run():
    global input_data, port_nr, percent, difference
    screen_width = GetSystemMetrics(0)
    screen_height = GetSystemMetrics(1)
    exit = False
    window = gui()
    while True:
        # input_data have to be checked every iteration to make plotting data more real time
        event, values = window.read()
        if event == '1':
            if start_COM(port_nr):
                update_buttons(window, event)
                sim = Sim_1.Sim1(input_data,
                                 int(values['-START-']),
                                 int(values['-STOP-']),
                                 float(values['-LEVEL-']),
                                 values,
                                 percent,
                                 difference)
            else:
                break

        elif event == '2':
            if start_COM(port_nr):
                update_buttons(window, event)
                sim = Sim_2.Sim2(input_data,
                                 int(values['-START-']),
                                 int(values['-STOP-']),
                                 float(values['-LEVEL-']),
                                 values,
                                 percent,
                                 difference)
            else:
                break

        elif event == '3':
            if start_COM(port_nr):
                update_buttons(window, event)
                sim = Sim_3.Sim3(input_data,
                                 int(values['-START-']),
                                 int(values['-STOP-']),
                                 float(values['-LEVEL-']),
                                 values,
                                 percent,
                                 difference)
            else:
                break

        elif event == '4':
            if start_COM(port_nr):
                update_buttons(window, event)
                sim = Sim_4.Sim4(input_data,
                                 int(values['-START-']),
                                 int(values['-STOP-']),
                                 float(values['-LEVEL-']),
                                 values,
                                 percent,
                                 difference)
            else:
                break

        elif event == '5':
            if start_COM(port_nr):
                update_buttons(window, event)
                sim = Sim_5.Sim5(input_data,
                                 int(values['-START-']),
                                 int(values['-STOP-']),
                                 float(values['-LEVEL-']),
                                 values,
                                 percent,
                                 difference)
            else:
                break

        elif event == '6':
            if start_COM(port_nr):
                update_buttons(window, event)
                sim = Sim_2.Sim2(input_data,
                                 int(values['-START-']),
                                 int(values['-STOP-']),
                                 float(values['-LEVEL-']),
                                 values,
                                 percent,
                                 difference)
            else:
                break

        elif event == 'QUIT' or event == sg.WIN_CLOSED:
            exit = True
            print('\nApplication stopped without any errors.'
                  '\n======================================')
            break

        elif event == '-RESET-':
            animation.event_source.start()
            # sg.SystemTray.notify('Simulation RESET', 'Adapted curve returned to last saved one',
            #                      display_duration_in_ms=1,
            #                      location=((screen_width / 2) - 200, (screen_height / 2) - 40))
            plt.close(1)
            sim.i = 0
            sim.adapted_open = sim.saved_open

        elif event == '-PAUSE-':
            animation.event_source.stop()
            # sg.SystemTray.notify('Simulation STOP', 'Press PLAY to continue',
            #                      display_duration_in_ms=1,
            #                      location=((screen_width/2) - 200, (screen_height/2) - 40))
            continue

        elif event == '-PLAY-':
            animation.event_source.start()
            # sg.SystemTray.notify('Simulation PLAY', 'You can STOP and RESET',
            #                      display_duration_in_ms=1,
            #                      location=((screen_width / 2) - 200, (screen_height / 2) - 40))
            plt.close(1)

        else:
            print(f'Wrong input! {event}')
            continue
        if not exit:
            animation = sim.simulate(1000, window)
            mng = plt.get_current_fig_manager()
            mng.full_screen_toggle()
            plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
