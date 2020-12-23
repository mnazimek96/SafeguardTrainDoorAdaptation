import PySimpleGUI as sg
import matplotlib.pyplot as plt


def gui():
    menu = [
        [
            sg.Text('Start', size=(5, 1), background_color='grey'),
            sg.Text('Stop', size=(4, 1), background_color='grey'),
            sg.Text('Level', size=(4, 1), background_color='grey'),
            sg.Text('Mod', size=(31, 1), background_color='grey')
        ],
        [

        ],
        [
            sg.InputText(default_text=30, key='-START-', size=(5, 1)),
            sg.InputText(default_text=180, key='-STOP-', size=(5, 1)),
            sg.InputText(default_text=1, key='-LEVEL-', size=(5, 1)),
            sg.Radio('+', key='-MOD1-', group_id='radio', size=(1, 1), default=True, background_color='#616161'),
            sg.Radio('-', key='-MOD2-', group_id='radio', size=(1, 1), background_color='#616161'),
            sg.Radio('+-', key='-MOD3-', group_id='radio', size=(2, 1), background_color='#616161'),
            sg.Radio('-+', key='-MOD4-', group_id='radio', size=(2, 1), background_color='#616161'),
            sg.Radio('rand', key='-MOD5-', group_id='radio', size=(3, 1), background_color='#616161'),
        ],
        [sg.Frame(layout=[
            [
                sg.Button("1", button_color=('white', 'green'), size=(6, 1)),
                sg.Button("2", button_color=('white', 'green'), size=(6, 1)),
                sg.Button("3", button_color=('white', 'green'), size=(6, 1)),
                sg.Button("4", button_color=('white', 'green'), size=(6, 1)),
                sg.Button("5", button_color=('white', 'green'), size=(6, 1)),
                sg.Button("6", button_color=('white', 'green'), size=(6, 1)),
            ]], title='Simulations', relief=sg.RELIEF_SUNKEN,
                tooltip='Use these to set flags', background_color='grey')
        ],
    ]

    memory_layout = [
        [
            sg.Text('EPROM', background_color='grey', size=(6, 5)),
            sg.Text('Saved in cycle: ', key="-EPROM-", size=(22, 5))
        ],
        [
            sg.Text('RAM', background_color='grey', size=(6, 5)),
            sg.Text('cycle nr.: ', key="-RAM-", size=(22, 5))
        ],
    ]

    layout = [
        [
            sg.Column(menu, background_color='grey'),
            sg.VSeparator(),
            sg.Column(memory_layout, background_color='grey'),
        ],
        [
            sg.HSeparator(),
        ],
        [
            sg.Button("QUIT", button_color=('white', 'red')),
        ]
    ]

    window = sg.Window("Memory", layout, margins=(2, 2), background_color='grey')

    return window


def update_buttons(window, button):
    plt.close()
    for i in range(1, 6):
        if str(i) == button:
            window[button].update(button_color=('white', '#4CBB17'))
        else:
            window[str(i)].update(button_color=('white', 'green'))
    pass
