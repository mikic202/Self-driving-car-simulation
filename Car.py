import typing


class Car:
    def __init__(self, position: typing.List[float]) -> None:
        self._position = position
        self._speed = []  # w ukałdzie odniesienia robota
        self._acceleration = []  # w ukałdzie odniesienia robota
        self._rotation = [0, 0, 0]
        self._angular_velocity = float  # w ukałdzie odniesienia robota

    def set_position(self, position: typing.List[float]) -> None:
        self._position = position

    def position(self) -> typing.List[float]:
        return self._position

    def set_speed(self, speed: typing.List[float]) -> None:
        self._speed = speed

    def speed(self) -> typing.List[float]:
        return self._speed

    def set_acceleration(self, acceleration: typing.List[float]) -> None:
        self._acceleration = acceleration

    def acceleration(self) -> typing.List[float]:
        return self._acceleration

    def set_rotation(self, rotation: typing.List[float]) -> None:
        self._rotation = rotation

    def rotation(self) -> typing.List[float]:
        return self._rotation

    def set_angular_velocity(self, angular_velocity: float) -> None:
        self._angular_velocity = angular_velocity

    def angular_velocity(self) -> float:
        return self._angular_velocity
