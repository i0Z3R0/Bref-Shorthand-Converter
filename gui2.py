import csv
import pyperclip
import PySimpleGUI as sg

abbr_dict = {}
with open('abbr.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        abbr_dict[row[1]] = row[0]

layout = [[sg.Text('Bref Shorthand Convert', font=('Helvetica', 20))],
          [sg.Text('Enter some text: ')],
          [sg.Input()],
          [sg.Button('Copy to clipboard')],
          [sg.Output(size=(40, 20))],
          [sg.Text('Made by 0Z3R0', font=('Helvetica', 10))]]

window = sg.Window('Shorthand text', layout, size=(400, 200))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == sg.TIMEOUT_KEY:
        output_words = []
        chunks = values[0].split(" ")
        for chunk in chunks:
            if chunk in abbr_dict:
                output_words.append(abbr_dict[chunk])
            else:
                output_words.append(chunk)
        output_text = " ".join(output_words)

        print(output_text)

    elif event == 'Copy to clipboard':
        pyperclip.copy(output_text)

window.close()
