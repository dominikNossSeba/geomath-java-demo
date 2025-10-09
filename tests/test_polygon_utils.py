"""Tests for :mod:`geomath.polygon_utils`."""

from geomath import Vector2D, area, is_convex


def test_polygon_area_square() -> None:
    square = [
        Vector2D(0, 0),
        Vector2D(1, 0),
        Vector2D(1, 1),
        Vector2D(0, 1),
    ]
    assert area(square) == 1.0


def test_is_convex_true() -> None:
    square = [
        Vector2D(0, 0),
        Vector2D(1, 0),
        Vector2D(1, 1),
        Vector2D(0, 1),
    ]
    assert is_convex(square)


def test_is_convex_false() -> None:
    concave = [
        Vector2D(0, 0),
        Vector2D(2, 0),
        Vector2D(1, 1),
        Vector2D(2, 2),
        Vector2D(0, 2),
    ]
    assert not is_convex(concave)
