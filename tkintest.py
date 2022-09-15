import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

root.attributes('-fullscreen', True)
root.title("menu")
 
# creating text label to display on window screen
img = ImageTk.PhotoImage(Image.open("/Users/emrekurt/Desktop/Kod/gelato/V.png"))
label = tk.Label(root, image=img)
label.grid(row=1, column=0, columnspan=3)
 
root.mainloop()