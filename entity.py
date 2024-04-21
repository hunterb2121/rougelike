from typing import Tuple


class Entity:
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]) -> None:
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy