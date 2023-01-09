import PySimpleGUI as sg
import csv
import pyperclip

abbr_dict = {}
with open('abbr.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        abbr_dict[row[1]] = row[0]

layout = [
    [sg.Text("Bref Shorthand", size=(40, 1), font=("Helvetica", 25), text_color="black")],
    [sg.Text("Made by 0Z3R0", size=(40, 1), font=("Helvetica", 10), text_color="black")],
    [sg.Input(key="input", size=(40, 1), font=("Helvetica", 20), enable_events=True)],
    [sg.Output(size=(40, 10), font=("Helvetica", 20), key="output")],
    [sg.Button("Copy to Clipboard", font=("Helvetica", 20)), sg.Exit(font=("Helvetica", 20))],
]

window = sg.Window("Bref Shorthand", layout, size=(400, 400))

while True:
    event, values = window.read()
    if event in (None, "Exit"):
        break
    if event == "input":
        input_text = values["input"]
        output_words = []
        chunks = input_text.split(" ")
        for chunk in chunks:
            if chunk in abbr_dict:
                output_words.append(abbr_dict[chunk])
            else:
                output_words.append(chunk)
        output_text = " ".join(output_words)
        window["output"].update(output_text)
    if event == "Copy to Clipboard":
        # Remove the trailing newline from output_text
        output_text = output_text.rstrip()
        # Copy output_text to the clipboard
        pyperclip.copy(output_text)

window.close()
