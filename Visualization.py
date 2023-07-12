import sys
import pygame
from math import pi
from DifferentialDriveCar import DifferentialDriveCar
from time import time
from typing import List

BACKGROUND_COLOR = (230, 230, 230)
DIAGNOSTIC_CIRCLE_COLOR = (220, 220, 220)
METER_TO_PIXEL_RATIO = 15
CAR_NUMBER = 10


class PygameCarObject:
    def __init__(self, car: DifferentialDriveCar) -> None:
        self._car = car
        self._image = pygame.image.load('abc.png')
        self._image = pygame.transform.scale(self._image, (self._image.get_size()[0]*self._car.wheel_distance()*METER_TO_PIXEL_RATIO/self._image.get_size()[1], self._image.get_size()[1]*self._car.wheel_distance()*METER_TO_PIXEL_RATIO/self._image.get_size()[1]))
        self._last_update = time()

    def draw_car(self, window, draw_diagnostics):
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

    def _draw_diagnostics(self, window, draw_diagnostics):
        if draw_diagnostics:
            pygame.draw.circle(window, DIAGNOSTIC_CIRCLE_COLOR, (self._car.position()[0]*METER_TO_PIXEL_RATIO, self._car.position()[1]*METER_TO_PIXEL_RATIO), self._car.wheel_distance()/2*METER_TO_PIXEL_RATIO)


class Visualization:
    def __init__(self) -> None:
        self._WIN = pygame.display.set_mode((600, 600))
        self._robots = []  # type: List[PygameCarObject]
        # self._car = DifferentialDriveCar([10, 10, 0], 2.0, 12.0)
        # self._image = pygame.image.load('abc.png')
        # self._image = pygame.transform.scale(self._image, (self._image.get_size()[0]*self._car.wheel_distance()*METER_TO_PIXEL_RATIO/self._image.get_size()[1], self._image.get_size()[1]*self._car.wheel_distance()*METER_TO_PIXEL_RATIO/self._image.get_size()[1]))
        self._controled_car = 0
        self._draw_diagnostocs = False
        self._last_car_update = time()
        self._init_robots()
        pygame.init()
        self._start()

    def _init_robots(self):
        for i in range(0, CAR_NUMBER):
            self._robots.append(PygameCarObject(DifferentialDriveCar([10, 10, 0], 2.0, 12.0)))

    def _start(self) -> None:
        while True:
            self._check_events()
            self._check_keystrokes()
            self.move_robots()
            self._WIN.fill(BACKGROUND_COLOR)
            self._draw_cars()
            pygame.display.flip()

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

    def move_robots(self):
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
    # threading.Thread(target=Visualization())
    win = Visualization()
