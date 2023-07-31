import sys
import pygame
from math import pi
from DifferentialDriveCar import DifferentialDriveCar
from time import time
from typing import List
from Gate import Gate
import json
from Line import Line
from TrackConstants import TrackConstants
import argparse

BACKGROUND_COLOR = (230, 230, 230)
DIAGNOSTIC_CIRCLE_COLOR = (220, 220, 220)
METER_TO_PIXEL_RATIO = 15
CAR_NUMBER = 10

class PygameCarObject:
    def __init__(self, car: DifferentialDriveCar, robot_number: int, image_path: str) -> None:
        self._robot_number = robot_number
        self._car = car
        self._image = pygame.image.load(image_path)
        self._image = pygame.transform.scale(self._image, (self._image.get_size()[0]*self._car.wheel_distance()*METER_TO_PIXEL_RATIO/self._image.get_size()[1], self._image.get_size()[1]*self._car.wheel_distance()*METER_TO_PIXEL_RATIO/self._image.get_size()[1]))
        self._last_update = time()

    def draw_car(self, window, draw_diagnostics: bool):
        w, h = self._image.get_size()
        self._draw_diagnostics(window, draw_diagnostics)
        self._rotate_car(window, self._image, (self._car.position()[0]*METER_TO_PIXEL_RATIO, self._car.position()[1]*METER_TO_PIXEL_RATIO), (w/2, h/2), -(self._car.rotation()[2]/(2 * pi)*360) % 360)

    def _rotate_car(self, window, image, pos, originPos, angle):
        image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1]-originPos[1]))
        offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

        rotated_offset = offset_center_to_pivot.rotate(-angle)

        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

        rotated_image = pygame.transform.rotate(image, angle)
        rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

        window.blit(rotated_image, rotated_image_rect)

    def _draw_diagnostics(self, window, draw_diagnostics: bool):
        if draw_diagnostics:
            pygame.draw.circle(window, DIAGNOSTIC_CIRCLE_COLOR, (self._car.position()[0]*METER_TO_PIXEL_RATIO, self._car.position()[1]*METER_TO_PIXEL_RATIO), self._car.wheel_distance()/2*METER_TO_PIXEL_RATIO)


class Visualization:
    def __init__(self, track_path: str, robot_image_path: str) -> None:
        self._track_path = track_path
        self._robot_image_path = robot_image_path
        self._track = []  # type: List[Line]
        self._gates = []  # type: List[Gate]
        self._robots = []  # type: List[PygameCarObject]
        self._start_point = [0, 0]
        self._WIN = pygame.display.set_mode((1200, 800))
        self._controled_car = 0
        self._draw_diagnostocs = False
        self._last_car_update = time()
        self._load_track()
        self._init_robots()
        pygame.init()
        self._start()

    def _init_robots(self):
        for i in range(0, CAR_NUMBER):
            self._robots.append(PygameCarObject(DifferentialDriveCar([self._start_point[0]//METER_TO_PIXEL_RATIO, self._start_point[1]//METER_TO_PIXEL_RATIO, 0], 2.0, 5.0), i, self._robot_image_path))

    def _load_track(self):
        with open(f'{self._track_path}{TrackConstants.TRACK_EXTENSION.value}', 'r') as f:
            data = json.load(f)
            for line in data[TrackConstants.TRACK.value]:
                self._track.append(Line(line[TrackConstants.LINE_START.value], line[TrackConstants.LINE_END.value]))
            for gate in data[TrackConstants.GATES.value]:
                self._gates.append(Gate(gate[TrackConstants.LINE_START.value], gate[TrackConstants.LINE_END.value]))
            self._start_point = data[TrackConstants.START_POINT.value]

    def _draw_track(self):
        for line in self._track:
            line.draw_line(self._WIN)
        for gate in self._gates:
            gate.draw_line(self._WIN)

    def _start(self) -> None:
        while True:
            self._check_events()
            self._check_keystrokes()
            self._move_robots()
            self._check_lines()
            self._WIN.fill(BACKGROUND_COLOR)
            self._draw_cars()
            self._draw_track()
            pygame.display.flip()

    def _check_lines(self):
        for line in self._track:
            if(line.check_robot_colision(self._robots[self._controled_car]._car)):
                line._line_colour = [255, 0, 0]
            else:
                line._line_colour = [0, 0, 0]

        for gate in self._gates:
            if gate.check_robot_colision(self._robots[self._controled_car]._car):
                gate._line_colour = [255, 0, 0]
            else:
                gate._line_colour = [60, 255, 60]

    def _check_keystrokes(self):
        keys_press = pygame.key.get_pressed()
        if keys_press[pygame.K_SPACE]:
            self._robots[self._controled_car]._car.set_wheel_rotation_speed({"right": 2, "left": 0})
        elif keys_press[pygame.K_1]:
            self._robots[self._controled_car]._car.set_wheel_rotation_speed({"right": 0, "left": 0})
        elif keys_press[pygame.K_2]:
            self._robots[self._controled_car]._car.set_wheel_rotation_speed({"right": 1, "left": 1})
        elif keys_press[pygame.K_3]:
            self._robots[self._controled_car]._car.set_wheel_rotation_speed({"right": 0, "left": 2})
        elif keys_press[pygame.K_d]:
            self._draw_diagnostocs = True
        elif keys_press[pygame.K_s]:
            self._draw_diagnostocs = False

    def _move_robots(self):
        for robot in self._robots:
            current_time = time()
            robot._car.move_robot_for(current_time - robot._last_update)
            robot._last_update = current_time

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self._controled_car += 1

    def _draw_cars(self):
        for robot in self._robots:
            robot.draw_car(self._WIN, self._draw_diagnostocs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("TrackCreator")
    parser.add_argument("-t", "--track", type=str, default="example_track", help="track file destination (without extension)")
    parser.add_argument("-r", "--robot", type=str, default="abc.png", help="robot image destination")
    args = parser.parse_args()
    win = Visualization(args.track, args.robot)
