"""Polygon helper utilities."""

from __future__ import annotations

from typing import Sequence

from .vector2d import Vector2D


def area(points: Sequence[Vector2D] | None) -> float:
    """Return non-negative polygon area via the shoelace formula."""

    if points is None or len(points) < 3:
        return 0.0
    s = 0.0
    n = len(points)
    for i in range(n):
        a = points[i]
        b = points[(i + 1) % n]
        s += a.x * b.y - a.y * b.x
    return abs(s) * 0.5


def is_convex(points: Sequence[Vector2D] | None) -> bool:
    """Return True if the polygon is convex."""

    if points is None or len(points) < 3:
        return False

    n = len(points)
    sign = 0
    for i in range(n):
        a = points[i]
        b = points[(i + 1) % n]
        c = points[(i + 2) % n]
        ab = b.subtract(a)
        bc = c.subtract(b)
        cross = ab.cross(bc)
        if cross != 0.0:
            curr = 1 if cross > 0 else -1
            if sign == 0:
                sign = curr
            elif sign != curr:
                return False
    return True
