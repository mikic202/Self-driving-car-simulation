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