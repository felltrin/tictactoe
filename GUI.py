import tkinter as tk
from tkinter import *
from tkinter import messagebox


class GUI:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("300x350")

        self.player_turn = "X"

        self.button_txt1 = tk.StringVar()
        self.button_txt2 = tk.StringVar()
        self.button_txt3 = tk.StringVar()
        self.button_txt4 = tk.StringVar()
        self.button_txt5 = tk.StringVar()
        self.button_txt6 = tk.StringVar()
        self.button_txt7 = tk.StringVar()
        self.button_txt8 = tk.StringVar()
        self.button_txt9 = tk.StringVar()

        self.game_button_frame = tk.Frame(self.root, bg="black", bd=5, relief=SUNKEN)
        self.game_button_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # instantiate the buttons
        self.button1 = tk.Button(self.game_button_frame, height=4, width=4, textvariable=self.button_txt1,
                                 command=lambda: self.button_click(1))
        self.button2 = tk.Button(self.game_button_frame, height=4, width=4, textvariable=self.button_txt2,
                                 command=lambda: self.button_click(2))
        self.button3 = tk.Button(self.game_button_frame, height=4, width=4, textvariable=self.button_txt3,
                                 command=lambda: self.button_click(3))
        self.button4 = tk.Button(self.game_button_frame, height=4, width=4, textvariable=self.button_txt4,
                                 command=lambda: self.button_click(4))
        self.button5 = tk.Button(self.game_button_frame, height=4, width=4, textvariable=self.button_txt5,
                                 command=lambda: self.button_click(5))
        self.button6 = tk.Button(self.game_button_frame, height=4, width=4, textvariable=self.button_txt6,
                                 command=lambda: self.button_click(6))
        self.button7 = tk.Button(self.game_button_frame, height=4, width=4, textvariable=self.button_txt7,
                                 command=lambda: self.button_click(7))
        self.button8 = tk.Button(self.game_button_frame, height=4, width=4, textvariable=self.button_txt8,
                                 command=lambda: self.button_click(8))
        self.button9 = tk.Button(self.game_button_frame, height=4, width=4, textvariable=self.button_txt9,
                                 command=lambda: self.button_click(9))

        # grid the buttons
        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)
        self.button3.grid(row=0, column=2)

        self.button4.grid(row=1, column=0)
        self.button5.grid(row=1, column=1)
        self.button6.grid(row=1, column=2)

        self.button7.grid(row=2, column=0)
        self.button8.grid(row=2, column=1)
        self.button9.grid(row=2, column=2)

        self.root.mainloop()

    def button_click(self, num_of_button):
        match num_of_button:
            case 1:
                self.button_txt1.set(self.player_turn)
            case 2:
                self.button_txt2.set(self.player_turn)
            case 3:
                self.button_txt3.set(self.player_turn)
            case 4:
                self.button_txt4.set(self.player_turn)
            case 5:
                self.button_txt5.set(self.player_turn)
            case 6:
                self.button_txt6.set(self.player_turn)
            case 7:
                self.button_txt7.set(self.player_turn)
            case 8:
                self.button_txt8.set(self.player_turn)
            case 9:
                self.button_txt9.set(self.player_turn)
            case _:
                print("Error has occurred")
        self.check_game_state()
        if self.player_turn == "X":
            self.player_turn = "O"
        else:
            self.player_turn = "X"

    def check_game_state(self):
        if self.button_txt1.get() == "X" or self.button_txt1.get() == "O":
            if self.button_txt1.get() == self.button_txt2.get() and self.button_txt2.get() == self.button_txt3.get():
                self.winning_message()
            elif self.button_txt1.get() == self.button_txt4.get() and self.button_txt4.get() == self.button_txt7.get():
                self.winning_message()
            elif self.button_txt1.get() == self.button_txt5.get() and self.button_txt5.get() == self.button_txt9.get():
                self.winning_message()
        if self.button_txt2.get() == "X" or self.button_txt2.get() == "O":
            if self.button_txt2.get() == self.button_txt5.get() and self.button_txt5.get() == self.button_txt8.get():
                self.winning_message()
        if self.button_txt3.get() == "X" or self.button_txt3.get() == "O":
            if self.button_txt3.get() == self.button_txt6.get() and self.button_txt6.get() == self.button_txt9.get():
                self.winning_message()
            elif self.button_txt3.get() == self.button_txt5.get() and self.button_txt5.get() == self.button_txt7.get():
                self.winning_message()
        if self.button_txt4.get() == "X" or self.button_txt4.get() == "O":
            if self.button_txt4.get() == self.button_txt5.get() and self.button_txt5.get() == self.button_txt6.get():
                self.winning_message()
        if self.button_txt7.get() == "X" or self.button_txt7.get() == "O":
            if self.button_txt7.get() == self.button_txt8.get() and self.button_txt8.get() == self.button_txt9.get():
                self.winning_message()
        if self.button_txt1.get() and self.button_txt2.get() and self.button_txt3.get() and self.button_txt4.get()\
                and self.button_txt5.get() and self.button_txt6.get() and self.button_txt7.get() and self.button_txt8.get()\
                and self.button_txt9.get():
            self.disable_all_buttons()
            if not messagebox.askyesno("Tic Tac Toe", "Sorry, this game is a draw, would you like to play again?"):
                self.root.destroy()
            else:
                self.reset()

    def winning_message(self):
        self.disable_all_buttons()
        if not messagebox.askyesno(title="Winner!", message="Congratulations! Player " + self.player_turn +
                                                            " won! Would you like to play again?"):
            self.root.destroy()
        else:
            self.reset()

    def disable_all_buttons(self):
        self.button1.config(state=DISABLED)
        self.button2.config(state=DISABLED)
        self.button3.config(state=DISABLED)
        self.button4.config(state=DISABLED)
        self.button5.config(state=DISABLED)
        self.button6.config(state=DISABLED)
        self.button7.config(state=DISABLED)
        self.button8.config(state=DISABLED)
        self.button9.config(state=DISABLED)

    def reset(self):
        self.button_txt1 = tk.StringVar()
        self.button_txt2 = tk.StringVar()
        self.button_txt3 = tk.StringVar()
        self.button_txt4 = tk.StringVar()
        self.button_txt5 = tk.StringVar()
        self.button_txt6 = tk.StringVar()
        self.button_txt7 = tk.StringVar()
        self.button_txt8 = tk.StringVar()
        self.button_txt9 = tk.StringVar()

        self.game_button_frame = tk.Frame(self.root, bg="black", bd=5, relief=SUNKEN)
        self.game_button_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # instantiate the buttons
        self.button1 = tk.Button(self.game_button_frame, height=4, width=4, textvariable=self.button_txt1,
                                 command=lambda: self.button_click(1))
        self.button2 = tk.Button(self.game_button_frame, height=4, width=4, textvariable=self.button_txt2,
                                 command=lambda: self.button_click(2))
        self.button3 = tk.Button(self.game_button_frame, height=4, width=4, textvariable=self.button_txt3,
                                 command=lambda: self.button_click(3))
        self.button4 = tk.Button(self.game_button_frame, height=4, width=4, textvariable=self.button_txt4,
                                 command=lambda: self.button_click(4))
        self.button5 = tk.Button(self.game_button_frame, height=4, width=4, textvariable=self.button_txt5,
                                 command=lambda: self.button_click(5))
        self.button6 = tk.Button(self.game_button_frame, height=4, width=4, textvariable=self.button_txt6,
                                 command=lambda: self.button_click(6))
        self.button7 = tk.Button(self.game_button_frame, height=4, width=4, textvariable=self.button_txt7,
                                 command=lambda: self.button_click(7))
        self.button8 = tk.Button(self.game_button_frame, height=4, width=4, textvariable=self.button_txt8,
                                 command=lambda: self.button_click(8))
        self.button9 = tk.Button(self.game_button_frame, height=4, width=4, textvariable=self.button_txt9,
                                 command=lambda: self.button_click(9))

        # grid the buttons
        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)
        self.button3.grid(row=0, column=2)

        self.button4.grid(row=1, column=0)
        self.button5.grid(row=1, column=1)
        self.button6.grid(row=1, column=2)

        self.button7.grid(row=2, column=0)
        self.button8.grid(row=2, column=1)
        self.button9.grid(row=2, column=2)
