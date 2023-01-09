import csv
import pyperclip

abbr_dict = {}
with open('abbr.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        abbr_dict[row[1]] = row[0]

while True:
    input_text = input("Enter some text (type 'q' to quit): ")
    if input_text == "q":
        print("Goodbye!")
        break
    output_words = []
    chunks = input_text.split(" ")
    for chunk in chunks:
        if chunk in abbr_dict:
            output_words.append(abbr_dict[chunk])
        else:
            output_words.append(chunk)
    output_text = " ".join(output_words)
    print(output_text)
    with open("abbr.txt", "a") as output_file:
        output_file.write(output_text + "\n\n")
    output_text = output_text.rstrip()
    pyperclip.copy(output_text)