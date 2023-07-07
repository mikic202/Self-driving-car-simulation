import typing
from Car import Car
from math import inf, pi, cos, sin


class DifferentialDriveCar(Car):
    def __init__(self, position: typing.List[float], wheel_diametre: float, wheel_distance: float) -> None:
        super().__init__(position)
        self._wheel_rotation_speed = {"right": 0.0, "left": 0.0}  # w układzie odniesienia robota
        self._wheel_speed = {"right": 0.0, "left": 0.0}  # w układzie odniesienia robota
        self._wheel_diametre = wheel_diametre
        self._instantaneous_center_of_rotation = inf  # w układzie odniesienia robota
        self._wheel_distance = wheel_distance

    def wheel_rotation_speed(self) -> typing.Dict[str, float]:
        return self._wheel_rotation_speed

    def set_wheel_rotation_speed(self, wheel_rotation_speed: typing.Dict[str, float]) -> None:
        self._wheel_rotation_speed = wheel_rotation_speed

    def move_robot_for(self, time_in_s: float) -> None:
        dl = self._wheel_diametre * self._wheel_rotation_speed["left"] * time_in_s
        dp = self._wheel_diametre * self._wheel_rotation_speed["right"] * time_in_s

        fix = (dp + dl)/2
        fifi = (dp - dl)/self._wheel_distance
        if fifi == 0:
            self._instantaneous_center_of_rotation = inf
        else:
            self._instantaneous_center_of_rotation = fix/fifi
        self._position[0] += fix*cos(self._rotation[2] + fifi/2)
        self._position[1] += fix*sin(self._rotation[2] + fifi/2)
        self._rotation[2] += fifi
        self._rotation[2] = self._rotation[2] % (2*pi)

    def wheel_diametre(self) -> int:
        return self._wheel_diametre

    def wheel_distance(self) -> int:
        return self._wheel_distance

    def instantaneous_center_of_rotation(self) -> int:
        return self._instantaneous_center_of_rotation
