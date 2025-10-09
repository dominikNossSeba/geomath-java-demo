"""Tiny 2D geometry helpers with a deliberate bug for demo purposes."""

from .vector2d import Vector2D
from .polygon_utils import area, is_convex

__all__ = ["Vector2D", "area", "is_convex"]
