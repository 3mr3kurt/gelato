import io
import os
import glob
import PySimpleGUI as sg

from PIL import Image, ImageTk

flavor_dict = {"vanilla":"/Users/emrekurt/Desktop/Kod/gelato/flavors/V.png",
"chocolate":"/Users/emrekurt/Desktop/Kod/gelato/flavors/dark-chocolate-gelato-flavor.png"}


def parse_folder(string):
    return flavor_dict[string]

def load_image(path, window):
    try:
        image = Image.open(path)
        image.thumbnail((400,400))
        photo_img = ImageTk.PhotoImage(image)
        window["image"].update(data=photo_img)
    except:
        print(f'Unable to open (path)!')


def main():
    elements = [
        [sg.Image(key="image")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), enable_events=True, key="file"),
            sg.FolderBrowse()
        ]
    ]
    window = sg.Window("Menu", elements, size=(475, 475))
    images = []
    location = 0

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "file":
            images = parse_folder(values["file"])
            if images:
                load_image(images[0], window)
    window.close()

    if __name__ == "__main__":
        main()