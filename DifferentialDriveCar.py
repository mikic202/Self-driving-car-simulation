import typing
from Car import Car
from math import inf, pi, cos, sin


class DifferentialDriveCar(Car):
    def __init__(self, position: typing.List[float], whele_diametre: float, wheel_distance: float) -> None:
        super().__init__(position)
        self._wheel_rotation_speed = {"right": 0.0, "left": 0.0}  # w układzie odniesienia robota
        self._wheel_speed = {"right": 0.0, "left": 0.0}  # w układzie odniesienia robota
        self._whele_diametre = whele_diametre
        self._instantaneous_center_of_rotation = 0  # w układzie odniesienia robota
        self._wheel_distance = wheel_distance

    def wheel_rotation_speed(self) -> typing.Dict[str, float]:
        return self._wheel_rotation_speed

    def set_wheel_rotation_speed(self, wheel_rotation_speed: typing.Dict[str, float]) -> None:
        self._wheel_rotation_speed = wheel_rotation_speed
        # self._wheel_speed = {"left": wheel_rotation_speed["left"]*self._whele_diametre, "right": wheel_rotation_speed["right"]*self._whele_diametre}
        # self._speed = [0, sum(self._wheel_speed.values())/2]
        # self._angular_velocity = (self._wheel_speed["left"] - self._wheel_speed["right"])/self._wheel_distance
        # if self._angular_velocity > 0.0001 or self._angular_velocity < -0.0001:
        #     self._instantaneous_center_of_rotation = self._speed[1]/self._angular_velocity
        # else:
        #     self._instantaneous_center_of_rotation = inf

    def move_robot_for(self, time_in_s: float) -> None:
        dl = self._whele_diametre * self._wheel_rotation_speed["left"] * time_in_s
        dp = self._whele_diametre * self._wheel_rotation_speed["right"] * time_in_s
        # dfl = self._wheel_rotation_speed["left"] * time_in_s
        # dfp = self._wheel_rotation_speed["right"] * time_in_s
        # self._rotation[2] = (self._rotation[2] - (dfl - dfp)*self._wheel_distance)
        # self._position[0] = self._position[0] + self._whele_diametre * (dfl + dfp)/2*cos(pi*(self._rotation[2]))
        # self._position[1] = self._position[1] + self._whele_diametre * (dfl + dfp)/2*sin(pi*(self._rotation[2]))
        # delta_fi = (dl - dp)/(2 * self._wheel_distance)
        # delta_p = (dl + dp)/2

        fix = (dp + dl)/2
        fifi = (dp - dl)/self._wheel_distance
        if fifi == 0:
            d = fix
        else:
            d = 2 * fix/fifi*sin(fifi/2)
            R = fix/fifi
            # print(R)
        self._position[0] += fix*cos(self._rotation[2] + fifi/2)
        self._position[1] += fix*sin(self._rotation[2] + fifi/2)
        self._rotation[2] += fifi
        self._rotation[2] = self._rotation[2] % (2*pi)


if __name__ == "__main__":
    robot = DifferentialDriveCar([0, 0, 0], 1.0, 2.0)
    robot.set_wheel_rotation_speed({"right": 1, "left": 0})
    robot.move_robot_for(28)
    # robot.move_robot_for(4)
    # robot.move_robot_for(1)
    # robot.move_robot_for(1)
    print(robot.position())
