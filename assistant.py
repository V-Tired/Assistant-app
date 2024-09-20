from weather import Weather
from notes import Notepad
from timer import Timer
from tkinter import *

weather = Weather()
note = Notepad()
timer = Timer()


class Assistant:

    def __init__(self, window):
        self.window = window

    def check_request(self, request):
        if "timer" in request:
            total_count = timer.check_request(request)
            return 1, total_count

        elif "weather" in request:
            humidity = weather.check_weather(request)
            return 2, humidity

        elif "note" in request or "notes" in request:
            if "check" in request:
                content = note.check_notes()
                return 3, content

            else:
                new_note = note.make_note(request)
                return 4, new_note

        elif request == "help":
            return 5, ["list of options"]

        elif "delete" in request and "note" in request:
            return 6
