import PySimpleGUI as sg
from random import randint

def create_window():

    sg.theme('Python')
    layout = [
        [(sg.Text('Random number between:', font = 'Calibri 20'))],
        [sg.VPush()],
        [sg.Button('1-3', expand_x=True), sg.Button('1-5', expand_x=True), sg.Button('1-10', expand_x=True)],
        [sg.VPush()],
        [sg.Text('', key = 'Output', font = 'Calibri 30')],
        [sg.VPush()],
        [sg.Button('Reset')]


    ]

    return sg.Window('Guess game',layout, size = (500,400), element_justification = 'center')


window = create_window()

active = False
nr = randint(1, 20)

while True:
    event, values = window.read(timeout = 10)
    if event in (sg.WIN_CLOSED, '-Close-'):
        break

    if event == '1-3':
        nr = randint(1, 3)
        window['Output'].update(nr)

    if event == '1-5':
        nr = randint(1, 5)
        window['Output'].update(nr)

    if event == '1-10':
        nr = randint(1, 10)
        window['Output'].update(nr)

    if event == 'Reset':
        window['Output'].update('')

window.close()