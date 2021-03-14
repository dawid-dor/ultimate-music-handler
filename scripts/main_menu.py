import PySimpleGUI as sg
from .youtube_downloader import youtube_downloader


def main_menu():
    # Change color scheme
    sg.theme("dark grey 9")

    layout = [
        [sg.Button("Youtube Downloader", size=(30, 2))],
        [sg.Button("Metadata Changer", size=(30, 2))],
        [sg.Button("Song Cutter", size=(30, 2))],
    ]

    window = sg.Window("Ultimate Music Handler", layout)

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == "Youtube Downloader":
            youtube_downloader()

    window.close()