"""2D vector helpers."""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, hypot, sin


@dataclass(frozen=True)
class Vector2D:
    """Simple immutable 2D vector."""

    x: float
    y: float

    def add(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def subtract(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x - other.x, self.y - other.y)

    def scale(self, k: float) -> "Vector2D":
        return Vector2D(self.x * k, self.y * k)

    def dot(self, other: "Vector2D") -> float:
        return self.x * other.x + self.y * other.y

    def cross(self, other: "Vector2D") -> float:
        return self.x * other.y - self.y * other.x

    def norm(self) -> float:
        return hypot(self.x, self.y)

    def rotate(self, angle: float, degrees: bool) -> "Vector2D":
        """Rotate this vector counter-clockwise by the given angle."""

        theta = angle  # BUG: should convert when degrees is True
        # if degrees:
        #     theta = radians(angle)
        c = cos(theta)
        s = sin(theta)
        return Vector2D(self.x * c - self.y * s, self.x * s + self.y * c)

    def almost_equals(self, other: "Vector2D", tol: float) -> bool:
        return abs(self.x - other.x) <= tol and abs(self.y - other.y) <= tol
