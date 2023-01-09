# Bref-Shorthand-Converter

## Simple tool to convert normal text to Bref, an alphabetic shorthand system ([more info here](https://www.reddit.com/r/shorthand/comments/esjhdk/bref_shorthand/), [Bref manual here](https://drive.google.com/drive/folders/1PZcAYhusYGpaLHwMUBAdZURA25lKk2Mu))

# Prerequisites
- Latest version of Python 3
- PySimpleGui and pyperclip (in requirements.txt)

# Installation
1. git clone https://github.com/i0Z3R0/Bref-Shorthand-Converter.git
2. cd Bref-Shorthand-Converter
3. pip3 install -r requirements.txt
4. python3 main.py or python3 gui.py

# Usage
1. Run the program (main.py or gui.py)
2. Type in anything in normal English
3. The main.py program prints the text in Bref and saves it to abbr.txt
4. The gui.py program prints the text, click the button to copy to clipboard
5. If a word is not in the Bref dictionary (abbr.csv), it will just add the whole word to the output
