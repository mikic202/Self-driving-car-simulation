import typing


class Car:
    def __init__(self, position: typing.List[float]) -> None:
        self._position = position
        self._speed = []
        self._acceleration = []
        self._rotation = []

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
