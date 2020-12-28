import PySimpleGUI as sg
import matplotlib.pyplot as plt


def gui():
    menu = [
        [
            sg.Text('Start', size=(4, 1), background_color='grey'),
            sg.Text('Stop', size=(5, 1), background_color='grey'),
            sg.Text('Level', size=(4, 1), background_color='grey'),
            sg.Text('Mod', size=(31, 1), background_color='grey')
        ],
        [
            sg.HSeparator()
        ],
        [
            sg.InputText(default_text=30, key='-START-', size=(5, 1)),
            sg.InputText(default_text=180, key='-STOP-', size=(5, 1)),
            sg.InputText(default_text=1, key='-LEVEL-', size=(5, 1)),
            sg.Radio('+', key='-MOD1-', group_id='mod', size=(1, 1), default=True, background_color='#616161'),
            sg.Radio('-', key='-MOD2-', group_id='mod', size=(1, 1), background_color='#616161'),
            sg.Radio('+-', key='-MOD3-', group_id='mod', size=(2, 1), background_color='#616161'),
            sg.Radio('-+', key='-MOD4-', group_id='mod', size=(2, 1), background_color='#616161'),
            sg.Radio('rand', key='-MOD5-', group_id='mod', size=(4, 1), background_color='#616161'),
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
        [sg.Frame(layout=[
            [
                sg.Text('Original: ', key='-ORIGIN-', size=(15, 7)),
                sg.Text('Adaptation (10 cycles): ', key='-ADAPT_EPROM-', size=(15, 7)),
                sg.Text('Saved: ', key="-SAVED-", size=(15, 7)),
            ]], title='EPROM', relief=sg.RELIEF_SUNKEN,
            tooltip='Use these to set flags', background_color='grey')
        ],
        [sg.Frame(layout=[
            [
                sg.Text('Cycle nr.: ', key="-RAM-", size=(15, 7)),
                sg.Text('Ongoing: ', size=(15, 7)),
                sg.Text('Adapted: ', size=(15, 7)),
            ]], title='RAM', relief=sg.RELIEF_SUNKEN,
            tooltip='Use these to set flags', background_color='grey')
        ],
    ]

    layout = [
        [
            sg.Frame(layout=[[sg.Column(menu, background_color='grey')]], title='Options', background_color='grey'),
            # sg.Column(menu, background_color='grey'),
            # sg.VSeparator(),
        ],
        [
            sg.Column(memory_layout, background_color='grey'),
        ],
        [
            sg.HSeparator(),
        ],
        [
            sg.Button("QUIT", button_color=('white', 'red')),
            sg.Text('', size=(10, 1), background_color='grey'),  # SPACER
            sg.Button("PLAY", button_color=('white', '#74B72E'), disabled=True, key='-PLAY-'),
            sg.Button("PAUSE", button_color=('white', 'orange'), disabled=True, key='-PAUSE-'),
            sg.Button("RESET", button_color=('white', 'blue'), disabled=True, key='-RESET-')
        ]
    ]
    # when you want to open this window on second screen use - location=(2100, 330)
    window = sg.Window("Memory", layout, margins=(2, 2), background_color='grey')

    return window


def update_buttons(window, button):
    plt.close()
    for i in range(1, 6):
        if str(i) == button:
            window[button].update(button_color=('white', '#4CBB17'))
        else:
            window[str(i)].update(button_color=('white', 'green'))
    window['-PLAY-'].update(disabled=False)
    window['-PAUSE-'].update(disabled=False)
    window['-RESET-'].update(disabled=False)
    pass


def play(event, animation):
    if event == 'PAUSE':
        animation.event_source.stop()
    elif event == 'PLAY':
        animation.event_source.stop()
