import pygame

"""Create a timer using user-inputted times."""

timer = None
pygame.mixer.init()


class Timer:
    def __int__(self):
        pass

    def check_request(self, request: str) -> int:
        """Checks through the input to see what variables to include in the timer."""
        input_list = request.split(" ")
        num = input_list.index("for")
        count = int(input_list[num + 1])
        var = input_list[num + 2]
        count2 = 0
        if "and" in input_list:
            count2 = int(input_list[num + 4])
            var2 = input_list[num + 5]
            if var2 == "minutes":
                count2 = count2 * 60
        if var == "minutes" or var == "minute":
            count = count * 60
        elif var == "hour" or var == "hours":
            count = count * 60 * 60
        elif var == "seconds":
            pass
        return count+count2

    def count_down(self, count: int, window, timer_text) -> None:
        """Begins countdown, displays timer, and plays a sound at end of timer."""
        minutes = count // 60
        seconds = count % 60
        if seconds < 10:
            seconds = f"0{seconds}"

        if count > 0:
            window.after(1000, self.count_down, count - 1, window, timer_text)
            timer_text.config(text=f"{minutes}:{seconds}")
        if count == 0:
            timer_text.grid_forget()
            pygame.mixer.music.load("1.mp3")
            pygame.mixer.music.play(loops=0)
