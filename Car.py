import typing


class Car:
    def __init__(self, position: typing.List[int]) -> None:
        self._position = position
        self._speed = []
        self._acceleration = []

    def set_position(self, position: typing.List[int]) -> None:
        self._position = position

    def position(self) -> typing.List[int]:
        return self._position

    def set_speed(self, speed: typing.List[int]) -> None:
        self._speed = speed

    def speed(self) -> typing.List[int]:
        return self._speed

    def set_acceleration(self, acceleration: typing.List[int]) -> None:
        self._acceleration = acceleration

    def acceleration(self) -> typing.List[int]:
        return self._acceleration
