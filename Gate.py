import pygame
from DifferentialDriveCar import DifferentialDriveCar
import math
from Line import Line

METER_TO_PIXEL_RATIO = 15


class Gate(Line):
    def __init__(self, start: int, end: int) -> None:
        super().__init__(start, end)
        self._line_colour = (60, 255, 60)
