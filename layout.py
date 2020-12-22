import PySimpleGUI as sg


def gui():
    menu = [
        [sg.Frame(layout=[
            [
                sg.Button("1", button_color=('white', 'green')),
                sg.Button("2", button_color=('white', 'green')),
                sg.Button("3", button_color=('white', 'green')),
                sg.Button("4", button_color=('white', 'green')),
                sg.Button("5", button_color=('white', 'green')),
                sg.Button("6", button_color=('white', 'green')),
            ]], title='Simulations', relief=sg.RELIEF_SUNKEN,
                tooltip='Use these to set flags', background_color='grey')
        ],
        [sg.Button('quit', button_color=('white', 'red'))]
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

        ]
    ]

    window = sg.Window("Memory", layout, margins=(150, 50), background_color='grey')

    return window