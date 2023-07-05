import sys
import pygame
from math import pi
from DifferentialDriveCar import DifferentialDriveCar
import threading


class Visualization:
    def __init__(self) -> None:
        self._WIN = pygame.display.set_mode((600, 600))
        self._car = DifferentialDriveCar([0, 0, 0], 2.0, 6.0)
        self.image = pygame.image.load('abc.png')
        self._draw_diagnostocs = False
        pygame.init()
        self._start()

    def _start(self):
        while True:
            self._check_quit()
            self._check_keystrokes()
            self._move_robot()
            self._WIN.fill((0, 0, 0))
            self._draw_diagnostics()
            self._draw_car()
            pygame.display.flip()

    def _check_keystrokes(self):
        keys_press = pygame.key.get_pressed()
        if keys_press[pygame.K_SPACE]:
            self._car.set_wheel_rotation_speed({"right": 2, "left": 0})
        elif keys_press[pygame.K_1]:
            self._car.set_wheel_rotation_speed({"right": 0, "left": 0})
        elif keys_press[pygame.K_2]:
            self._car.set_wheel_rotation_speed({"right": 1, "left": 1})
        elif keys_press[pygame.K_3]:
            self._car.set_wheel_rotation_speed({"right": 0, "left": 2})
        elif keys_press[pygame.K_d]:
            self._draw_diagnostocs = True
        elif keys_press[pygame.K_s]:
            self._draw_diagnostocs = False

    def _move_robot(self):
        self._car.move_robot_for(0.005)

    def _check_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def _draw_diagnostics(self):
        if self._draw_diagnostocs:
            pygame.draw.circle(self._WIN, (123, 123, 123), (self._car.position()[0]*15 + 100, self._car.position()[1]*15 + 100), self._car._wheel_distance/2*15)

    def _draw_car(self):
        w, h = self.image.get_size()
        self.blitRotate(self.image, (self._car.position()[0]*15 + 100, self._car.position()[1]*15 + 100), (w/2, h/2), -(self._car._rotation[2]/(2 * pi)*360)%360)

    def blitRotate(self, image, pos, originPos, angle):

        image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
        offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

        rotated_offset = offset_center_to_pivot.rotate(-angle)

        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

        rotated_image = pygame.transform.rotate(image, angle)
        rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

        self._WIN.blit(rotated_image, rotated_image_rect)


if __name__ == "__main__":
    win = Visualization()