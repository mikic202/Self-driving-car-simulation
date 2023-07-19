import pygame
from DifferentialDriveCar import DifferentialDriveCar
import math

METER_TO_PIXEL_RATIO = 15


class Line:
    def __init__(self, start: int, end: int) -> None:
        self._start = start if start[1] < end[1] else end
        self._end = end if start[1] < end[1] else start
        self._a = (start[1] - end[1])/(start[0] - end[0])
        self._b = start[1] - self._a*start[0]
        print(self._start)
        print(self._end)

    def draw_line(self, win: pygame.display) -> None:
        pygame.draw.line(win, (0, 0, 0), self._start, self._end)

    def check_robot_colision(self, robot: DifferentialDriveCar) -> bool:
        return self.interectLineCircle((robot.position()[0]*METER_TO_PIXEL_RATIO, robot.position()[1]*METER_TO_PIXEL_RATIO), robot.wheel_distance()/2*METER_TO_PIXEL_RATIO)

    def interectLineCircle(self, cpt, r):
        perpendicular_a = -1/self._a
        perpendicular_b = cpt[1]-perpendicular_a*cpt[0]
        intersection_ponit_x = (self._b - perpendicular_b)/(perpendicular_a - self._a)
        intersection_ponit_y = self._a * intersection_ponit_x + self._b
        dx = intersection_ponit_x - cpt[0]
        dy = intersection_ponit_y - cpt[1]
        distance = math.sqrt(dx*dx + dy*dy)
        if distance > r:
            return False
        if ((self._start[0] > cpt[0] and self._start[1] > cpt[1]) or (self._start[0] < cpt[0] and self._start[1] > cpt[1])) and math.sqrt((self._start[0]-cpt[0])**2 + (self._start[1]-cpt[1])**2) > r:
            return False
        if ((self._end[0] < cpt[0] and self._end[1] < cpt[1]) or (self._end[0] > cpt[0] and self._end[1] < cpt[1])) and math.sqrt((self._end[0]-cpt[0])**2 + (self._end[1]-cpt[1])**2) > r:
            return False
        return True