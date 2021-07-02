import tkinter as tk
import pyttsx3

class Widget():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TTS")
        self.root.resizable(0,0)
        self.root.configure(background="pink")
        self.label = tk.Label(self.root,text="Type something",bg="pink",fg="blue",font="arial 30 bold")
        self.label.pack()
        self.textbox = tk.Entry(self.root,width=35,font="arial 25")
        self.textbox.pack()
        self.button = tk.Button(self.root,text="SPEAK",bg="blue",fg="red",font="arial 25 bold")
        self.button.pack()
        self.root.mainloop()

if __name__ == "__main__":
    temp = Widget()