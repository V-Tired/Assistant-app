from tkinter import *
from assistant import Assistant
from timer import Timer
from schedule import calendar_display
from database import DbMaker
import pandas as pd
import pandastable as pt

"""Displays all of the GUI for the program and passes any input into assistant.py for sorting."""

# Colors
MID = "#50B498"
LIGHT = "#DEF9C4"
DARK = "#468585"
FONT = ("futura", 18, "bold")
BUTTON_FONT = ("futura", 12, "bold")
LABEL_FONT = ("futura", 11, "normal")

db = DbMaker()


class UI:
    def __init__(self):
        """Creates all GUI elements on initialization."""
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


    def process_request(self):
        """Sends request to assistant for sorting, displays error if request not recognized."""
        self.text = self.entry.get().lower()
        assistant = Assistant(self.window)
        try:
            num, value = assistant.check_request(self.text)
            self.entry.delete(first=0, last=END)
            return num, value
        except TypeError:
            self.entry.delete(first=0, last=END)
            error = Label(text="Sorry, I don't recognize that request. please try again.", bg=DARK, fg=LIGHT,
                          font=("futura", 10, "normal"))
            error.grid(column=0, row=19, columnspan=3, pady=5, )
            self.window.after(10000, error.grid_forget)
            num = None
            value = None
            return num, value


    def submit(self):
        """On button click, calls request processing, then checks the number to activate the corresponding
         GUI action."""
        num, value = self.process_request()

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
            self.display_options()

        elif num == 6:
            # Delete notes option
            print("eventually delete note")

        elif num == 7:
            # Show calendar
            if value is not None:
                calendar = calendar_display(m_input=value)
            else:
                calendar = calendar_display()
            calendar = calendar.replace(" ", "_")
            calendar_object = Label(text=calendar, font=BUTTON_FONT, bg=DARK, fg=LIGHT, justify="left")
            calendar_object.grid(column=2, row=2, columnspan=3, sticky="w")

        elif num == 8:
            # Display events from database
            self.display_database()

        elif num == 9:
            # Add event to Database
            note, month, day = value
            db.add_to_events(note, month, day)

        elif num == 10:
            # Delete event from Database
            event_id = value
            db.delete_entry(event_id)

        elif num is None:
            pass

    def display_options(self):
        """Displays all currently available options for the assistant."""
        options = ["Here is a list of phrases to try:",
                   "-What's the weather in (city) (state)? Note: only in US",
                   "-Make a note to ...",
                   "-Check notes",
                   "-Set a timer for...",
                   "-Show calendar",
                   "-Show (month) calendar",
                   "-Check events",
                   "-Create event: (event details) on (month) (day)"]
        row = 4
        for each in options:
            option = Label(text=each, bg=DARK, fg=LIGHT, font=LABEL_FONT)
            option.grid(column=0, row=row, padx=10, pady=6, columnspan=2, sticky="w")
            row += 1
            self.window.after(10000, option.grid_forget)

    def display_database(self):
        """Creates a separate window to display the events database in a table."""
        from_db = []
        columns = ["Id", "Note", "Month", "Day"]
        row = 4
        try:
            data = db.read_data(db.connection)
            for each in data:
                each = list(each)
                from_db.append(each)
            df = pd.DataFrame(from_db, columns=columns)

            dt_da1 = Toplevel()
            dt_da1.title('Event List')
            pd.set_option('future.no_silent_downcasting', True)
            dt_da_pt = pt.Table(dt_da1, dataframe=df, showtoolbar=True, showstatusbar=True)
            dt_da_pt.show()

        except FileNotFoundError:
            error = Label(text="Sorry, I could not find any events. Add some and try again.", bg=DARK, fg=LIGHT,
                          font=("futura", 10, "normal"))
            self.window.after(10000, error.grid_forget)
