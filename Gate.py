import pygame
from DifferentialDriveCar import DifferentialDriveCar
import math
from Line import Line

METER_TO_PIXEL_RATIO = 15


class Gate(Line):
    def draw_line(self, win: pygame.display) -> None:
        pygame.draw.line(win, (123, 123, 123), self._start, self._end)
