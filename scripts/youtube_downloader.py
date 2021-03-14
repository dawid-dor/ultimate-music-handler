import PySimpleGUI as sg
import youtube_dl
import threading


def youtube_downloader():
    def reset_fields(*argv):
        for arg in argv:
            window["-{}-".format(arg)].update("")
            values["-{}-".format(arg)] = ""

    def clear_info():
        window["-INFO-"].update("")

    DOWNLOAD_FOLDER = "H:/Muzyka YT"
    # Youtube parameters
    ydl_opts = {
        # Output folder
        "outtmpl": "{DOWNLOAD_FOLDER}/%({title})s-%(id)s.%(ext)s",
        # Parameters
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    # Change color scheme
    sg.theme("dark grey 9")

    # Define the window's contents
    layout = [
        [sg.Text("Download Folder: "), sg.Text("{}".format(DOWNLOAD_FOLDER))],
        [sg.Text("Video URL")],
        [sg.Input(key="-URL-")],
        [sg.Text("Video Name")],
        [sg.Input(key="-NAME-")],
        [sg.Text(size=(40, 1), key="-INFO-")],
        [sg.Button("Download"), sg.Button("Return")],
    ]

    # Create the window
    window = sg.Window("Youtube Downloader", layout)

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == "Return":
            break
        # Get song URL from window
        song_url = values["-URL-"]
        # Download song
        try:
            # Check if name field is empty - if its not, name the file as written in the field
            if len(values["-NAME-"]) > 0:
                ydl_opts["outtmpl"] = "{}/{}.%(ext)s".format(
                    DOWNLOAD_FOLDER, values["-NAME-"]
                )
            else:
                ydl_opts["outtmpl"] = "{}/%({title})s-%(id)s.%(ext)s".format(
                    DOWNLOAD_FOLDER
                )

            # Download the file
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([song_url])
            window["-INFO-"].update(
                "Succesfully downloaded a song!", text_color="green"
            )
            # Reset fields
            reset_fields("URL", "NAME")
            threading.Timer(3, clear_info).start()

        except Exception:
            window["-INFO-"].update(
                "Could not download song. Please check your URL.", text_color="red"
            )
            threading.Timer(3, clear_info).start()

    # Finish up by removing from the screen
    window.close()