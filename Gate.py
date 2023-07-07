import pygame


class Gate:
    def __init__(self, start: int, end: int) -> None:
        self._start = start
        self._end = end

    def draw_line(self, win: pygame.display) -> None:
        pygame.draw.line(win, (123, 123, 123), self._start, self._end)
