"""Base types for Cube implementation"""

from enum import Enum
from typing import Optional, Tuple


class CubeException(Exception):
    pass


class Face(Enum):
    """Representation of a Cube Face"""
    L = 0
    R = 1
    D = 2
    U = 3
    B = 4
    F = 5

    def get_axis(self) -> int:
        """Return axis of movement (x=0, y=1, z=2)"""
        if self in (Face.L, Face.R):
            return 0
        if self in (Face.D, Face.U):
            return 1
        if self in (Face.B, Face.F):
            return 2

        raise CubeException("invalid face")  # pragma: no cover

    @staticmethod
    def create(face_str: str):
        """Create a CubeFace"""
        if face_str == "L":
            return Face.L
        if face_str == "R":
            return Face.R
        if face_str == "D":
            return Face.D
        if face_str == "U":
            return Face.U
        if face_str == "B":
            return Face.B
        if face_str == "F":
            return Face.F
        raise CubeException("invalid face " + str(face_str))


class Color(Enum):
    """Representation of the color of a Cube Piece"""
    R = 0
    O = 1
    W = 2
    Y = 3
    B = 4
    G = 5

    def __lt__(self, other):
        return self.name < other.name

    @staticmethod
    def create(color_str: str):
        """Create a CubeColor"""
        if color_str == "R":
            return Color.R
        if color_str == "O":
            return Color.O
        if color_str == "W":
            return Color.W
        if color_str == "Y":
            return Color.Y
        if color_str == "B":
            return Color.B
        if color_str == "G":
            return Color.G
        raise CubeException("invalid color " + str(color_str))


Coordinates = Tuple[int, int, int]
"""Defines the coordinates of a given CubePiece in 3D space"""

ColorOrientation = Tuple[Optional[Color], Optional[Color], Optional[Color]]
"""Defines the color orientation of a given CubePiece"""


class PieceType(Enum):
    """Type of piece"""
    CORNER = 3
    EDGE = 2
    CENTER = 1
    INNER = 0
