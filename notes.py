from pathlib import Path


class Notepad:
    def __init__(self):
        pass

    def make_note(self, note):
        note = note.split("to")
        memo = note[1]
        with open(file="notes.txt", mode="a") as file:
            file.writelines(f"{memo}\n")
        return memo

    def check_notes(self):
        try:
            with open(file="notes.txt", mode="r") as file:
                content = file.readlines()
            return content
        except FileNotFoundError:
            if not Path("notes.txt").exists():
                open(file="notes.txt", mode="w")
            return ["No notes currently available"]
