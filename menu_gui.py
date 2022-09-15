from importlib.resources import path
import PySimpleGUI as sg
import os.path
import numpy as np
import cv2
import tkinter as tk
from PIL import ImageTk, Image


#put dictionary of all flavors and image paths here
flavor_dict = {"vanilla":"/Users/emrekurt/Desktop/Kod/gelato/V.png",
"chocolate":"/Users/emrekurt/Desktop/Kod/gelato/dark-chocolate-gelato-flavor.png"}


#image retrieval function
def get_image_path(strin):
    return flavor_dict[strin]

path_list = []


while True:
    print("flavors available: ", path_list)
    next_flavor = get_image_path(input("enter a flavor to add or remove: "))
    if next_flavor in path_list:
        path_list.remove(next_flavor)
        try:
            root = tk.Tk()
            root.attributes('-fullscreen', True)
            root.title("menu")
            display = np.concatenate(([cv2.imread(x) for x in path_list]), axis=1)
            blue, green, red, = cv2.split(display)
            display = cv2.merge((red, green, blue))
            im = Image.fromarray(display)
            imgtk = ImageTk.PhotoImage(image=im)
            label = tk.Label(root, image=imgtk)
            # root.mainloop()

        except:
            #cv2.imshow('menu', cv2.imread("/Users/emrekurt/Desktop/Kod/gelato/idle.jpg"))
            root = tk.Tk()
            root.attributes('-fullscreen', True)
            root.title("menu")
            display = np.concatenate(([cv2.imread(x) for x in path_list]), axis=1)
            blue, green, red, = cv2.split(display)
            display = cv2.merge((red, green, blue))
            im = Image.fromarray(display)
            imgtk = ImageTk.PhotoImage(image=im)
            label = tk.Label(root, image=imgtk)
            root.mainloop()
            #just idle pic

    else:
        path_list.append(next_flavor)
        try:
            display = np.concatenate(([cv2.imread(x) for x in path_list]), axis=1)
            root.mainloop()

        except:
            cv2.imshow('menu', cv2.imread("/Users/emrekurt/Desktop/Kod/gelato/idle.jpg"))
            root.mainloop()
            #just idle pic

       

    

