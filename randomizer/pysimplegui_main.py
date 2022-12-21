#!/usr/bin/env python3
import random
from pathlib import Path
from typing import List

import PySimpleGUI as sg


def pick(options: List[str]) -> str:
    randint = random.randint(0, len(options) - 1)
    return options[randint].strip()


# Define the window's contents
layout = [
    [sg.Text("Created especially for liefie!")],
    [sg.Text("Random number")],
    [
        sg.Spin(
            values=[i for i in range(-99999, 99999)],
            initial_value=0,
            key="-NR-START-",
            size=(10, 1),
        ),
        sg.Spin(
            values=[i for i in range(-99999, 99999)],
            initial_value=100,
            key="-NR-END-",
            size=(10, 1),
        ),
    ],
    [sg.Text("From File")],
    [sg.Input("", size=(50, 1), key="-FILENAME-"), sg.FileBrowse()],
    [sg.Text("From options")],
    [sg.Multiline("", size=(50, 10), key="-OPTIONS-")],
    [sg.Button("Generate"), sg.Button("Quit")],
    [sg.Text("Output")],
    [sg.Text(f"From number: {random.randint(0, 100)}", key="-NR-OUTPUT-")],
    [sg.Text(f"From File: ", key="-FILE-OUTPUT-")],
    [sg.Text(f"From options: ", key="-OPTIONS-OUTPUT-")],
    [sg.Text(f"Random skill: ", key="-SKILL-OUTPUT-")],
    [sg.Text(f"Random aspiration: ", key="-ASPIRATION-OUTPUT-")],
    [sg.Text(f"Random career: ", key="-CAREER-OUTPUT-")],
]

# Create the window
window = sg.Window("Awesome Randomizer", layout)

files = {
    "-CAREER-OUTPUT-": "careers.txt",
    "-ASPIRATION-OUTPUT-": "aspirations.txt",
    "-SKILL-OUTPUT-": "skills.txt",
}

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == "Quit":
        break

    if event == "Generate":
        randint = random.randint(values["-NR-START-"], values["-NR-END-"])
        window["-NR-OUTPUT-"].update(f"Generated: {randint}")

        check_path = Path(values["-FILENAME-"])
        if check_path.is_file():
            with open(check_path) as f:
                options = f.readlines()
                window["-FILE-OUTPUT-"].update(f"From File: {pick(options)}")

        if values["-OPTIONS-"]:
            options = values["-OPTIONS-"].split()
            window["-OPTIONS-OUTPUT-"].update(f"From options: {pick(options)}")

        for sg_elem, file in files.items():
            with open(Path(__file__).parent.resolve() / file) as f:
                options = f.readlines()
                random_type = sg_elem.split("-")[1].lower()
                window[sg_elem].update(f"Random {random_type}: {pick(options)}")


# Finish up by removing from the screen
window.close()
