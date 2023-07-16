import tkinter as tk


class Start:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("300x350")

        self.label1 = tk.Label(self.root, text="Welcome to Tic Tac Toe!", font=("Sans Serif", 18))
        self.label1.pack()

        self.button_start = tk.Button(self.root, text="Start", font=("Sans Serif", 12))
        self.button_start.pack()

        self.button_help = tk.Button(self.root, text="Help", font=("Sans Serif", 12))
        self.button_help.pack()

        self.button_exit = tk.Button(self.root, text="Exit", font=("Sans Serif", 12))
        self.button_exit.pack()

        self.root.mainloop()
