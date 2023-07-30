import pygame
from DifferentialDriveCar import DifferentialDriveCar
import math

METER_TO_PIXEL_RATIO = 15


class Line:
    def __init__(self, start: int, end: int) -> None:
        self._line_colour = (0, 0, 0)
        self._start = start if start[0] < end[0] else end
        self._end = end if start[0] < end[0] else start
        self._is_diagonal = False
        if start[0] - end[0] == 0:
            self._is_diagonal = True
        else:
            self._a = (start[1] - end[1])/(start[0] - end[0])
            self._b = start[1] - self._a*start[0]

    def draw_line(self, win: pygame.display) -> None:
        pygame.draw.line(win, self._line_colour, self._start, self._end)

    def check_robot_colision(self, robot: DifferentialDriveCar) -> bool:
        return self.interectLineCircle((robot.position()[0]*METER_TO_PIXEL_RATIO, robot.position()[1]*METER_TO_PIXEL_RATIO), robot.wheel_distance()/2*METER_TO_PIXEL_RATIO)

    def interectLineCircle(self, cpt, r):

        if self._is_diagonal:
            return self._start[0] <= cpt[0] + r and self._start[0] >= cpt[0] - r

        if self._a == 0:
            if cpt[0] <= self._end[0] + r and cpt[0] >= self._start[0] - r and abs(self._end[1]-cpt[1]) <= r:
                return True
            return False

        perpendicular_a = -1/self._a
        perpendicular_b = cpt[1]-perpendicular_a*cpt[0]
        intersection_ponit_x = (self._b - perpendicular_b)/(perpendicular_a - self._a)
        intersection_ponit_y = self._a * intersection_ponit_x + self._b
        dx = intersection_ponit_x - cpt[0]
        dy = intersection_ponit_y - cpt[1]
        distance = math.sqrt(dx*dx + dy*dy)
        if distance > r:
            return False
        if intersection_ponit_x > self._end[0] and intersection_ponit_x > self._start[0] and math.sqrt((self._end[0]-cpt[0])**2 + (self._end[1]-cpt[1])**2) > r:
             return False
        if intersection_ponit_x < self._end[0] and intersection_ponit_x < self._start[0] and math.sqrt((self._start[0]-cpt[0])**2 + (self._start[1]-cpt[1])**2) > r:
             return False
        return True
