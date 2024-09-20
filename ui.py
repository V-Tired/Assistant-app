from tkinter import *
from assistant import Assistant
from timer import Timer

MID = "#50B498"
LIGHT = "#DEF9C4"
DARK = "#468585"
FONT = ("futura", 18, "bold")
BUTTON_FONT = ("futura", 12, "bold")
LABEL_FONT = ("futura", 11, "normal")


class UI:
    def __init__(self):
        self.text = ""
        # Window Config
        self.window = Tk()
        self.window.config(height=200, width=100, bg=DARK, pady=25, padx=25)
        self.window.minsize(200, 100)

        # Buttons, Labels, and Entries
        self.title = Label(text="Personal Assistant", bg=DARK, fg=LIGHT, font=FONT)
        self.title.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

        self.entry = Entry(width=50,)
        self.entry.grid(column=0, row=2, padx=10, pady=10, columnspan=2)

        self.submit_button = Button(text="Submit", bg=MID, fg=LIGHT, font=BUTTON_FONT, command=self.submit)
        self.submit_button.grid(column=0, row=3, columnspan=2, pady=10)

        self.footer = Label(text="Type help for suggestions", font=("futura", 8, "normal"), bg=DARK, fg=LIGHT)
        self.footer.grid(column=0, row=20, columnspan=3, pady=20)

    def submit(self):
        self.text = self.entry.get().lower()
        assistant = Assistant(self.window)
        try:
            num, value = assistant.check_request(self.text)
            self.entry.delete(first=0, last=END)
        except TypeError:
            self.entry.delete(first=0, last=END)
            error = Label(text="Sorry, I don't recognize that request. please try again.", bg=DARK, fg=LIGHT,
                          font=("futura", 10, "normal"))
            error.grid(column=0, row=19, columnspan=3, pady=5, )
            self.window.after(10000, error.grid_forget)
            num = None

        if num == 1:
            # Timer gets initiated
            timer = Timer()
            timer_text = Label(text="00:00", fg=DARK, bg=LIGHT, font=BUTTON_FONT)
            timer_text.grid(column=0, row=1, columnspan=3, pady=10,)
            timer.count_down(value, self.window, timer_text)

        elif num == 2:
            # Weather gets displayed
            weather = Label(text=value, bg=DARK, fg=LIGHT, font=LABEL_FONT)
            weather.grid(column=0, row=4, columnspan=2, sticky="w")
            self.window.after(10000, weather.grid_forget)

        elif num == 3:
            # All notes displayed
            row = 4
            for each in value:
                note_list = Label(text=each, bg=DARK, fg=LIGHT, font=LABEL_FONT)
                note_list.grid(column=0, row=row, padx=10, pady=5, columnspan=2, sticky="w")
                row += 1
                self.window.after(10000, note_list.grid_forget)

        elif num == 4:
            # New note being added displayed
            new_note = Label(text=value, bg=DARK, fg=LIGHT, font=LABEL_FONT)
            new_note.grid(column=0, row=4, columnspan=2, sticky="w")
            self.window.after(10000, new_note.grid_forget)

        elif num == 5:
            # Help options displayed
            options = ["Here is a list of phrases to try:", "-What's the weather in (city) (state)?",
                       "-Make a note: ...", "-Check notes", "-Set a timer for..."]
            row = 4
            for each in options:
                option = Label(text=each, bg=DARK, fg=LIGHT, font=LABEL_FONT)
                option.grid(column=0, row=row, padx=10, pady=6, columnspan=2, sticky="w")
                row += 1
                self.window.after(10000, option.grid_forget)

        elif num == 6:
            # Delete notes option
            pass
