from pathlib import Path

"""Creates a text document to store any notes to be accessed later."""


class Notepad:

    def __init__(self):
        pass

    def make_note(self, note: str) -> str:
        """Creates a note in the notes.txt document."""
        note = note.split("to")
        memo = note[1]
        with open(file="notes.txt", mode="a") as file:
            file.writelines(f"{memo}\n")
        return memo

    def check_notes(self) -> list:
        """Accesses the notes.txt document(or creates one if there is none) and returns its info to be displayed
         by UI."""
        try:
            with open(file="notes.txt", mode="r") as file:
                content = file.readlines()
            if not content:
                return ["No notes currently available"]
            else:
                return content
        except FileNotFoundError:
            if not Path("notes.txt").exists():
                open(file="notes.txt", mode="w")
            return ["No notes currently available"]
