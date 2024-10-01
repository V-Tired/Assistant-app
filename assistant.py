from weather import Weather
from notes import Notepad
from timer import Timer


months = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
          "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12}

weather = Weather()
note = Notepad()
timer = Timer()


class Assistant:

    def __init__(self, window):
        self.window = window

    def check_request(self, request: str) -> tuple[int | None, int | str | list | None]:
        """Check user input for certain keywords, passes the information into the corresponding function, then returns a
         designated number and any relevant information in the input that can be passed to UI for display"""
        if "timer" in request:
            total_count = timer.check_request(request)
            return 1, total_count

        elif "weather" in request:
            humidity = weather.check_weather(request)
            return 2, humidity

        elif "make" and "note" in request or "notes" in request:
            if "check" in request:
                content = note.check_notes()
                return 3, content

            elif "delete" not in request:
                new_note = note.make_note(request)
                return 4, new_note

        elif request == "help":
            return 5, ["list of options"]

        elif "delete" in request and "note" in request:
            return 6, [""]

        elif "calendar" in request:
            for month in months:
                if month in request:
                    return 7, months[month]
            return 7, None

        elif "check" in request or "view" in request and "events" in request:
            return 8, None

        elif "create" in request or "add" in request and "event" in request:
            export = None
            split_request = request.split(":")[1]
            event = split_request.split()
            for month in months:
                if month in event:
                    event_note = (event[0:event.index(month)])
                    event_note.pop()
                    joined_note = " ".join(event_note)
                    note_month = months[month]
                    note_day = event[event.index(month)+1]
                    export = (joined_note, note_month, note_day)
            return 9, export

        elif "delete" in request and "event" in request:
            request = request.split()
            event_id = request[2]
            return 10, event_id

        elif "send" in request and "email" in request:
            return 11, None

        else:
            return None, None
