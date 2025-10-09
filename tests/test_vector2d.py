"""Tests for :mod:`geomath.vector2d`."""

import math

import pytest

from geomath import Vector2D


def assert_approx(v: Vector2D, x: float, y: float, tol: float) -> None:
    assert v.almost_equals(Vector2D(x, y), tol), (
        f"Expected approx ({x}, {y}) but got {v}"
    )


def test_add_sub_dot_norm() -> None:
    a = Vector2D(1, 2)
    b = Vector2D(3, 4)
    sum_vec = a.add(b)
    diff_vec = b.subtract(a)
    assert_approx(sum_vec, 4, 6, 1e-12)
    assert_approx(diff_vec, 2, 2, 1e-12)
    assert a.dot(b) == pytest.approx(11.0)
    assert a.norm() == pytest.approx(math.sqrt(5.0))


def test_rotate_degrees_90_fails_intentionally() -> None:
    # Rotating (1, 0) by +90 degrees should give (0, 1)
    v = Vector2D(1, 0).rotate(90.0, True)
    assert v.almost_equals(Vector2D(0, 1), 1e-9), (
        f"Expected (0,1) after 90° rotation, got {v}"
    )


def test_rotate_radians_ok() -> None:
    v = Vector2D(1, 0).rotate(math.pi / 2, False)
    assert v.almost_equals(Vector2D(0, 1), 1e-9)
