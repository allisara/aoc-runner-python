from __future__ import annotations
import pathlib
import math
from os import getenv


class Hailstone():
    def __init__(self, x: int, y: int, z: int, x_vel: int, y_vel: int, z_vel: int) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.z_vel = z_vel

        self.xy_slope = self.y_vel / self.x_vel
        self.b = self.y - self.xy_slope * self.x

    def __str__(self) -> str:
        return f"{self.x}, {self.y}, {self.z} @ {self.x_vel}, {self.y_vel}, {self.z_vel}"

    def get_xy_intersect(self, stone: Hailstone) -> tuple[float, float]:
        x_coord = (stone.b - self.b) / (self.xy_slope - stone.xy_slope)
        y_coord = self.xy_slope * x_coord + self.b

        return (x_coord, y_coord)

    def is_future_xy(self, coord: tuple[float, float]) -> bool:
        x, y = coord
        if self.x_vel > 0:
            return x > self.x
        else:
            return x < self.x

    def get_pos_at_t(self, t: int) -> tuple[int, int, int]:
        x = self.x + self.x_vel * t
        y = self.y + self.y_vel * t
        z = self.z + self.z_vel * t
        return (x, y, z)


# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process


def _format_dataset(dataset: "list[str]"):
    hailstones: list[Hailstone] = []

    for line in dataset:
        line = line.split(" @ ")
        coords = line[0].split(", ")
        velocities = line[1].split(", ")
        hailstones.append(Hailstone(int(coords[0]), int(coords[1]), int(
            coords[2]), int(velocities[0]), int(velocities[1]), int(velocities[2])))

    return hailstones


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines() if s.strip()]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)
